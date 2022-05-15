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

# Generated 2022-05-15 19:54:37.818594
# Class DeviceControl
class DeviceControl:

    def keyboard_action(self, key, action):
        from framework.modules.device_control.core.Keyboard import Keyboard
        return Keyboard().keyboard_action(key, action)

    def press_and_release_key(self, key):
        from framework.modules.device_control.core.Keyboard import Keyboard
        return Keyboard().press_and_release_key(key)

    def highlight(self, direction):
        from framework.modules.device_control.core.Keyboard import Keyboard
        return Keyboard().highlight(direction)

    def ctrl_v(self):
        from framework.modules.device_control.core.Keyboard import Keyboard
        return Keyboard().ctrl_v()

    def alt_tab(self):
        from framework.modules.device_control.core.Keyboard import Keyboard
        return Keyboard().alt_tab()

    def alt_f4(self):
        from framework.modules.device_control.core.Keyboard import Keyboard
        return Keyboard().alt_f4()

    def type_text_with_random_delay(self, text):
        from framework.modules.device_control.core.Keyboard import Keyboard
        return Keyboard().type_text_with_random_delay(text)

    def mouse_action(self, button, action):
        from framework.modules.device_control.core.Mouse import Mouse
        return Mouse().mouse_action(button, action)

    def random_click_into_area(self, x1, y1, x2, y2):
        from framework.modules.device_control.core.Mouse import Mouse
        return Mouse().random_click_into_area(x1, y1, x2, y2)

    def left_click_to_position(self, x, y):
        from framework.modules.device_control.core.Mouse import Mouse
        return Mouse().left_click_to_position(x, y)

    def move_cursor(self, x, y):
        from framework.modules.device_control.core.Mouse import Mouse
        return Mouse().move_cursor(x, y)

    def scroll(self, value):
        from framework.modules.device_control.core.Mouse import Mouse
        return Mouse().scroll(value)

# End of class DeviceControl
