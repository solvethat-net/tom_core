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

import random
import mouse
import time
from mouse import UP, DOWN, DOUBLE, LEFT


class Mouse:

    def mouse_action(self, button, action):
        # Decide what type of mouse action simulate
        if action == DOWN:
            mouse.press(button)
        if action == UP:
            mouse.release(button)
        if action == DOUBLE:
            mouse.press(button)
            mouse.release(button)

    def random_click_into_area(self, x1, y1, x2, y2):
        x = random.randint(x1, x2)
        y = random.randint(y1, y2)
        self.move_cursor(x, y)
        self.mouse_action(LEFT, DOWN)
        time.sleep(random.uniform(0.1, random.uniform(0.5, 2)))
        self.mouse_action(LEFT, UP)

    def left_click_to_position(self, x, y):
        self.move_cursor(x, y)
        self.mouse_action(LEFT, DOWN)
        self.mouse_action(LEFT, UP)

    def move_cursor(self, x, y):
        # Simulate mouse move with cursor
        mouse.move(int(x), int(y))

    def scroll(self, value):
        # Simulate mouse wheel scroll
        mouse.wheel(float(value))
