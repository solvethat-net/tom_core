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

# Generated 2022-05-15 19:54:37.802968
from framework.modules.clipboard.Clipboard import Clipboard
from framework.modules.databases.Databases import Databases
from framework.modules.device_control.DeviceControl import DeviceControl
from framework.modules.event_player.EventPlayer import EventPlayer
from framework.modules.filesystem.Filesystem import Filesystem
from framework.modules.io_streams.IoStreams import IoStreams
from framework.modules.languages.Languages import Languages
from framework.modules.listeners.Listeners import Listeners
from framework.modules.non_lang_expressions.NonLangExpressions import NonLangExpressions
from framework.modules.ocr.Ocr import Ocr
from framework.modules.os_gui.OsGui import OsGui
from framework.modules.process_support.ProcessSupport import ProcessSupport
from framework.modules.screen_capturer.ScreenCapturer import ScreenCapturer
from framework.modules.sequences_support.SequencesSupport import SequencesSupport
from framework.modules.speech_recognizer.SpeechRecognizer import SpeechRecognizer


class Framework:
    clipboard = Clipboard()
    databases = Databases()
    device_control = DeviceControl()
    event_player = EventPlayer()
    filesystem = Filesystem()
    io_streams = IoStreams()
    languages = Languages()
    listeners = Listeners()
    non_lang_expressions = NonLangExpressions()
    ocr = Ocr()
    os_gui = OsGui()
    process_support = ProcessSupport()
    screen_capturer = ScreenCapturer()
    sequences_support = SequencesSupport()
    speech_recognizer = SpeechRecognizer()
# End of class Framework
