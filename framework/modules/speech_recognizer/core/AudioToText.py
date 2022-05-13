# TOM_CORE version n. 0.1.5
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
# https://www.solvethat.net/installer/GNU_License.pdf

import speech_recognition

from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from ui.Ui import Ui


class AudioToText(CoreModel):

    def __init__(self):
        self.recognizer = speech_recognition.Recognizer()
        self.framework = Framework()
        self.ui = Ui()

    def convert_audio_to_text(self, audio_file):
        # Convert audio file with recorded voice to string
        for one_language in CoreModel.language_list:
            try:
                text = self.recognizer.recognize_google(audio_file, language=one_language)
                self.ui.terminal.print_info_log("Audio file is " + one_language)
                return text
            except:
                pass
        self.ui.terminal.print_warn_log("Audio file language wasn't recognized")
        return MetadataEnum.ERROR
        # TODO try all API
        #     recognize_bing(): Microsoft Bing Speech
        #     recognize_google(): Google Web Speech API
        #     recognize_houndify(): Houndify by SoundHound
        #     recognize_ibm(): IBM Speech to Text
        #     recognize_wit(): Wit.ai
        #     recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
        #     recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
