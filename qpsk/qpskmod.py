#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: irongiant
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from PyQt5 import QtCore
from gnuradio import blocks
import numpy
from gnuradio import channels
from gnuradio.filter import firdes
from gnuradio import digital
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import math
import sip



class qpskmod(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "qpskmod")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.qpsk = qpsk = digital.constellation_rect([0.707+0.707j, -0.707+0.707j, -0.707-0.707j, 0.707-0.707j], [0, 1, 3, 2],
        4, 2, 2, 1, 1).base()
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0 = digital.adaptive_algorithm_cma( qpsk, .0001, 4).base()
        self.sps = sps = 4
        self.samp_rate = samp_rate = 16000
        self.phase_offset = phase_offset = 1.0005
        self.noise = noise = 0.2
        self.freq_offset = freq_offset = 0.025
        self.excess_bw = excess_bw = 0.35

        ##################################################
        # Blocks
        ##################################################

        self._phase_offset_range = qtgui.Range(0.999, 1.001, 0.0001, 1.0005, 200)
        self._phase_offset_win = qtgui.RangeWidget(self._phase_offset_range, self.set_phase_offset, "'phase_offset'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._phase_offset_win)
        self._noise_range = qtgui.Range(0, 1, 0.01, 0.2, 200)
        self._noise_win = qtgui.RangeWidget(self._noise_range, self.set_noise, "'noise'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._noise_win)
        self._freq_offset_range = qtgui.Range(-0.1, 0.1, 0.001, 0.025, 200)
        self._freq_offset_win = qtgui.RangeWidget(self._freq_offset_range, self.set_freq_offset, "'freq_offset'", "counter_slider", float, QtCore.Qt.Horizontal)
        self.top_layout.addWidget(self._freq_offset_win)
        self.qtgui_const_sink_x_0 = qtgui.const_sink_c(
            1024, #size
            "", #name
            3, #number of inputs
            None # parent
        )
        self.qtgui_const_sink_x_0.set_update_time(0.10)
        self.qtgui_const_sink_x_0.set_y_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_x_axis((-2), 2)
        self.qtgui_const_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, "")
        self.qtgui_const_sink_x_0.enable_autoscale(False)
        self.qtgui_const_sink_x_0.enable_grid(False)
        self.qtgui_const_sink_x_0.enable_axis_labels(True)


        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        styles = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        markers = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(3):
            if len(labels[i]) == 0:
                self.qtgui_const_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_const_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_const_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_const_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_const_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_const_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_const_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_const_sink_x_0_win = sip.wrapinstance(self.qtgui_const_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_const_sink_x_0_win)
        self.fir_filter_xxx_0 = filter.fir_filter_ccc(1, firdes.root_raised_cosine(1.0,samp_rate,samp_rate/sps,excess_bw,11*sps))
        self.fir_filter_xxx_0.declare_sample_delay(0)
        self.digital_symbol_sync_xx_0 = digital.symbol_sync_cc(
            digital.TED_MUELLER_AND_MULLER,
            sps,
            ((2*math.pi)/100),
            1.0,
            1.0,
            1.5,
            2,
            digital.constellation_qpsk().base(),
            digital.IR_MMSE_8TAP,
            128,
            [])
        self.digital_linear_equalizer_0 = digital.linear_equalizer(15, int(sps), variable_adaptive_algorithm_0, True, [ ], 'corr_est')
        self.digital_costas_loop_cc_0 = digital.costas_loop_cc(((2*math.pi)/100), 4, False)
        self.digital_constellation_modulator_0_0_0 = digital.generic_mod(
            constellation=qpsk,
            differential=True,
            samples_per_symbol=4,
            pre_diff_code=True,
            excess_bw=excess_bw,
            verbose=False,
            log=False,
            truncate=False)
        self.channels_channel_model_0 = channels.channel_model(
            noise_voltage=noise,
            frequency_offset=freq_offset,
            epsilon=phase_offset,
            taps=[1.0],
            noise_seed=0,
            block_tags=False)
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.analog_random_source_x_0 = blocks.vector_source_b(list(map(int, numpy.random.randint(0, 256, 10000))), True)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_random_source_x_0, 0), (self.digital_constellation_modulator_0_0_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.channels_channel_model_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.fir_filter_xxx_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.qtgui_const_sink_x_0, 0))
        self.connect((self.channels_channel_model_0, 0), (self.digital_linear_equalizer_0, 0))
        self.connect((self.digital_constellation_modulator_0_0_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.digital_costas_loop_cc_0, 0), (self.qtgui_const_sink_x_0, 2))
        self.connect((self.digital_linear_equalizer_0, 0), (self.digital_symbol_sync_xx_0, 0))
        self.connect((self.digital_symbol_sync_xx_0, 0), (self.digital_costas_loop_cc_0, 0))
        self.connect((self.fir_filter_xxx_0, 0), (self.qtgui_const_sink_x_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "qpskmod")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_qpsk(self):
        return self.qpsk

    def set_qpsk(self, qpsk):
        self.qpsk = qpsk

    def get_variable_adaptive_algorithm_0(self):
        return self.variable_adaptive_algorithm_0

    def set_variable_adaptive_algorithm_0(self, variable_adaptive_algorithm_0):
        self.variable_adaptive_algorithm_0 = variable_adaptive_algorithm_0

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps
        self.digital_symbol_sync_xx_0.set_sps(self.sps)
        self.fir_filter_xxx_0.set_taps(firdes.root_raised_cosine(1.0,self.samp_rate,self.samp_rate/self.sps,self.excess_bw,11*self.sps))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)
        self.fir_filter_xxx_0.set_taps(firdes.root_raised_cosine(1.0,self.samp_rate,self.samp_rate/self.sps,self.excess_bw,11*self.sps))

    def get_phase_offset(self):
        return self.phase_offset

    def set_phase_offset(self, phase_offset):
        self.phase_offset = phase_offset
        self.channels_channel_model_0.set_timing_offset(self.phase_offset)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_freq_offset(self):
        return self.freq_offset

    def set_freq_offset(self, freq_offset):
        self.freq_offset = freq_offset
        self.channels_channel_model_0.set_frequency_offset(self.freq_offset)

    def get_excess_bw(self):
        return self.excess_bw

    def set_excess_bw(self, excess_bw):
        self.excess_bw = excess_bw
        self.fir_filter_xxx_0.set_taps(firdes.root_raised_cosine(1.0,self.samp_rate,self.samp_rate/self.sps,self.excess_bw,11*self.sps))




def main(top_block_cls=qpskmod, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
