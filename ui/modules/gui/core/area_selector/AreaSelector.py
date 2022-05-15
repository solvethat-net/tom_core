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

from tkinter import Canvas, BOTH, Toplevel

from framework.Framework import Framework
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from ui.modules.gui.core.windows.BranchOutWindow import BranchOutWindow


class AreaSelector(GUIModel):

    def __init__(self, title, condition_enum):
        self.framework = Framework()
        self.title = title
        self.condition_enum = condition_enum
        self.window = Toplevel(GUIModel.root)
        self.window.overrideredirect(True)
        self.window.focus_set()
        # TODO multi display ??????
        self.window.geometry("1920x1080")
        self.window.attributes('-alpha', 0.1)
        self.window.bind('<Motion>', self.on_motion)
        self.window.bind("<ButtonPress-1>", self.start_draw)
        self.window.bind("<B1-Motion>", self.on_draw)
        self.window.bind("<B1-Motion>", self.on_draw)
        self.window.bind("<Escape>", self.on_cross_event)
        self.window.bind("<Return>", self.confirm_select)
        self.canvas = Canvas(self.window)
        self.canvas.pack(fill=BOTH, expand=1)
        GUIModel.area_selector_running = True
        self.selected_area = None
        self.resize_v_top = False
        self.resize_v_bottom = False
        self.resize_h_left = False
        self.resize_h_right = False
        self.resize_left_up = False
        self.resize_right_up = False
        self.resize_left_down = False
        self.resize_right_down = False
        self.confirmed = False

    def on_cross_event(self, event):
        # Call close method
        self.close_window()

    def close_window(self):
        # Destroy window and make area_selector_running false
        self.window.destroy()
        self.window.update()
        GUIModel.area_selector_running = False

    def confirm_select(self, event):
        # Set up GUIModel.select_... variables and create new branch out window
        self.confirmed = True
        self.window.destroy()
        self.window.update()

        if GUIModel.select_x2 < GUIModel.select_x1:
            new_x2 = GUIModel.select_x1
            GUIModel.select_x1 = GUIModel.select_x2
            GUIModel.select_x2 = new_x2

        if GUIModel.select_y2 < GUIModel.select_y1:
            new_y2 = GUIModel.select_y1
            GUIModel.select_y1 = GUIModel.select_y2
            GUIModel.select_y2 = new_y2

        GUIModel.base64_image = self.framework.screen_capturer.capture_area(GUIModel.select_x1, GUIModel.select_y1,
                                                                            GUIModel.select_x2, GUIModel.select_y2)
        GUIModel.post_area_select_treatment = BranchOutWindow(self.title, self.condition_enum)

    def on_motion(self, event):
        # Listener method set bool values by actual mouse position
        if self.selected_area:
            # Diagonal conditions
            if GUIModel.select_y1 - 15 <= event.y <= GUIModel.select_y1 + 15 and \
                    GUIModel.select_x1 - 15 <= event.x <= GUIModel.select_x1 + 15:
                self.resize_left_up = True
                self.canvas.config(cursor="size_nw_se")
            elif GUIModel.select_y2 - 15 <= event.y <= GUIModel.select_y2 + 15 and \
                    GUIModel.select_x2 - 15 <= event.x <= GUIModel.select_x2 + 15:
                self.resize_right_down = True
                self.canvas.config(cursor="size_nw_se")
            elif GUIModel.select_y1 - 15 <= event.y <= GUIModel.select_y1 + 15 and \
                    GUIModel.select_x2 - 15 <= event.x <= GUIModel.select_x2 + 15:
                self.resize_right_up = True
                self.canvas.config(cursor="size_ne_sw")
            elif GUIModel.select_y2 - 15 <= event.y <= GUIModel.select_y2 + 15 and \
                    GUIModel.select_x1 - 15 <= event.x <= GUIModel.select_x1 + 15:
                self.resize_left_down = True
                self.canvas.config(cursor="size_ne_sw")
            # Horizontal conditions
            elif GUIModel.select_x1 - 10 <= event.x <= GUIModel.select_x1 + 10 and \
                    GUIModel.select_y1 - 10 <= event.y <= GUIModel.select_y2 + 10:
                self.resize_h_left = True
                self.canvas.config(cursor="sb_h_double_arrow")
            elif GUIModel.select_x2 - 10 <= event.x <= GUIModel.select_x2 + 10 and \
                    GUIModel.select_y1 - 10 <= event.y <= GUIModel.select_y2 + 10:
                self.resize_h_right = True
                self.canvas.config(cursor="sb_h_double_arrow")
            # vertical conditions
            elif GUIModel.select_y1 - 10 <= event.y <= GUIModel.select_y1 + 10 and \
                    GUIModel.select_x1 - 10 <= event.x <= GUIModel.select_x2 + 10:
                self.resize_v_top = True
                self.canvas.config(cursor="sb_v_double_arrow")
            elif GUIModel.select_y2 - 10 <= event.y <= GUIModel.select_y2 + 10 and \
                    GUIModel.select_x1 - 10 <= event.x <= GUIModel.select_x2 + 10:
                self.resize_v_bottom = True
                self.canvas.config(cursor="sb_v_double_arrow")
            else:
                self.resize_v_top = False
                self.resize_v_bottom = False
                self.resize_h_left = False
                self.resize_h_right = False
                self.resize_left_up = False
                self.resize_right_up = False
                self.resize_left_down = False
                self.resize_right_down = False
                self.canvas.config(cursor="arrow")

    def set_coords_by_model(self):
        # Set up rectangle size by GUI model select position values
        self.canvas.coords(self.selected_area, GUIModel.select_x1, GUIModel.select_y1, GUIModel.select_x2,
                           GUIModel.select_y2)

    def start_draw(self, event):
        # GUI model select position values by bool position values or start draw new rectangle
        if self.resize_left_up:
            GUIModel.select_x1 = event.x
            GUIModel.select_y1 = event.y
            self.set_coords_by_model()
        elif self.resize_right_up:
            GUIModel.select_x2 = event.x
            GUIModel.select_y1 = event.y
            self.set_coords_by_model()
        elif self.resize_left_down:
            GUIModel.select_x1 = event.x
            GUIModel.select_y2 = event.y
            self.set_coords_by_model()
        elif self.resize_right_down:
            GUIModel.select_x2 = event.x
            GUIModel.select_y2 = event.y
            self.set_coords_by_model()
        elif self.resize_h_left:
            GUIModel.select_x1 = event.x
            self.set_coords_by_model()
        elif self.resize_h_right:
            GUIModel.select_x2 = event.x
            self.set_coords_by_model()
        elif self.resize_v_top:
            GUIModel.select_y1 = event.y
            self.set_coords_by_model()
        elif self.resize_v_bottom:
            GUIModel.select_y2 = event.y
            self.set_coords_by_model()
        else:
            self.canvas.delete("all")
            GUIModel.select_x1 = event.x
            GUIModel.select_y1 = event.y
            self.selected_area = self.canvas.create_rectangle(event.x, event.y, event.x, event.y, fill='blue',
                                                              outline='red', dash=(6, 6))

    def on_draw(self, event):
        # Resize rectangle while mouse drag from first left button press
        if self.resize_left_up:
            GUIModel.select_x1 = event.x
            GUIModel.select_y1 = event.y
            self.set_coords_by_model()
        elif self.resize_right_up:
            GUIModel.select_x2 = event.x
            GUIModel.select_y1 = event.y
            self.set_coords_by_model()
        elif self.resize_left_down:
            GUIModel.select_x1 = event.x
            GUIModel.select_y2 = event.y
            self.set_coords_by_model()
        elif self.resize_right_down:
            GUIModel.select_x2 = event.x
            GUIModel.select_y2 = event.y
            self.set_coords_by_model()
        elif self.resize_h_left:
            GUIModel.select_x1 = event.x
            self.set_coords_by_model()
        elif self.resize_h_right:
            GUIModel.select_x2 = event.x
            self.set_coords_by_model()
        elif self.resize_v_top:
            GUIModel.select_y1 = event.y
            self.set_coords_by_model()
        elif self.resize_v_bottom:
            GUIModel.select_y2 = event.y
            self.set_coords_by_model()
        else:
            GUIModel.select_x2 = event.x
            GUIModel.select_y2 = event.y
            self.canvas.coords(self.selected_area, GUIModel.select_x1, GUIModel.select_y1, event.x, event.y)
