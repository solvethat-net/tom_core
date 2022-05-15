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

import base64

import pystray
from pystray import Menu, MenuItem
from PIL import Image
from io import BytesIO

from core_util.CoreModel import CoreModel
from ui.Ui import Ui
from ui.modules.gui.core.assets import Base64Imgs
from ui.modules.gui.core.assets.model.GUIModel import GUIModel


class TrayIcon(CoreModel, GUIModel):

    def __init__(self):
        self.ui = Ui()
        self.icon = None

    def default_action(self, icon):
        # Default action is hiding and showing of main gui
        if GUIModel.gui_is_hidden:
            self.ui.gui.show_created_tool_bar_frame()
            GUIModel.gui_is_hidden = False
        else:
            self.ui.gui.hide_tool_bar_frame()
            GUIModel.gui_is_hidden = True

    def stop_tray(self):
        # Kill pystray
        self.icon.visible = False
        self.icon.stop()

    def setup(self, icon):
        # Pystray icon setup
        icon.visible = True

    def init_icon(self):
        # Create tray icon and show
        tom_core_ico = Base64Imgs.core_logo_small
        image = Image.open(BytesIO(base64.b64decode(tom_core_ico)))
        self.icon = pystray.Icon('')
        self.icon.menu = Menu(MenuItem('', self.default_action, default=True, visible=False),
                              MenuItem('New...', lambda: self.ui.gui.new_event()),
                              MenuItem('Open...', lambda: self.ui.gui.open_event()),
                              # MenuItem('Import', lambda: self.import_event()),
                              MenuItem('User manual', lambda: self.ui.gui.user_manual_event()),
                              MenuItem('End application', lambda: self.ui.gui.kill_gui()))
        self.icon.icon = image
        self.icon.title = 'tom_core'
        self.icon.run(self.setup)
