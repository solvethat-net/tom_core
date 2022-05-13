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

from datetime import datetime
from threading import Thread

from core_util.MetadataEnum import MetadataEnum
from core_util.SynapseModel import SynapseModel
from framework.Framework import Framework
from framework.modules.listeners.core.listeners.KeyboardListener import KeyboardListener
from framework.modules.listeners.core.listeners.model.ListenersModel import ListenersModel
from framework.modules.listeners.core.listeners.MouseListener import MouseListener


class KeyLogger(ListenersModel):

    def __init__(self):
        self.framework = Framework()
        self.mouse_listener = MouseListener()
        self.keyboard_listener = KeyboardListener()

    def init_key_list(self):
        # Init recording vars
        if not ListenersModel.recording_in_progress:
            ListenersModel.recording_in_progress = True
            ListenersModel.key_list = [[datetime.now(), ["start"], [[MetadataEnum.START]],
                                        [MetadataEnum.SYSTEM, MetadataEnum.LIST, MetadataEnum.START]]]

    def get_recorded_data(self):
        # Return key list as synapse model
        synapse_model = SynapseModel()
        synapse_model.data.extend(ListenersModel.key_list)
        return synapse_model

    def run_key_listener(self):
        # Run only keyboard listener
        self.init_key_list()
        ListenersModel.keyboard_recording = True
        if not ListenersModel.keyboard_listener_initialized:
            ListenersModel.keyboard_listener_initialized = True
            Thread(target=self.keyboard_listener.run, name="run_key_listener-keyboard_listener.run").start()

    def run_mouse_listener(self):
        # Run only mouse listener
        self.init_key_list()
        ListenersModel.mouse_recording = True
        if not ListenersModel.mouse_listener_initialized:
            ListenersModel.mouse_listener_initialized = True
            Thread(target=self.mouse_listener.run, name="run_mouse_listener-mouse_listener.run").start()

    def run_both(self):
        # Run keyboard and mouse listener
        if not ListenersModel.recording_in_progress:
            ListenersModel.key_list = [
                [datetime.now(), ["start"], [[MetadataEnum.START]],
                 [MetadataEnum.SYSTEM, MetadataEnum.LIST, MetadataEnum.START]]]
            Thread(target=self.mouse_listener.run, name="run_both-self.mouse_listener.run").start()
            Thread(target=self.keyboard_listener.run, name="run_both-keyboard_listener.run").start()
            self.framework.listeners.run_speech_listener()

    def stop_key_listener(self):
        # Stop keyboard listener
        ListenersModel.keyboard_recording = False
        self.keyboard_listener.stop()

    def stop_mouse_listener(self):
        # Stop mouse listener
        ListenersModel.mouse_recording = False
        self.mouse_listener.stop()

    def stop_all(self):
        # Stop keyboard and mouse listener
        ListenersModel.recording_in_progress = False
        if ListenersModel.keyboard_recording and ListenersModel.mouse_recording:
            ListenersModel.keyboard_recording = False
            self.keyboard_listener.stop()
            ListenersModel.mouse_recording = False
            self.mouse_listener.stop()
        elif ListenersModel.keyboard_recording and not ListenersModel.mouse_recording:
            self.stop_key_listener()
        elif not ListenersModel.keyboard_recording and ListenersModel.mouse_recording:
            self.stop_mouse_listener()
