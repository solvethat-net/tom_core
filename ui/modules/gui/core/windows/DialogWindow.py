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

from tkinter import Frame, Toplevel, PhotoImage

from ui.modules.gui.core.assets import Base64Imgs


class DialogWindow:

    def __init__(self, root):
        self.window = Toplevel(root)
        self.dialog_window_frame = Frame()
        self.dialog_window_frame.pack()
        self.window.iconbitmap(default=Base64Imgs.core_logo_small)
        favicon = PhotoImage(data=Base64Imgs.core_logo_small)
        self.window.iconphoto(False, favicon)
        self.window.title("")
        # window.overrideredirect(True)
        self.window.geometry("150x50")
