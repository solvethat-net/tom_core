# TOM_CORE version n. 0.1.6
# Copyright (C) 2022 Tomáš Sýkora

# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program; if not, is available on:
# https://www.solvethat.net/installer/LICENSE

from threading import Thread

import speech_recognition as sr

from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from framework.modules.listeners.core.listeners.model.ListenersModel import ListenersModel
from ui.Ui import Ui


class SpeechListener(ListenersModel):

    def __init__(self):
        self.framework = Framework()
        self.ui = Ui()

    def listening_0(self):
        # Run speech record and call convert to text on turn off
        ListenersModel.turn_off_just_speech = False
        with sr.Microphone() as source:
            while not ListenersModel.turn_off_just_speech:
                audio = sr.Recognizer().listen(source)
                if not ListenersModel.turn_off_just_speech:
                    text = self.framework.speech_recognizer.convert_audio_to_text(audio)
                    if text != MetadataEnum.ERROR:
                        self.ui.terminal.print_info_log("Speech recognized as: " + text)
                        text = text.lower()
                        self.framework.process_support.treatment_entry(text)
                    else:
                        self.ui.terminal.print_warn_log(str(text))
                else:
                    break

    def run_speech_listener(self):
        # Run speech recording in new thread
        Thread(target=self.listening_0, name="run_speech_listener-listening_0").start()

    def stop_speech_listener(self):
        # Kill speech recording thread by switch to True
        ListenersModel.turn_off_just_speech = True
