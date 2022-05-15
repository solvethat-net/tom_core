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
from ui.modules.gui.core.assets.model.ToolBarModel import ToolBarModel
from ui.modules.gui.core.tool_bar.MainView import MainView
from ui.modules.gui.core.tool_bar.SequenceListView import SequenceListView
from ui.modules.gui.core.tool_bar.SequenceView import SequenceView
from ui.modules.gui.core.tool_bar.TextInputView import TextInputView


class ToolBarController(GUIModel, ToolBarModel):

    def start_tool_bar(self):
        GUIModel.main_view = MainView()
        GUIModel.sequence_view = SequenceView()
        GUIModel.text_input_view = TextInputView()
        GUIModel.sequence_list_view = SequenceListView()
        # TODO self.overrideredirect(True) - windows
        #      self.wm_attributes('-type', 'splash') - linux
        GUIModel.root.overrideredirect(True)
        GUIModel.root.attributes("-topmost", True)
        GUIModel.root.geometry("")

        def on_focus_in_0(event):
            GUIModel.is_focused = True

        def on_focus_out_0(event):
            GUIModel.is_focused = False

        GUIModel.root.bind('<FocusIn>', on_focus_in_0)
        GUIModel.root.bind('<FocusOut>', on_focus_out_0)

    def hide_tool_bar_frame(self):
        # Hide main gui
        GUIModel.root.withdraw()
        GUIModel.gui_is_hidden = True

    def show_created_tool_bar_frame(self):
        # Show main gui
        GUIModel.root.deiconify()
        GUIModel.gui_is_hidden = False

    def show_message(self, message):
        # Show custom message in text input view
        GUIModel.root.hide_all()
        GUIModel.root.hide_all_views()
        GUIModel.text_input_view.show_base()
        ToolBarModel.main_view = False
        GUIModel.text_input_view.show_message(message)

    def reload_sequences_list(self):
        # Reload sequence list externally
        GUIModel.sequence_list_view.load_sequences()

    def show_sequences_list(self):
        # Show panel sequence list
        GUIModel.main_view.seq_button_click()
        GUIModel.sequence_view.show_seq_list()

    def stop_running_sequence(self):
        # Stop running sequence externally
        GUIModel.sequence_list_view.stop_running()

    def show_pause_running_sequence_view(self):
        # Show suspended run mode in sequence list view
        ToolBarModel.suspended_sequence = True
        ToolBarModel.current_horizontal_method = GUIModel.sequence_list_view.show_suspended_running
        ToolBarModel.current_vertical_method = None
        GUIModel.main_view.change_gui_orientation()
        GUIModel.main_view.place_to_saved_edge()
