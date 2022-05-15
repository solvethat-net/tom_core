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

from tkinter import Toplevel, Label

from ui.Ui import Ui
from ui.modules.gui.core.assets.model.GUIModel import GUIModel


class Tooltip(GUIModel):

    def __init__(self, widget, text):
        # Create a tooltip for a given widget
        self.ui = Ui()
        self.wait_time = 300  # milliseconds
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.window = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hide()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.wait_time, self.show)

    def unschedule(self):
        id = self.id
        self.id = None
        if id: self.widget.after_cancel(id)

    def show(self, event=None):
        self.window = Toplevel(self.widget)
        self.window.overrideredirect(True)
        # self.overrideredirect(True) - windows
        # self.wm_attributes('-type', 'splash') - linux
        self.window.attributes("-topmost", True)
        label = Label(self.window, text=self.text, justify='center', background="#ffffff", relief='solid',
                      borderwidth=1, wraplength=200)
        label.pack(ipadx=1)

        self.window.update()
        horizontal, vertical = self.get_horizontal_vertical()
        if self.window:
            if horizontal:
                x = (self.widget.winfo_rootx() - self.window.winfo_width()) + self.widget.winfo_width() / 2
            else:
                x = self.widget.winfo_rootx() + self.widget.winfo_width() / 2
            if vertical:
                y = self.widget.winfo_rooty() + self.widget.winfo_height()
            else:
                y = self.widget.winfo_rooty() - self.window.winfo_height()
            self.window.geometry("+%d+%d" % (x, y))

    def get_horizontal_vertical(self):
        # Get horizontal and vertical variables by actual widget position
        horizontal = False
        vertical = True
        if self.widget.winfo_rootx() + self.widget.winfo_width() > self.ui.gui.width_by_percent(GUIModel.root, 80):
            horizontal = True
        elif self.widget.winfo_rootx() < self.ui.gui.width_by_percent(GUIModel.root, 20):
            horizontal = False
        if self.widget.winfo_rooty() < self.ui.gui.height_by_percent(GUIModel.root, 20):
            vertical = True
        elif self.widget.winfo_rooty() + self.widget.winfo_height() > self.ui.gui.height_by_percent(GUIModel.root, 80):
            vertical = False
        return horizontal, vertical

    def hide(self):
        tw = self.window
        self.window = None
        if tw: tw.destroy()
