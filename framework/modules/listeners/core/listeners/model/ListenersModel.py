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

class ListenersModel:
    turn_off_just_speech = True
    key_list = []
    mouse_position = [0, 0]
    mouse_lock = None
    keyboard_lock = None
    keyboard_listener_initialized = False
    mouse_listener_initialized = False
    keyboard_recording = False
    mouse_recording = False
    recording_in_progress = False
    mouse_pressed = False
    last_mouse_event = None
