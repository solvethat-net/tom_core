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

import webbrowser
from threading import Thread
from tkinter import Tk, PhotoImage
from tkinter.filedialog import asksaveasfilename, askopenfilename

from core_util.CoreModel import CoreModel
from framework.Framework import Framework
from ui.Ui import Ui
from ui.modules.gui.core.ToolBarController import ToolBarController
from ui.modules.gui.core.assets import Base64Imgs
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from ui.modules.gui.core.system_tray.TrayIcon import TrayIcon
from ui.modules.gui.core.windows.WelcomePanel import WelcomePanel


class GuiController(CoreModel, GUIModel):

    def __init__(self):
        self.framework = Framework()
        self.ui = Ui()
        self.opw = 0
        self.oph = 0

    def run_gui(self):
        tom_core_image = Base64Imgs.core_logo_small
        GUIModel.root = Tk()
        GUIModel.root.title("tom_core")
        GUIModel.root.iconbitmap(default=tom_core_image)
        GUIModel.root.iconphoto(False, PhotoImage(data=tom_core_image))
        GUIModel.system_tray = TrayIcon()
        Thread(target=GUIModel.system_tray.init_icon, name="run_gui-system_tray.init_icon").start()
        if CoreModel.current_db_file_path:
            ToolBarController().start_tool_bar()
        else:
            WelcomePanel()
        GUIModel.root.mainloop()

        # for thread in threading.enumerate():
        #     print(thread.name)

    def destroy_tkinter(self):
        # Kill all tkinter
        GUIModel.root.destroy()

    def clear_root(self):
        for widgets in GUIModel.root.winfo_children(): widgets.destroy()

    def kill_gui(self):
        # Kill application
        Thread(daemon=True, name="kill_gui-destroy_tkinter", target=self.destroy_tkinter).start()
        GUIModel.system_tray.stop_tray()

    def write_to_db_table(self, path):
        name = path[path.rfind("/") + 1:]
        self.framework.databases.write_to_databases_table(path, name)

    def new_event(self):
        # Get new database path
        filename = asksaveasfilename(defaultextension=".db", filetypes=(("Database file", "*.db"),))
        if filename:
            self.framework.databases.create_current_db(filename)
            self.framework.databases.save_configuration("current_database", filename)
            CoreModel.current_db_file_path = filename
            self.write_to_db_table(filename)
            self.process_tool_bar()

    def open_event(self):
        # Get path to existing database
        filename = askopenfilename(filetypes=[("Database file", "*.db")])
        if filename:
            self.framework.databases.save_configuration("current_database", filename)
            CoreModel.current_db_file_path = filename
            self.write_to_db_table(filename)
            self.process_tool_bar()

    def import_event(self):
        # TODO https://tableplus.com/blog/2018/07/sqlite-how-to-copy-table-to-another-database.html
        #  filename = askopenfilename()
        pass

    def user_manual_event(self):
        # Open url in default browser
        webbrowser.open('https://solvethat.net/manual.html')

    def process_tool_bar(self):
        # Restart tool bar and show seq list view
        if not GUIModel.main_view:
            self.clear_root()
            self.ui.gui.start_tool_bar()
        self.ui.gui.reload_sequences_list()
        self.ui.gui.show_sequences_list()

    def create_ops_0(self, window):
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        self.opw = width / 100
        self.oph = height / 100

    def width_by_percent(self, window, percent):
        # Return how much PX is given percent width
        self.create_ops_0(window)
        return round(self.opw * percent)

    def height_by_percent(self, window, percent):
        # Return how much PX is given percent height
        self.create_ops_0(window)
        return round(self.oph * percent)

    def is_in_gui_area(self, x_pos, y_pos):
        # Check if cursor is not in gui used screen area
        horizontal = False
        vertical = False
        if GUIModel.x_pos < x_pos < GUIModel.x_pos + GUIModel.width: horizontal = True
        if GUIModel.y_pos < y_pos < GUIModel.y_pos + GUIModel.height: vertical = True
        if vertical and horizontal:
            return True
        else:
            return False
