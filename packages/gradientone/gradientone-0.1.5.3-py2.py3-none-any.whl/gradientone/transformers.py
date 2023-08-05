#!/usr/bin/python

"""

Copyright (C) 2016-2017 GradientOne Inc. - All Rights Reserved
Unauthorized copying or distribution of this file is strictly prohibited
without the express permission of GradientOne Inc.

"""

import datetime
import time
import collections
import json
import logging
import os.path
import traceback
import copy
import gateway_helpers
from configparser import ConfigParser
from gateway_helpers import dt2ms, post_log, \
    round_sig, logger
from scope import IviScopeClient


cfg = ConfigParser()
cfg.read('/etc/gradient_one.cfg')
COMMON_SETTINGS = cfg['common']
CLIENT_SETTINGS = cfg['client']
try:
    TMPDIR = CLIENT_SETTINGS["TMPDIR"]
except:
    TMPDIR = "/tmp"

SENTRY_CLIENT = gateway_helpers.get_sentry()

CLIENT_ID = 'ORIGINAL'
SAMPLE_FILE = 'MDO30121M.txt'
CONFIG_URL = ("https://" + COMMON_SETTINGS['DOMAIN'] + "/testplansummary/" +
              COMMON_SETTINGS['COMPANYNAME'] + '/' +
              COMMON_SETTINGS['HARDWARENAME'])
COMPANYNAME = COMMON_SETTINGS['COMPANYNAME']
HARDWARENAME = COMMON_SETTINGS['HARDWARENAME']
MAX_VALID_MEAS_VAL = 1e36
BASE_URL = gateway_helpers.BASE_URL
DEFAULT_TEK_CONFIG = {
    'acquisition': {
        'type': 'average',
        'start_time': -4.999999999999996e-06,
        'time_per_record': 9.999999999999999e-06,
        'number_of_envelopes': 0,
        'number_of_averages': 512,
        'number_of_points_minimum': 1000,
    },
    'trigger': {
        'type': 'edge',
        'source': 'ch1',
        'coupling': 'dc',
        'level': 0.288,
    },
    'trigger_edge_slope': 'positive',
    'channels': {
        'ch1': {
            'channel_enabled': True,
            'channel_offset': 0,
            'channel_range': 2,
            'channel_coupling': 'dc',
        },
        'ch2': {
            'channel_enabled': False,
            'channel_offset': 0,
            'channel_range': 1,
            'channel_coupling': 'dc',
        },
        'ch3': {
            'channel_enabled': False,
            'channel_offset': 0,
            'channel_range': 1,
            'channel_coupling': 'dc',
        },
        'ch4': {
            'channel_enabled': False,
            'channel_offset': 0,
            'channel_range': 1,
            'channel_coupling': 'dc',
        },
    },
    'outputs': {
        'enabled': False,
        'impedance': 50,
    },
    'output_noise': {
        'enabled': False,
        'percent': 0,
    },
    'standard_waveform': {
        'waveform': 'square',
        'frequency': 220000,
        'amplitude': 1,
        'dc_offset': 0,
        'duty_cycle_high': 50,
        'start_phase': 0,
        'pulse_width': 1e-06,
        'symmetry': 50,
    },
}


class Transformer(object):
    """transforms instructions from the server to instrument commands

    The Transformer will request a instrument instance based on the
    instrument_type given in the configuration and passes the parameters
    to the instrument. After the run, the Transformer reads back the data
    from the instrument to package up for a Transmitter to tranmit to
    the server."""

    def __init__(self, command, instr=None, session=None):
        self.setup = command  # setup attribute to be deprecated
        self.test_run = command  # to be deprecated
        self.command = command
        self.instr = instr
        self.session = session
        self.dec_factor = 1
        self.test_run_id = None
        self.trace_dict = {}

    def _write_trace_dict(self):
        filename = 'full-trace-%s.json' % self.test_run_id
        trace_file = os.path.join(TMPDIR, filename)
        with open(trace_file, 'w') as f:
            f.write(json.dumps(self.trace_dict))


class IviTransformer(Transformer):
    """transformer for ivi instruments"""

    def __init__(self, command, ivi_obj, session):
        Transformer.__init__(self, command, session=session)
        self.instr = ivi_obj
        self.instr._write("*CLS")
        self.channels = self.instr.channels


