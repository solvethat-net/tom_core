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

import importlib

import keyboard
from keyboard import KEY_DOWN, KEY_UP
from datetime import datetime
from threading import Lock
from core_util.MetadataEnum import MetadataEnum
from ui.Ui import Ui
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from framework.modules.listeners.core.listeners.model.ListenersModel import ListenersModel


class KeyboardListener(ListenersModel, GUIModel):

    def __init__(self):
        self.ui = Ui()
        self.pressed = []

    def run(self):
        # Start keyboard listener with own event handler
        self.ui.terminal.print_info_log("Keyboard listener ON")
        importlib.reload(keyboard)
        ListenersModel.keyboard_lock = Lock()
        ListenersModel.keyboard_lock.acquire()

        def replace_shift(event_text):
            if 'shift' in event_text or event_text == 'shift':
                return event_text.replace('shift', 'left shift,right shift')
            return event_text

        def handler(event):
            # Handle keyboard events
            if not GUIModel.is_focused and GUIModel.capturing_keyboard_on and not GUIModel.area_selector_running:

                if event.event_type == KEY_DOWN:
                    self.pressed.append(event.name)

                if event.event_type == KEY_UP:
                    shortcut = None
                    if len(self.pressed) > 1:
                        shortcut = replace_shift('+'.join(self.pressed))
                    elif len(self.pressed) == 1:
                        shortcut = self.pressed[0]

                    self.pressed = []
                    if shortcut:
                        ListenersModel.key_list.append(
                            [datetime.now(), [shortcut, KEY_DOWN], [[MetadataEnum.KEYBOARD]],
                             [MetadataEnum.USER, MetadataEnum.KEYBOARD, MetadataEnum.INPUT]])

                    ListenersModel.key_list.append(
                        [datetime.now(), [replace_shift(event.name), event.event_type], [[MetadataEnum.KEYBOARD]],
                         [MetadataEnum.USER, MetadataEnum.KEYBOARD, MetadataEnum.INPUT]])

        keyboard._listener.add_handler(handler)
        ListenersModel.keyboard_lock.acquire()
        keyboard._listener.remove_handler(handler)

    def stop(self):
        # Stop keyboard listener
        keyboard.unhook_all()
        ListenersModel.keyboard_lock.release()
        ListenersModel.recording_in_progress = False
        ListenersModel.keyboard_listener_initialized = False
        self.ui.terminal.print_info_log("Keyboard listener OFF")
