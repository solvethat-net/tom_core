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

import time
import keyboard
import random

from keyboard import KEY_UP, KEY_DOWN


class Keyboard:

    def __init__(self):
        pass

    def keyboard_action(self, key, action):
        # Decide what type of keyboard action simulate
        if action == KEY_DOWN:
            keyboard.press(key)
        if action == KEY_UP:
            keyboard.release(key)

    def press_and_release_key(self, key):
        keyboard.press(key)
        keyboard.release(key)

    def highlight(self, direction):
        # Simulate text highlight
        keyboard.press_and_release("ctrl,left shift,right shift+" + direction)

    def ctrl_v(self):
        # Simulate paste
        keyboard.press_and_release("ctrl+v")

    def alt_tab(self):
        keyboard.press_and_release("alt+tab")

    def alt_f4(self):
        keyboard.press_and_release("alt+f4")

    def type_text_with_random_delay(self, text):
        # Simulate user typing on keyboard
        for one in text:
            if one == '@':
                keyboard.press_and_release("shift+@")
            else:
                time.sleep(random.uniform(0.1, random.uniform(0.5, 1)))
                # TODO Znaky pod klavesovymi skratkami napr. @ je treba stisknout s shiftem ??
                self.keyboard_action(one, KEY_DOWN)
                time.sleep(random.uniform(0.1, random.uniform(0.5, 1)))
                self.keyboard_action(one, KEY_UP)