class ScopeTransformer(IviTransformer, IviScopeClient):
    """transformer for oscilloscopes"""

    def __init__(self, command, ivi_obj=None, session=None):
        IviTransformer.__init__(self, command, ivi_obj, session)
        self.trace_dict = {}
        self.test_run = command  # deprecating
        self.command = command
        self.channel_names = [c.name for c in self.channels]
        self.channel_list = self.channel_names[:4]
        self.ch_idx_dict = {
            'ch1': 0,
            'ch2': 1,
            'ch3': 2,
            'ch4': 3,
        }
        self.enabled_list = ['ch1']  # by default, only ch1 enabled
        self.set_adders = 0
        self.exception_count = 0
        self.screenshot_blob_key = ''
        self.instrument_info = collections.defaultdict(int)
        self.g1_measurement_results = collections.defaultdict(int)
        self._horizontal_divisions = 10
        self._vertical_divisions = 10
        dd = collections.defaultdict(str)
        self.ce_dict = collections.defaultdict(lambda: dd)
        self.config_scorecard = {
            'success': [],
            'failure': [],
            'errors': {
                'usb_timeouts': 0,
                'usb_resource_busy': 0,
            },
            'times': {
                'start_to_finish': 0,
                'load_config': 0,
                'fetch_waveform': 0,
                'fetch_measurements': 0,
            }
        }
        self.times = {
            'init': time.clock(),
            'load_config_start': 0,
            'load_config_end': 0,
            'fetch_measurements_start': 0,
            'fetch_measurements_end': 0,
            'complete': 0,
        }
        self.config = collections.defaultdict(lambda: {})
        if command['category'] == 'Capture':
            logger.debug("creating cloud capture transformer")
            self.hybrid = True
            self.config = 'hybrid'
        else:
            self.config.update(command['info'])
            logger.debug("creating user-configured transformer")
            self.hybrid = False
            try:
                if self.command['label'] == 'grl_test':
                    self.ce_dict.update(DEFAULT_TEK_CONFIG)
                elif self.command['category'] == 'Config':
                    ce = command['info']['config_excerpt']
                    self.ce_dict.update(ce)
                else:
                    self.ce_dict.update(command['info'])
            except Exception:
                logger.debug("Exception in loading Config Excerpt")
                logger.debug(traceback.format_exc())
        self.test_run_id = str(self.command['id'])

        base_meas = [
            {
                'ivi_name': 'rise_time',
                'display_name': 'Rise Time',
            },
            {
                'ivi_name': 'fall_time',
                'display_name': 'Fall Time',
            },
            {
                'ivi_name': 'frequency',
                'display_name': 'Frequency',
            },
            {
                'ivi_name': 'period',
                'display_name': 'Period',
            },
            {
                'ivi_name': 'voltage_rms',
                'display_name': 'Voltage RMS',
            },
            {
                'ivi_name': 'voltage_peak_to_peak',
                'display_name': 'Voltage Peak to Peak',
            },
            {
                'ivi_name': 'voltage_max',
                'display_name': 'Voltage Max',
            },
            {
                'ivi_name': 'voltage_min',
                'display_name': 'Voltage Min',
            },
            {
                'ivi_name': 'voltage_high',
                'display_name': 'Voltage High',
            },
            {
                'ivi_name': 'voltage_low',
                'display_name': 'Voltage Low',
            },
            {
                'ivi_name': 'voltage_average',
                'display_name': 'Voltage Average',
            },
            {
                'ivi_name': 'width_negative',
                'display_name': 'Width Negative',
            },
            {
                'ivi_name': 'width_positive',
                'display_name': 'Width Positive',
            },
            {
                'ivi_name': 'duty_cycle_negative',
                'display_name': 'Duty Cycle Negative',
            },
            {
                'ivi_name': 'duty_cycle_positive',
                'display_name': 'Duty Cycle Positive',
            },
            {
                'ivi_name': 'amplitude',
                'display_name': 'Amplititude',
            },
            {
                'ivi_name': 'voltage_cycle_rms',
                'display_name': 'Voltage Cycle RMS',
            },
        ]
        self.meas_list = []
        self.meas_list.extend(base_meas)
        if not cfg.getboolean('client', 'SIMULATED'):
            if self.command['info']['instrument_type'] == 'TektronixMSO5204B':
                specific_meas = [
                    {
                        'ivi_name': 'voltage_cycle_average',
                        'display_name': 'Voltage Cycle Average',
                    },
                    {
                        'ivi_name': 'overshoot_negative',
                        'display_name': 'Overshoot Negative',
                    },
                    {
                        'ivi_name': 'overshoot_positive',
                        'display_name': 'Overshoot Positive',
                    },
                ]
                self.meas_list.extend(specific_meas)

            elif self.command['info']['instrument_type'] == 'RigolMSO2302A':
                self.meas_list.append({
                    'ivi_name': 'overshoot',
                    'display_name': 'Overshoot'
                })
        self.test_plan = False
        self.acq_dict = {
            'time_per_record': '',
            'number_of_points_minimum': '',
            'type': '',
            'start_time': '',
            'number_of_averages': '',
            'number_of_envelopes': '',
            'record_length': '',
        }
        try:
            self.trace_dict['more_options'] = None
        except Exception:
            logger.debug("more more_options exception")

        if cfg.getboolean('client', 'SIMULATED'):
            self.ce_dict['enabled_list'] = self.enabled_list
        self.instrument_info['channels'] = []
        if self.ce_dict['channels']:
            for ch in self.ce_dict['channels']:
                self.ce_dict[ch] = self.ce_dict['channels'][ch]
        logger.debug("ce_dict after init: %s" % self.ce_dict)
        try:
            logger.debug("trying to get channels object")
            self.channels = self.instr.channels
        except Exception:
            logger.debug("EXCEPTION: unabled to get channels obj", trace=True)
            self.channels = None
        self.logger = gateway_helpers.logger
        self.first_slice = None
        self.time_step = None
        self.waveform_length = 0
        self.slice_length = 0
        self.trace_dict['channels'] = []

    def set_timebase(self, timebase_dict):
        for key in timebase_dict:
            self.set_adders += 1
            self._setinstr_with_tries(self.instr.timebase, key,
                                      timebase_dict[key], label='timebase_',
                                      tries=3)

    def load_config(self):
        logger.debug("loading config")
        self.times['load_config_start'] = time.clock()
        if 'info' in self.config and self.config['info'] is not None:
            if 'raw_setup' in self.config['info']:
                self.load_raw_setup()
                time.sleep(1)

        # self.instr._interface.timeout = 100000
        if 'acquisition' in self.ce_dict:
            self._set_acquisition(self.ce_dict['acquisition'])
        if 'trigger' in self.ce_dict:
            self.set_trigger(self.ce_dict['trigger'])
        self.set_channels()
        if 'timebase' in self.ce_dict:
            self.set_timebase(self.ce_dict['timebase'])
        try:
            afg_enabled = self.ce_dict['outputs']['enabled']
            logger.debug("afg_enabled is: %s" % afg_enabled)
        except Exception:
            logger.debug("afg_enabled exception, setting False")
            afg_enabled = False
        if afg_enabled:
            try:
                self.set_outputs(self.ce_dict['outputs'])
                self.set_standard_waveform(self.ce_dict['standard_waveform'])
            except:
                logging.warning("AFG Enabled, but exception setting output")
        self.times['load_config_end'] = time.clock()
        return True

    def check_any_channel_enabled(self):
        """Checks if any channel is enabled. If none, return False

        Also updates the gateway info on the server.
        """
        channels_enabled = []
        for ch in self.channel_list:
            if self.instr.channels[self.ch_idx_dict[ch]].enabled:
                channels_enabled.append(ch)
        data = {
            'name': HARDWARENAME,
            'company': COMPANYNAME,
        }
        if channels_enabled:
            data['state'] = "Channels enabled %s" % channels_enabled
            instrument_info = {
                'channels_enabled': channels_enabled
            }
            instrument_type = self.command['info']['instrument_type']
            data['instruments'] = {instrument_type: instrument_info}
            self.put(BASE_URL + '/gateway', data=json.dumps(data))
            return True
        else:
            # if none enabled
            data['state'] = 'No Channels Enabled'
            self.put(BASE_URL + '/gateway', data=json.dumps(data))
            return False

    def _set_acquisition(self, acq_dict):
        if 'record_length' in acq_dict:
            del acq_dict['record_length']
        logger.debug("setting acquisition: " + str(acq_dict))
        try:
            if acq_dict['type'] == 'average':
                acq_dict['number_of_averages'] = int(
                    acq_dict['number_of_averages'])
            else:
                if 'number_of_averages' in acq_dict:
                    del acq_dict['number_of_averages']
            if acq_dict['type'] == 'envelope':
                acq_dict['number_of_envelopes'] = int(
                    acq_dict['number_of_envelopes'])
            else:
                if 'number_of_envelopes' in acq_dict:
                    del acq_dict['number_of_envelopes']
            if acq_dict['number_of_points_minimum']:
                acq_dict['number_of_points_minimum'] = int(
                    acq_dict['number_of_points_minimum'])
        except Exception:
            logger.debug(traceback.format_exc())

        for key in acq_dict:
            self.set_adders += 1
            self._setinstr_with_tries(self.instr.acquisition, key,
                                      acq_dict[key], label='acquisition_',
                                      tries=3)

    def set_trigger(self, trigger_dict):
        logger.debug("setting trigger")
        trigger = self.instr.trigger
        for key in trigger_dict:
            self._setinstr(trigger, key, trigger_dict[key], label='trigger_')

        if trigger_dict['type'] == 'edge':
            try:
                value = self.ce_dict['trigger_edge_slope']
                trigger.edge.slope = value
                self.config_scorecard['success'].append('trigger_edge_slope')
            except Exception:
                logger.debug("failed to set edge slope with %s" % value)
                self.config_scorecard['failure'].append('trigger_edge_slope')

    def set_standard_waveform(self, waveform_dict, index=0):
        logger.debug("set standard_waveform")
        standard_waveform = self.instr.outputs[index].standard_waveform
        if not standard_waveform:
            logger.debug("no standard_waveform to set")
            logger.debug("outputs[0] dir: %s" % dir(self.instr.outputs[0]))
            return False

        for key in waveform_dict:
            self._setinstr(standard_waveform, key, waveform_dict[key],
                           label='standard_waveform_')
        return True

    def set_outputs(self, output_dict, index=0):
        logger.debug("set outputs")
        output = self.instr.outputs[index]
        for key in output_dict:
            self._setinstr(output, key, output_dict[key], label='output_')
        try:
            output.noise.enabled = self.ce_dict['output_noise']['enabled']
            if output.noise.enabled:
                output.noise.percent = int(
                    self.ce_dict['output_noise']['percent'])
        except Exception:
            logger.debug("failed to set output noise")
            logger.debug(traceback.format_exc())

    def set_channels(self):
        logger.debug("[DEBUG] set channels with ce_dict:%s" % self.ce_dict)
        if not self.channels:
            self.channels = self.instr.channels
        for ch in self.channel_list:
            try:
                logger.debug("%s enabled: %s" %
                             (ch, self.ce_dict[ch]['channel_enabled']))
                en = self.ce_dict[ch]['channel_enabled']
                self.channels[self.ch_idx_dict[ch]].enabled = en
            except Exception:
                logger.debug("exception in setting channel enabled")
            if self.channels[self.ch_idx_dict[ch]].enabled:
                self._set_channel_settings(self.channels, ch)

    def _set_channel_settings(self, channels, ch):
        channel_settings = ['offset', 'range', 'coupling', 'input_impedance']
        for setting in channel_settings:
            if setting not in self.ce_dict[ch]:
                continue
            value = self.ce_dict[ch]['channel_' + setting]
            self._setinstr(channels[self.ch_idx_dict[ch]],
                           setting,
                           value,
                           label='channel_',
                           )

    def _set_enabled_list(self):
        self.enabled_list = []  # resets enabled list
        if cfg.getboolean('client', 'SIMULATED'):
            self.enabled_list = ['ch1']
            return
        for ch in self.channel_list:
            if self.instr.channels[self.ch_idx_dict[ch]].enabled:
                self.enabled_list.append(ch)
        for ch in self.enabled_list:
            if self.config == 'hybrid':
                self.ce_dict[ch] = collections.defaultdict(int)
                self.ce_dict[ch]['channel_enabled'] = True
            elif not self.ce_dict[ch]['channel_enabled']:
                self.enabled_list.remove(ch)

    def check_commands_completed(self):
        r = self.instr._ask("*ESR?")
        self.logger.debug("*ESR response: %s" % r)
        # r = self.instr._ask("allev?")
        # self.logger.info("allev? response: %s" % r)

    def fetch_measurements(self):
        """Fetches trace, metadata, screenshot, and measurements"""
        logger.debug("fetching measurements")
        self.times['fetch_measurements_start'] = time.clock()
        self._set_enabled_list()
        self.time_step = 0.000001
        self.slice_dict = collections.defaultdict(int)
        self.first_slice = collections.defaultdict(int)
        self.trace_dict['start_tse'] = int(dt2ms(datetime.datetime.now()))
        logger.debug("enabled_list: %s" % self.enabled_list)
        meas_dict = {}
        index = 0
        # Fetch the waveform for each channel enabled
        for ch in self.enabled_list:
            self._fetch_waveform(ch, index, meas_dict)
            index += 1
        # Write the dictionary of trace data
        self._write_trace_dict()
        # Make quick post for first feedback
        self._quick_post_results()
        # Grab a screenshot from the instrument
        self._grab_and_post_screenshot()
        index = 0
        # Run measurments on each channel
        for ch in self.enabled_list:
            self._fetch_waveform_measurements(ch, meas_dict)
            index += 1
        self.times['fetch_measurements_end'] = time.clock()
        return meas_dict

    def _fetch_waveform(self, ch, index, meas_dict):
        self.check_commands_completed()
        voltage_list = None
        start_time = 0
        end_time = 0
        self.trace_dict['channels'].append({})
        try:
            if cfg.getboolean('client', 'SIMULATED'):
                self.ce_dict[ch]['channel_enabled'] = True
            logger.debug("%s channel_enabled: %s" %
                         (ch, self.ce_dict[ch]['channel_enabled']))
            if self.ce_dict[ch]['channel_enabled']:
                channel = self.instr.channels[self.ch_idx_dict[ch]]
                waveform = list(channel.measurement.fetch_waveform())
                logger.debug("waveform length for %s: %s" %
                             (ch, len(waveform)))
                self.waveform_length = len(waveform)
                start_time = waveform[0][0]
                end_time = waveform[-1][0]
                time_step = waveform[1][0] - start_time
                voltage_list = self.get_voltage_list(waveform)
                slice_list = self.get_slice_list(voltage_list)
                self.slice_dict[ch] = slice_list
                self.first_slice[ch] = slice_list[0]
                self.check_commands_completed()
            meas_dict[ch] = collections.defaultdict(str)
            self.trace_dict[ch + '_voltages'] = voltage_list
            self.trace_dict[ch + '_start_time'] = start_time
            self.trace_dict[ch + '_end_time'] = end_time
            self.trace_dict['name'] = ch
            self.trace_dict['channels'][-1]['results'] = voltage_list
            self.trace_dict['channels'][-1]['time_step'] = time_step
            self.time_step = time_step  # migrate towards ch specific
        except Exception:
            self.logger.warning("failed to fetch waveform for: %s"
                                % ch, exc_info=True)

    def _fetch_waveform_measurements(self, ch_str, meas_dict):
        self.check_commands_completed()
        logger.debug("fetching waveform measurements")
        if not self.channels:
            channel = self.instr.channels[ch_str]
        else:
            channel = self.instr.channels[self.ch_idx_dict[ch_str]]
        meas_dict[ch_str]['valid'] = True
        for meas in self.meas_list:
            # Skip is simulated (meas_list should be empty anyway)
            if cfg.getboolean('client', 'SIMULATED'):
                continue
            m_val = ''
            measurement = channel.measurement
            try:
                ivi_name = meas['ivi_name']
                m_val = measurement.fetch_waveform_measurement(ivi_name)
                self.check_commands_completed()
                meas_dict[ch_str][ivi_name] = m_val
                if m_val > MAX_VALID_MEAS_VAL:
                    meas_dict[ch_str]['valid'] = False
                else:
                    m_val = MAX_VALID_MEAS_VAL
                meas_dict[ch_str][ivi_name] = m_val
                meas['value'] = MAX_VALID_MEAS_VAL
            except Exception:
                logger.debug(ch_str + " measurement exception")
                logger.debug(traceback.format_exc())
        meas_dict[ch_str]['waveform_measurements'] = list(self.meas_list)

    def get_trigger(self):
        logger.debug("getting trigger")
        trigger_dict = {
            'type': '',
            'coupling': '',
            'source': '',
            'level': '',
        }
        for name in trigger_dict:
            trigger_dict[name] = getattr(self.instr.trigger, name)
        self.ce_dict['trigger_edge_slope'] = self.instr.trigger.edge.slope
        return trigger_dict

    def get_acquisition(self):
        logger.debug("getting acquisition")
        for key in self.acq_dict:
            self.acq_dict[key] = getattr(self.instr.acquisition, key)
        return self.acq_dict

    def get_standard_waveform(self, index=0):
        logger.debug("getting standard_waveform")
        standard_waveform = self.instr.outputs[index].standard_waveform
        std_wave_dict = {
            'waveform': '',
            'frequency': '',
            'amplitude': '',
            'dc_offset': '',
            'duty_cycle_high': '',
            'start_phase': '',
            'pulse_width': '',
            'symmetry': '',
        }
        if standard_waveform:
            for key in std_wave_dict:
                std_wave_dict[key] = getattr(standard_waveform, key)
        else:
            logger.debug("no standard_waveform object")
            logger.debug("outputs[0] dir: %s" % dir(self.instr.outputs[0]))

    def get_outputs(self, index=0):
        logger.debug("getting outputs")
        outputs = None
        try:
            outputs = self.instr.outputs[index]
        except Exception:
            logger.debug("getting outputs exception")
        output_dict = {
            'impedance': '',
            'enabled': '',
        }
        if not outputs:
            return output_dict

        for key in output_dict:
            output_dict[key] = getattr(outputs, key)
            logger.debug("output from instr: %s %s" % (key, output_dict[key]))
        output_dict['standard_waveform'] = self.get_standard_waveform()
        self.ce_dict['outputs_noise_percent'] = outputs.noise.percent
        return output_dict

    def _get_excerpt_channel_data(self):
        """updates config exerpt to match instrument reported channel enabled,
           offset, range, and coupling. Updates enabled list to match
           instrument reported enabled channels. Returns copy of updated
           config excerpt"""
        logger.debug("updating config_excerpt, requesting channels")
        if not self.channels:
            self.channels = self.instr.channels
        config_excerpt = copy.deepcopy(self.ce_dict)
        self.enabled_list = []
        for ch in self.channel_list:
            ch_dict = collections.defaultdict(str)
            logger.debug("requesting channel enabled data for %s" % ch)
            ch_dict['channel_enabled'] = self.channels[
                self.ch_idx_dict[ch]].enabled
            time.sleep(0.25)
            if ch_dict['channel_enabled']:
                logger.debug("response %s enabled" % ch)
                ch_dict['channel_offset'] = self.channels[
                    self.ch_idx_dict[ch]].offset
                time.sleep(0.25)
                ch_dict['channel_range'] = self.channels[
                    self.ch_idx_dict[ch]].range
                time.sleep(0.25)
                ch_dict['channel_coupling'] = self.channels[
                    self.ch_idx_dict[ch]].coupling
                time.sleep(0.25)
                cii = self.channels[self.ch_idx_dict[ch]].input_impedance
                time.sleep(0.25)
                ch_dict['channel_input_impedance'] = cii
                self.enabled_list.append(ch)
            else:
                logger.debug("response: %s NOT enabled" % ch)
            config_excerpt[ch] = ch_dict
        # sync up excerpt list with transformer list
        self.ce_dict['enabled_list'] = self.enabled_list
        config_excerpt['enabled_list'] = self.enabled_list
        return config_excerpt

    def get_config_excerpt(self):
        logger.debug("Pre getconfig outputs: %s" %
                     self.ce_dict['outputs'])
        if cfg.getboolean('client', 'SIMULATED'):
            return DEFAULT_TEK_CONFIG
        logger.debug("getting config_excerpt")
        config_excerpt = self._get_excerpt_channel_data()
        config_excerpt['trigger'] = self.get_trigger()
        config_excerpt['acquisition'] = self.get_acquisition()
        config_excerpt['outputs'] = self.get_outputs()
        config_excerpt['timebase'] = self.get_timebase()

        return config_excerpt

    def get_timebase(self):
        timebase = collections.defaultdict(int)
        try:
            timebase['position'] = self.instr.timebase.position
        except Exception:
            logger.debug("get timebase position exception")
        return timebase

    def get_probe_ids(self, total_channels=2):
        logger.debug("getting probe_ids")
        probe_ids = []
        if not self.channels:
            self.channels = self.instr.channels
        for i in range(total_channels):
            probe_ids.append(self.channels[i].probe_id)
        return probe_ids

    def get_voltage_list(self, waveform):
        logger.debug("getting voltage_list")
        voltage_list = [round_sig(float(point[1])) for point in waveform]
        return voltage_list

    def get_slice_list(self, voltage_list):
        """create list of slices sets class attribute"""
        logger.debug("getting slice_list")
        if len(voltage_list) >= int(CLIENT_SETTINGS["MAX_LENGTH_FOR_BROWSER"]):
            slice_list = [voltage_list[x:x + int(CLIENT_SETTINGS["MAX_LENGTH_FOR_BROWSER"])]  # nopep8
                          for x in range(0, len(voltage_list), int(CLIENT_SETTINGS["MAX_LENGTH_FOR_BROWSER"]))]  # nopep8
        else:
            slice_list = [voltage_list]
        return slice_list

    def _grab_and_post_screenshot(self):
        if cfg.getboolean('client', 'SIMULATED'):
            return
        png = self.instr.display.fetch_screenshot()
        self.logger.info("_grab_and_post_screenshot")
        filename = "screenshot-" + str(self.test_run_id)
        pngfile = os.path.join(TMPDIR, 'tempfile.png')
        with open(pngfile, 'w') as f:
            f.write(png)
        response = self.gzip_and_post_file(pngfile, file_key=filename)
        self.screenshot_blob_key = response.text
        self.trace_dict['screenshot_blob_key'] = response.text

    def _quick_post_results(self):
        """Gives the quick feedback to the server for UI feedback

        Also calls _post_summary_waveform() for the overall data
        """
        if self.hybrid:
            config_name = str(self.test_run_id)
        else:
            config_name = self.config['name']
        self._set_divisions()
        if self.slice_dict:
            slice_list_len = len(self.slice_dict.itervalues().next())
        else:
            slice_list_len = 0
        cid = self.test_run_id
        url = BASE_URL + '/results/%s/slices/metadata' % cid
        r = self.post(url, data=json.dumps({'num_of_slices': slice_list_len}))
        logger.info("metadata post response %s" % r.text)
        quick_results = {
            'test_results': self.first_slice,
            'num_of_slices': slice_list_len,
            'time_step': self.time_step,
            'test_plan': self.test_plan,
            'config_name': config_name,
            'screenshot_blob_key': self.screenshot_blob_key,
            'instrument_info': self.get_instrument_info(),
            'total_points': self.waveform_length,
            'slice_length': len(self.first_slice),
        }
        url_t = BASE_URL + "/results/" + str(self.test_run_id) + "/quickdata"
        headers = {'Content-Type': 'application/json', 'Accept': 'text/plain'}
        json_data = json.dumps(quick_results, ensure_ascii=True)
        response = self.session.post(url_t, data=json_data, headers=headers)
        self.logger.info("_quick_post_results response.status_code: %s"
                         % response.status_code)
        self._post_summary_waveform()

    def _set_divisions(self, h_divs=0, v_divs=0):
        if self.instr._horizontal_divisions:
            self._horizontal_divisions = self.instr._horizontal_divisions
        else:
            self._horizontal_divisions = 10
        if self.instr._vertical_divisions:
            self._vertical_divisions = self.instr._vertical_divisions
        else:
            self._vertical_divisions = 8
        if h_divs:
            self._horizontal_divisions = h_divs
        if v_divs:
            self._vertical_divisions = v_divs
        self.trace_dict['h_divs'] = self._horizontal_divisions
        self.trace_dict['v_divs'] = self._vertical_divisions

    def get_horizontal_divisions(self):
        if self._horizontal_divisions:
            return self._horizontal_divisions
        else:
            self._set_divisions()
            return self._horizontal_divisions

    def get_vertical_divisions(self):
        if self._vertical_divisions:
            return self._vertical_divisions
        else:
            self._set_divisions()
            return self._vertical_divisions

    def get_instrument_info(self):
        instr_info = {'channels': []}
        instr_info['h_divs'] = self.get_horizontal_divisions()
        instr_info['v_divs'] = self.get_vertical_divisions()
        instr_info['timebase_range'] = self.instr.timebase.range
        instr_info['timebase_position'] = self.instr.timebase.position
        instr_info['timebase_scale'] = self.instr.timebase.scale
        if not self.channels:
            self.channels = self.instr.channels
        ch_counter = 0
        for ch in self.enabled_list:
            channel_info = {}
            try:
                channel_info['trigger_level'] = self.channels[
                    self.ch_idx_dict[ch]].trigger_level
            except Exception:
                post_log("exception in getting trigger_level...%s"
                         % traceback.format_exc())
            try:
                channel_info['name'] = ch
                channel_info['range'] = self.channels[
                    self.ch_idx_dict[ch]].range
                channel_info['coupling'] = self.channels[
                    self.ch_idx_dict[ch]].coupling
                channel_info['offset'] = self.channels[
                    self.ch_idx_dict[ch]].offset
                channel_info['scale'] = self.channels[
                    self.ch_idx_dict[ch]].scale
            except Exception:
                post_log("exception with range, coupling, or offset...%s"
                         % traceback.format_exc())
            instr_info['channels'].append(channel_info)
            ch_counter += 1
        # update current objects's info
        self.instrument_info.update(instr_info)
        return instr_info

    def post_status_update(self, status):
        status_url = ('https://' + COMMON_SETTINGS["DOMAIN"] + '/status/' +
                      COMMON_SETTINGS['COMPANYNAME'] + '/' +
                      COMMON_SETTINGS['HARDWARENAME'])
        self.session.post(status_url, status)

    def handle_usb_error(self, e):
        if e.args == ('Operation timed out',):
            logger.debug("Found USBError: Operation timed out")
            self.config_scorecard['errors']['usb_timeouts'] += 1
        elif e.args == ('Resource busy',):
            logger.debug('Found USBError: Resource busy')
            self.post_status_update(self.session, "Critical USBError")
            self.config_scorecard['errors']['usb_resource_busy'] += 1
        else:
            logger.debug('Unknown USBError')

    def update_scorecard_times(self):
        times = self.times
        stf = times['complete'] - times['init']
        lc = times['load_config_end'] - times['load_config_start']
        fm = times['fetch_measurements_end'] - \
            times['fetch_measurements_start']
        config_times = {
            'start_to_finish': stf,
            'load_config': lc,
            'fetch_measurements': fm,
        }
        self.config_scorecard['times'] = config_times


