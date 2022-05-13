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

class PlayerModel:
    keyboard_lock = None
    paused_running = False
    break_running = False
    handler_is_running = False
    condition_mouse_position = None
    custom_delay = None
    watcher_check_var = None
    loop_is_running = False
    ocr_check_position = None
    ocr_check_np_arr = None
    esc_once_pressed = False
