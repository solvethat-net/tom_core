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

import mouse
import win32api
from datetime import datetime
from threading import Lock
from mouse import ButtonEvent, MoveEvent, WheelEvent, LEFT, RIGHT, MIDDLE, DOWN, UP, DOUBLE
from core_util.MetadataEnum import MetadataEnum
from ui.Ui import Ui
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from framework.modules.listeners.core.listeners.model.ListenersModel import ListenersModel


class MouseListener(ListenersModel, GUIModel):

    def __init__(self):
        self.ui = Ui()

    def run(self):
        # Start mouse listener with own event handler
        self.ui.terminal.print_info_log("Mouse listener ON")
        # from ctypes import windll
        # user32 = windll.user32
        # user32.SetProcessDPIAware()
        GUIModel.is_focused = False
        ListenersModel.mouse_pressed = False
        ListenersModel.mouse_lock = Lock()
        ListenersModel.mouse_lock.acquire()

        def append_position():
            # Append mouse move event to key list by last saved position
            ListenersModel.key_list.append(
                [datetime.now(), [ListenersModel.mouse_position[0], ListenersModel.mouse_position[1]],
                 [[MetadataEnum.MOUSE_MOVE]],
                 [MetadataEnum.USER, MetadataEnum.MOUSE, MetadataEnum.INPUT]])

        def check_position_of_area_selection():
            # If cursor position is in area of previous selection append LAST_MOUSE_POSITION enum
            if GUIModel.select_x1 <= ListenersModel.mouse_position[0] <= GUIModel.select_x2 and GUIModel.select_y1 <= \
                    ListenersModel.mouse_position[1] <= GUIModel.select_y2:
                ListenersModel.key_list.append(
                    [datetime.now(), [ListenersModel.mouse_position[0], ListenersModel.mouse_position[1]],
                     [[MetadataEnum.CONDITION_MOUSE_POSITION]],
                     [MetadataEnum.USER, MetadataEnum.MOUSE, MetadataEnum.INPUT]])
            else:
                append_position()

        def handler(event):
            # Handle mouse event
            if isinstance(event, MoveEvent):
                cursor_position = win32api.GetCursorPos()
                GUIModel.is_focused = self.ui.gui.is_in_gui_area(cursor_position[0], cursor_position[1])
                ListenersModel.mouse_position = [cursor_position[0], cursor_position[1]]

                if not GUIModel.is_focused:
                    if ListenersModel.mouse_pressed:
                        append_position()

            if GUIModel.capturing_mouse_on and not GUIModel.is_focused and not self.ui.gui.is_in_gui_area(
                    ListenersModel.mouse_position[0],
                    ListenersModel.mouse_position[1]):
                if not GUIModel.area_selector_running:
                    if isinstance(event, WheelEvent):
                        if ListenersModel.last_mouse_event != MetadataEnum.MOUSE_SCROLL:
                            append_position()

                        ListenersModel.last_mouse_event = MetadataEnum.MOUSE_SCROLL

                        ListenersModel.key_list.append(
                            [datetime.now(), [event.delta],
                             [[MetadataEnum.MOUSE_SCROLL]],
                             [MetadataEnum.USER, MetadataEnum.MOUSE, MetadataEnum.INPUT]])

                    if isinstance(event, ButtonEvent):
                        if not GUIModel.do_not_capture_next_mouse_click:
                            meta = None
                            event_type = None

                            if event.button == LEFT:
                                meta = MetadataEnum.MOUSE_LEFT

                            if event.button == RIGHT:
                                meta = MetadataEnum.MOUSE_RIGHT

                            if event.button == MIDDLE:
                                meta = MetadataEnum.MOUSE_MIDDLE

                            if event.event_type == DOWN or event.event_type == DOUBLE:
                                event_type = DOWN
                                ListenersModel.mouse_pressed = True
                                if GUIModel.select_x1:
                                    check_position_of_area_selection()
                                else:
                                    append_position()

                            elif event.event_type == UP and ListenersModel.mouse_pressed:
                                event_type = UP
                                ListenersModel.mouse_pressed = False

                            ListenersModel.last_mouse_event = meta

                            if meta and event_type:
                                ListenersModel.key_list.append(
                                    [datetime.now(), [event_type], [[meta]],
                                     [MetadataEnum.USER, MetadataEnum.MOUSE, MetadataEnum.INPUT]])
                        else:
                            GUIModel.do_not_capture_next_mouse_click = False

        mouse._listener.add_handler(handler)
        ListenersModel.mouse_lock.acquire()
        mouse._listener.remove_handler(handler)

    def stop(self):
        # Stop mouse listener
        ListenersModel.recording_in_progress = False
        ListenersModel.mouse_listener_initialized = False
        ListenersModel.mouse_lock.release()
        self.ui.terminal.print_info_log("Mouse listener OFF")
