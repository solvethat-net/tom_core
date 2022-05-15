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

# Generated 2022-05-15 19:54:37.818594
# Class Gui
class Gui:

    def run_gui(self):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().run_gui()

    def destroy_tkinter(self):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().destroy_tkinter()

    def clear_root(self):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().clear_root()

    def kill_gui(self):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().kill_gui()

    def write_to_db_table(self, path):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().write_to_db_table(path)

    def new_event(self):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().new_event()

    def open_event(self):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().open_event()

    def import_event(self):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().import_event()

    def user_manual_event(self):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().user_manual_event()

    def process_tool_bar(self):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().process_tool_bar()

    def width_by_percent(self, window, percent):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().width_by_percent(window, percent)

    def height_by_percent(self, window, percent):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().height_by_percent(window, percent)

    def is_in_gui_area(self, x_pos, y_pos):
        from ui.modules.gui.core.GuiController import GuiController
        return GuiController().is_in_gui_area(x_pos, y_pos)

    def start_tool_bar(self):
        from ui.modules.gui.core.ToolBarController import ToolBarController
        return ToolBarController().start_tool_bar()

    def hide_tool_bar_frame(self):
        from ui.modules.gui.core.ToolBarController import ToolBarController
        return ToolBarController().hide_tool_bar_frame()

    def show_created_tool_bar_frame(self):
        from ui.modules.gui.core.ToolBarController import ToolBarController
        return ToolBarController().show_created_tool_bar_frame()

    def show_message(self, message):
        from ui.modules.gui.core.ToolBarController import ToolBarController
        return ToolBarController().show_message(message)

    def reload_sequences_list(self):
        from ui.modules.gui.core.ToolBarController import ToolBarController
        return ToolBarController().reload_sequences_list()

    def show_sequences_list(self):
        from ui.modules.gui.core.ToolBarController import ToolBarController
        return ToolBarController().show_sequences_list()

    def stop_running_sequence(self):
        from ui.modules.gui.core.ToolBarController import ToolBarController
        return ToolBarController().stop_running_sequence()

    def show_pause_running_sequence_view(self):
        from ui.modules.gui.core.ToolBarController import ToolBarController
        return ToolBarController().show_pause_running_sequence_view()

# End of class Gui
