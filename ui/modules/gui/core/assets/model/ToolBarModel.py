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

class ToolBarModel:
    voice_recording = False
    list_is_dropped = False
    first_time = True
    row_size = 0
    all_hidden = False
    main_view = True
    right_edge = 0
    bottom_edge = 0
    mouse_position = [0, 0]
    horizontal = False  # TRUE = RIGHT, FALSE = LEFT
    vertical = True  # TRUE = TOP, FALSE = BOTTOM
    current_horizontal_method = None
    current_vertical_method = None
    seq_list_loaded = False
    seq_id_while_listing = 0
    last_text = None
    no_config_mark = True
    running_sequence = False
    suspended_sequence = False
    interrupt_run = False
    restarting = False
