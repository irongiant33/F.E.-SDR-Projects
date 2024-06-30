#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: irongiant
# GNU Radio version: 3.10.7.0

from packaging.version import Version as StrictVersion
from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import gr
from gnuradio.filter import firdes
from gnuradio.fft import window
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import zeromq
import math



class fskmod(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "fskmod")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.pulse_duration = pulse_duration = 100e-6
        self.time_window = time_window = pulse_duration * 10
        self.samp_rate = samp_rate = 8e6
        self.offset_freq = offset_freq = 2e6
        self.fsk_deviation_hz = fsk_deviation_hz = 100e3

        ##################################################
        # Blocks
        ##################################################

        self.zeromq_pub_sink_0 = zeromq.pub_sink(gr.sizeof_gr_complex, 1, 'tcp://127.0.0.1:4444', 100, False, (-1), '', True, True)
        self.blocks_vector_source_x_0 = blocks.vector_source_f((0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), True, 1, [])
        self.blocks_throttle2_0 = blocks.throttle( gr.sizeof_gr_complex*1, samp_rate, True, 0 if "auto" == "auto" else max( int(float(0.1) * samp_rate) if "auto" == "time" else int(0.1), 1) )
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_float*1, (int(pulse_duration * samp_rate) ))
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.analog_sig_source_x_0 = analog.sig_source_c(samp_rate, analog.GR_COS_WAVE, offset_freq, 1, 0, 0)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(((2 * math.pi * (fsk_deviation_hz / 2))/samp_rate))


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_sig_source_x_0, 0), (self.blocks_throttle2_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.zeromq_pub_sink_0, 0))
        self.connect((self.blocks_repeat_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.blocks_throttle2_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_repeat_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "fskmod")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_pulse_duration(self):
        return self.pulse_duration

    def set_pulse_duration(self, pulse_duration):
        self.pulse_duration = pulse_duration
        self.set_time_window(self.pulse_duration * 10)
        self.blocks_repeat_0.set_interpolation((int(self.pulse_duration * self.samp_rate) ))

    def get_time_window(self):
        return self.time_window

    def set_time_window(self, time_window):
        self.time_window = time_window

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.analog_frequency_modulator_fc_0.set_sensitivity(((2 * math.pi * (self.fsk_deviation_hz / 2))/self.samp_rate))
        self.analog_sig_source_x_0.set_sampling_freq(self.samp_rate)
        self.blocks_repeat_0.set_interpolation((int(self.pulse_duration * self.samp_rate) ))
        self.blocks_throttle2_0.set_sample_rate(self.samp_rate)

    def get_offset_freq(self):
        return self.offset_freq

    def set_offset_freq(self, offset_freq):
        self.offset_freq = offset_freq
        self.analog_sig_source_x_0.set_frequency(self.offset_freq)

    def get_fsk_deviation_hz(self):
        return self.fsk_deviation_hz

    def set_fsk_deviation_hz(self, fsk_deviation_hz):
        self.fsk_deviation_hz = fsk_deviation_hz
        self.analog_frequency_modulator_fc_0.set_sensitivity(((2 * math.pi * (self.fsk_deviation_hz / 2))/self.samp_rate))




def main(top_block_cls=fskmod, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
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