class TransformerMSO5204B(ScopeTransformer):

    def __init__(self, setup, ivi_obj, session):
        ScopeTransformer.__init__(self, setup, ivi_obj, session)
        self.channel_list = self.channel_names[:4]  # assigns first 4 channels
        self.acq_dict = {
            'time_per_record': '',
            'number_of_points_minimum': '',
            'type': '',
            'start_time': '',
            'number_of_averages': '',
            'number_of_envelopes': '',
            'record_length': '',
            'sample_rate': '',
        }

    def load_config(self):
        logger.debug("loading config")
        self.times['load_config_start'] = time.clock()
        if self.config['hybrid_config']:
            self.load_raw_setup()
            time.sleep(1)

        if 'horizontal' in self.ce_dict:
            self._set_horizontal(
                self.ce_dict['horizontal'], self.ce_dict['acquisition'])
        if 'acquisition' in self.ce_dict:
            self._set_acquisition(
                self.ce_dict['acquisition'], self.ce_dict['horizontal'])
        if 'trigger' in self.ce_dict:
            self.set_trigger(self.ce_dict['trigger'])
        self.set_channels()
        logger.info('the dict', self.ce_dict)
        if 'timebase' in self.ce_dict:
            logger.info("setting timebase")
            self.set_timebase(self.ce_dict['timebase'])

        try:
            afg_enabled = self.ce_dict['outputs']['enabled']
            logger.debug("afg_enabled is: %s" % afg_enabled)
        except Exception:
            logger.debug("afg_enabled exception, setting False")
            afg_enabled = False
        if afg_enabled:
            try:
                self.set_outputs(self.ce_dict['outputs'])
                self.set_standard_waveform(self.ce_dict['standard_waveform'])
            except:
                logging.warning("AFG Enabled, but exception setting output")
        self.times['load_config_end'] = time.clock()
        return True

    def _set_acquisition(self, acq_dict, horiz_dict):
        if 'record_length' in acq_dict:
            del acq_dict['record_length']
        logger.debug("setting acquisition: " + str(acq_dict))
        try:
            if acq_dict['type'] == 'average':
                acq_dict['number_of_averages'] = int(
                    acq_dict['number_of_averages'])
            else:
                if 'number_of_averages' in acq_dict:
                    del acq_dict['number_of_averages']
            if acq_dict['type'] == 'envelope':
                acq_dict['number_of_envelopes'] = int(
                    acq_dict['number_of_envelopes'])
            else:
                if 'number_of_envelopes' in acq_dict:
                    del acq_dict['number_of_envelopes']
            if acq_dict['number_of_points_minimum']:
                acq_dict['number_of_points_minimum'] = int(
                    acq_dict['number_of_points_minimum'])
                del acq_dict['number_of_points_minimum']
            if horiz_dict['sample_rate']:
                acq_dict['sample_rate'] = self._sample_rate_lookup(
                    horiz_dict['sample_rate'])

        except Exception:
            logger.debug(traceback.format_exc())

        for key in acq_dict:
            self.set_adders += 1

            self._setinstr_with_tries(self.instr.acquisition, key,
                                      acq_dict[key], label='acquisition_',
                                      tries=3)
            if key == 'number_of_points_minimum':
                pass
            else:
                self._setinstr_with_tries(self.instr.acquisition, key,
                                          acq_dict[key], label='acquisition_',
                                          tries=3)

    def get_config_excerpt(self):
        logger.debug("Pre getconfig outputs: %s" %
                     self.ce_dict['outputs'])
        if cfg.getboolean('client', 'SIMULATED'):
            return DEFAULT_TEK_CONFIG
        logger.debug("getting config_excerpt")
        config_excerpt = self._get_excerpt_channel_data()
        config_excerpt['trigger'] = self.get_trigger()
        config_excerpt['acquisition'] = self.get_acquisition()
        config_excerpt['outputs'] = self.get_outputs()
        config_excerpt['timebase'] = self.get_timebase()
        return config_excerpt

    def get_timebase(self):
        timebase = collections.defaultdict(int)
        try:
            timebase['position'] = self.instr.timebase.position
        except Exception:
            logger.debug("get timebase position exception")
        try:
            timebase['scale'] = self.instr.timebase.scale
        except Exception:
            logger.debug("get timebase scaleexception")
        return timebase

    # def set_timebase(self, timebase_dict, horiz_dict):

    #     try:
    #         if horiz_dict['scale']:
    #             timebase_dict['scale'] = self._scale_lookup(horiz_dict['scale'])  # noqa
    #     except Exception:
    #         logger.debug(traceback.format_exc())
    #     for key in timebase_dict:
    #         self.set_adders += 1
    #         self._setinstr_with_tries(self.instr.timebase, key,
    #                                   timebase_dict[key], label='timebase_',
    #                                   tries=3)

    def _sample_rate_lookup(self, value):
        sample_rate_table = {"400GS/s": 400e9,
                             "200GS/s": 200e9,
                             "80GS/s": 80e9,
                             "40GS/s": 40e9,
                             "20GS/s": 20e9,
                             "10GS/s": 10e9,
                             "5GS/s": 5e9,
                             "2.5GS/s": 2.5e9,
                             "1GS/s": 1e9,
                             "500MS/s": 500e6,
                             "200MS/s": 200e6,
                             "100MS/s": 100e6,
                             "50MS/s": 50e6,
                             "20MS/s": 20e6,
                             "10MS/s": 10e6,
                             "5MS/s": 5e6,
                             "2MS/s": 2e6,
                             "1MS/s": 1e6,
                             "500Ks/s": 500000,
                             "200Ks/s": 200000,
                             "100Ks/s": 100000,
                             "50Ks/s": 50000,
                             "20Ks/s": 20000,
                             "10Ks/s": 10000,
                             "5kS/s": 5000,
                             "2kS/s": 2000,
                             "1kS/s": 1000,
                             "500S/s": 500,
                             "200S/s": 200,
                             "100S/s": 100,
                             "50S/s": 50,
                             "20S/s": 20,
                             "10S/s": 10,
                             "5S/s": 5}
        sample_rate = sample_rate_table[value]
        logger.info('value = ', value, 'sample_rate = ', sample_rate)
        return sample_rate

    def _scale_lookup(self, value):
        value = value[0]
        scale_table = {"1ks": 1000,
                       "500s": 500,
                       "200s": 200,
                       "100s": 100,
                       "50s": 50,
                       "20s": 20,
                       "10s": 10,
                       "5s": 5,
                       "2s": 2,
                       "1s": 1,
                       "500ms": 0.5,
                       "200ms": 0.2,
                       "100ms": 0.1,
                       "50ms": 0.05,
                       "20ms": 0.02,
                       "10ms": 0.01,
                       "5ms": 0.005,
                       "2ms": 0.002,
                       "1ms": 0.001,
                       "500us": 5e-4,
                       "200us": 2e-4,
                       "100us": 1e-4,
                       "50us": 5e-5,
                       "20us": 2e-5,
                       "10us": 1e-5,
                       "5us": 5e-6,
                       "2us": 2e-6,
                       "1us":   1e-6,
                       "500ns": 5e-7,
                       "200ns": 2e-7,
                       "100ns": 1e-7,
                       "50ns":  5e-8,
                       "20ns":  2e-8,
                       "10ns":  1e-8,
                       "5ns":   5e-9,
                       "2.5ns": 2.5e-9,
                       "1ns":   1e-9,
                       "500ps": 5e-10,
                       "250ps": 2.5e-10}
        scale = scale_table[value]
        return scale


