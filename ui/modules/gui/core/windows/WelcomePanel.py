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

import webbrowser
from tkinter import PhotoImage, Label, Listbox, Scrollbar, END, Canvas, Button, LEFT
from tkinter.filedialog import asksaveasfilename, askopenfilename

from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from process.Process import Process
from ui.Ui import Ui
from ui.modules.gui.core.assets import Base64Imgs
from ui.modules.gui.core.assets.model.GUIModel import GUIModel


class WelcomePanel(CoreModel, GUIModel):

    def __init__(self):
        GUIModel.root.title("Welcome panel")
        self.framework = Framework()
        self.process = Process()
        self.ui = Ui()
        GUIModel.root.protocol("WM_DELETE_WINDOW", self.ui.gui.kill_gui)
        GUIModel.root.geometry("800x400")
        win_pos_start_x = self.ui.gui.width_by_percent(GUIModel.root, 50) - 400
        win_pos_start_y = self.ui.gui.height_by_percent(GUIModel.root, 50) - 250
        GUIModel.root.geometry("+%s+%s" % (win_pos_start_x, win_pos_start_y))
        GUIModel.root.resizable(False, False)

        self.welcome_icon = PhotoImage(data=Base64Imgs.welcome_image)
        self.new_icon = PhotoImage(data=Base64Imgs.new_database)
        self.open_icon = PhotoImage(data=Base64Imgs.open_database)
        self.user_manual_icon = PhotoImage(data=Base64Imgs.user_manual)

        self.recent_label = Label(GUIModel.root, text="Recents databases:")
        self.listbox = Listbox(GUIModel.root, borderwidth=5, highlightbackground="white", highlightcolor="white",
                               relief="flat", highlightthickness=0, activestyle="none", selectbackground="#f6e81d",
                               selectforeground="Black", justify=LEFT, exportselection=False, width=40, height=22)

        self.new_button = Button(GUIModel.root, image=self.new_icon, command=self.new_event, borderwidth=0)
        self.open_button = Button(GUIModel.root, image=self.open_icon, command=self.open_event, borderwidth=0)
        self.user_manual_button = Button(GUIModel.root, image=self.user_manual_icon, command=self.user_manual_event,
                                         borderwidth=0)
        self.listbox_data = []
        self.listbox.bind('<Return>', self.go_event)
        self.listbox.bind('<Double-Button>', self.go_event)
        self.listbox.bind("<<ListboxSelect>>", self.update_selection)
        self.scrollbar = Scrollbar(GUIModel.root, command=self.listbox.xview, borderwidth=1)
        self.scrollbar = Scrollbar(GUIModel.root, command=self.listbox.yview, borderwidth=1)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        canvas = Canvas(GUIModel.root, width=500, height=200)
        canvas.grid(row=1, column=0, columnspan=4, rowspan=2, padx=(15, 0), pady=(0, 0))

        GUIModel.root.welcome_icon = self.welcome_icon
        canvas.create_image((0, 0), image=self.welcome_icon, anchor='nw')

        self.recent_label.grid(row=0, column=4, rowspan=1, padx=(14, 0), pady=(10, 0), sticky='W')
        self.listbox.grid(row=1, column=4, columnspan=1, rowspan=5, padx=(15, 0), pady=(0, 0))

        self.new_button.grid(row=3, column=0, columnspan=1, rowspan=1, padx=(45, 0), pady=(15, 0), sticky='W')
        self.open_button.grid(row=3, column=1, columnspan=1, rowspan=1, padx=(50, 0), pady=(15, 0), sticky='W')
        self.user_manual_button.grid(row=3, column=2, columnspan=1, rowspan=1, padx=(50, 0), pady=(15, 0), sticky='W')

        self.load_databases()

    def load_databases(self):
        new_content = []
        self.listbox_data = self.framework.databases.get_all_udb_entity("DATABASES")
        ind = 0
        for one in self.listbox_data:
            if self.framework.filesystem.getFile().check_exist(one[0]) == MetadataEnum.OK:
                new_content.append(one)
                self.listbox.insert(END, one[1])
                self.listbox.itemconfig(ind, {'fg': 'black'})
                self.listbox.insert(END, one[0])
                ind += 1
                self.listbox.itemconfig(ind, {'fg': 'dark green'})
                ind += 1
        self.framework.databases.rewrite_databases_table(new_content)

    def clear_frame(self):
        for widgets in GUIModel.root.winfo_children(): widgets.destroy()

    def new_event(self):
        filepath = asksaveasfilename(defaultextension=".db", filetypes=(("Database file", "*.db"),))
        if filepath:
            self.framework.databases.create_current_db(filepath)
            self.framework.databases.save_configuration("current_database", filepath)
            CoreModel.current_db_file_path = filepath
            self.write_to_db_table(filepath)
            self.process_tool_bar()

    def open_event(self):
        filepath = askopenfilename(filetypes=[("Database file", "*.db")])
        if filepath:
            self.framework.databases.save_configuration("current_database", filepath)
            CoreModel.current_db_file_path = filepath
            self.write_to_db_table(filepath)
            self.process_tool_bar()

    def user_manual_event(self):
        webbrowser.open('https://solvethat.net/manual.html')

    def go_event(self, arg):
        if self.listbox.curselection():
            select_index = self.listbox.curselection()[0]
            if select_index > 0: select_index -= 1
            select = self.listbox_data[select_index]
            self.framework.databases.save_configuration("current_database", select[0])
            CoreModel.current_db_file_path = select[0]
            self.process_tool_bar()

    def process_tool_bar(self):
        self.clear_frame()
        self.ui.gui.start_tool_bar()
        self.ui.gui.reload_sequences_list()
        self.ui.gui.show_sequences_list()

    def write_to_db_table(self, path):
        name = path[path.rfind("/") + 1:]
        self.framework.databases.write_to_databases_table(path, name)

    def update_selection(self, arg):
        if self.listbox.curselection():
            if (self.listbox.curselection()[0] % 2) == 0:
                self.listbox.selection_set(self.listbox.curselection()[0], self.listbox.curselection()[0] + 1)
            else:
                self.listbox.selection_set(self.listbox.curselection()[0] - 1, self.listbox.curselection()[0])
