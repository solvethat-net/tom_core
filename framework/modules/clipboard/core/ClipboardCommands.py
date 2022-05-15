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

from ui.modules.gui.core.assets.model.GUIModel import GUIModel


class ClipboardCommands(GUIModel):

    def __init__(self):
        return

    def set_clipboard(self, text):
        # Set plain text or file path to clipboard
        GUIModel.root.clipboard_clear()
        GUIModel.root.clipboard_append(text)

    def get_clipboard(self):
        # Get plain text or file path from clipboard
        return GUIModel.root.clipboard_get()