class TransformerMDO3012(ScopeTransformer):

    def __init__(self, setup, ivi_obj, session):
        ScopeTransformer.__init__(self, setup, ivi_obj, session)
        self.channel_list = self.channel_names[:2]

    def _set_divisions(self, v_divs=8, h_divs=10):
        self._vertical_divisions = v_divs
        self._horizontal_divisions = h_divs


class TransformerMSO2302A(ScopeTransformer):

    def __init__(self, setup, ivi_obj, session):
        ScopeTransformer.__init__(self, setup, ivi_obj, session)
        self.channel_list = self.channel_names[:2]
        self.ch_idx_dict = {
            'chan1': 0,
            'chan2': 1,
            'chan3': 2,
            'chan4': 3,
        }
        self.acq_dict = {
            'time_per_record': '',
            'number_of_points_minimum': '',
            'type': '',
            'start_time': '',
            'number_of_averages': '',
            'record_length': '',
        }
        self.dec_factor = 1

    def get_outputs(self, index=0):
        pass

    def _set_channel_settings(self, channels, ch):
        channel_settings = ['offset', 'range', 'coupling', 'input_impedance']
        for setting in channel_settings:
            if setting not in self.ce_dict[ch]:
                continue
            value = self.ce_dict[ch]['chan' + setting]
            self._setinstr(channels[self.ch_idx_dict[ch]],
                           setting,
                           value,
                           label='chan',
                           )

    def _get_excerpt_channel_data(self):
        """updates config exerpt to match instrument reported channel enabled,
           offset, range, and coupling. Updates enabled list to match
           instrument reported enabled channels. Returns copy of updated
           config excerpt"""
        logger.debug("updating config_excerpt, requesting channels")
        if not self.channels:
            self.channels = self.instr.channels
        config_excerpt = copy.deepcopy(self.ce_dict)
        self.enabled_list = []
        for ch in self.channel_list:
            if ch == "chan1" or ch == "chan2":
                ch_dict = collections.defaultdict(str)
                logger.debug("requesting channel enabled data for %s" % ch)
                ch_dict['channel_enabled'] = self.channels[
                    self.ch_idx_dict[ch]].enabled
                time.sleep(0.25)
                if ch_dict['channel_enabled']:
                    logger.debug("response %s enabled" % ch)
                    ch_dict['channel_offset'] = self.channels[
                        self.ch_idx_dict[ch]].offset
                    time.sleep(0.25)
                    ch_dict['channel_range'] = self.channels[
                        self.ch_idx_dict[ch]].range
                    time.sleep(0.25)
                    ch_dict['channel_coupling'] = self.channels[
                        self.ch_idx_dict[ch]].coupling
                    time.sleep(0.25)
                    cii = self.channels[self.ch_idx_dict[ch]].input_impedance
                    time.sleep(0.25)
                    ch_dict['channel_input_impedance'] = cii
                    self.enabled_list.append(ch)
                else:
                    logger.debug("response: %s NOT enabled" % ch)
                config_excerpt[ch] = ch_dict
        # sync up excerpt list with transformer list
        self.ce_dict['enabled_list'] = self.enabled_list
        config_excerpt['enabled_list'] = self.enabled_list
        return config_excerpt

    def get_instrument_info(self):
        instr_info = {'channels': []}
        instr_info['h_divs'] = self.get_horizontal_divisions()
        instr_info['v_divs'] = self.get_vertical_divisions()
        instr_info['timebase_range'] = self.instr.timebase.range
        instr_info['timebase_position'] = self.instr.timebase.position
        instr_info['timebase_scale'] = self.instr.timebase.scale
        if not self.channels:
            self.channels = self.instr.channels
        ch_counter = 0
        for ch in self.enabled_list:
            channel_info = {}
            try:
                channel_info['trigger_level'] = self.instr.trigger.level
            except Exception:
                post_log("exception in getting trigger_level...%s"
                         % traceback.format_exc())
            try:
                channel_info['name'] = ch
                channel_info['range'] = self.channels[
                    self.ch_idx_dict[ch]].range
                channel_info['coupling'] = self.channels[
                    self.ch_idx_dict[ch]].coupling
                channel_info['offset'] = self.channels[
                    self.ch_idx_dict[ch]].offset
                channel_info['scale'] = self.channels[
                    self.ch_idx_dict[ch]].scale
            except Exception:
                post_log("exception with range, coupling, or offset...%s"
                         % traceback.format_exc())
            instr_info['channels'].append(channel_info)
            ch_counter += 1
        # update current objects's info
        self.instrument_info.update(instr_info)
        return instr_info

    def fetch_raw_setup(self, last_try=False):
        raw_setup = super(TransformerMSO2302A, self).fetch_raw_setup()
        return raw_setup.encode('hex')

    def _fetch_waveform(self, ch, index, meas_dict):
        self.instr._write(":WAVeform:MODE RAW")
        super(TransformerMSO2302A, self)._fetch_waveform(ch, index, meas_dict)


class TransformerMSO2024(ScopeTransformer):
    """overrides get_config_excerpt to skip outputs"""

    def get_config_excerpt(self):
        config_excerpt = self._get_excerpt_channel_data()
        config_excerpt['trigger'] = self.get_trigger()
        config_excerpt['acquisition'] = self.get_acquisition()
        return config_excerpt

    def _set_divisions(self, v_divs=8, h_divs=10):
        self._vertical_divisions = v_divs
        self._horizontal_divisions = h_divs

    def _alt_get_acquisition(self):
        """Alternative to convert acq to valid values

           Use this if ivi starts returning weird values for
           acquisition again
        """
        logger.debug("getting acquisition")
        for key in self.acq_dict:
            value = getattr(self.instr.acquisition, key)
            if key == 'time_per_record':
                value = self._convert_special_acq(value)
            self.acq_dict[key] = value
        return self.acq_dict

    def _convert_special_acq(self, value):
        if value < 100000:
            return value
        elif value < 500000:
            value = 100000
        elif value < 5000000:
            value = 1000000
        elif value < 50000000:
            value = 10000000
        else:
            return value
