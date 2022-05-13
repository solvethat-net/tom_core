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

class GUIModel:
    width = 0
    height = 0
    x_pos = 0
    y_pos = 0

    root = None
    system_tray = None

    main_view = None
    sequence_list_view = None
    sequence_view = None
    text_input_view = None

    gui_is_hidden = False
    is_focused = False
    turn_off_listeners = True
    capturing_keyboard_on = False
    capturing_mouse_on = False

    select_x1 = None
    select_y1 = None
    select_x2 = None
    select_y2 = None

    area_selector_running = False
    area_selector = None
    post_area_select_treatment = None
    do_not_capture_next_mouse_click = False
    base64_image = None
