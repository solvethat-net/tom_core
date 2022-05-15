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

from tkinter import StringVar, Entry, END

from core_util.CoreModel import CoreModel
from framework.Framework import Framework
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from ui.modules.gui.core.assets.model.ToolBarModel import ToolBarModel


class TextInputView(GUIModel, ToolBarModel, CoreModel):

    def __init__(self):
        self.framework = Framework()
        self.user_input = StringVar(GUIModel.root)
        self.input_field = Entry(GUIModel.root, textvariable=self.user_input, borderwidth=0, width=25)
        self.input_field.bind('<Return>', self.go_fce)
        self.input_field.bind('<Down>', self.arrow_down)
        self.input_field.bind('<Up>', self.arrow_up)
        self.method_to_done = ""

    def show_base(self):
        # Show main mode of text input view
        ToolBarModel.current_horizontal_method = self.show_base
        ToolBarModel.current_vertical_method = None
        if self.horizontal:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=1)
            self.input_field.grid(row=ToolBarModel.row_size, column=0, padx=(0, 5))
        else:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=0)
            self.input_field.grid(row=ToolBarModel.row_size, column=1, padx=(5, 0))

    def hide_all(self):
        # Hide all widgets
        ToolBarModel.current_horizontal_method = self.hide_all
        ToolBarModel.current_vertical_method = None
        self.input_field.grid_forget()
        GUIModel.main_view.core_button.grid_forget()

    def go_fce(self, arg):
        # Is called when user hit Enter key as input confirm
        text = self.user_input.get()
        self.input_field.delete(0, END)
        self.framework.process_support.treatment_entry(text)

    def show_message(self, message):
        # Set text entry variable to custom message
        self.user_input.set(message)

    def arrow_up(self, event):
        # Browsing last entered inputs, go up, first up is most last
        if ToolBarModel.seq_id_while_listing == 0: ToolBarModel.last_text = self.user_input.get()
        tbl = self.framework.databases.get_just_sentence_from_seq_table()
        if abs(ToolBarModel.seq_id_while_listing) + 1 <= len(tbl):
            ToolBarModel.seq_id_while_listing = ToolBarModel.seq_id_while_listing - 1
            self.show_sequence_title_by_row_number(tbl)

    def arrow_down(self, event):
        # Browsing last entered inputs, go down
        if abs(ToolBarModel.seq_id_while_listing) > 0:
            tbl = self.framework.databases.get_just_sentence_from_seq_table()
            ToolBarModel.seq_id_while_listing = ToolBarModel.seq_id_while_listing + 1
            self.show_sequence_title_by_row_number(tbl)

    def show_sequence_title_by_row_number(self, tbl):
        # Show title by actual position while browsing last entries
        if ToolBarModel.seq_id_while_listing == 0:
            if ToolBarModel.last_text:
                self.user_input.set(ToolBarModel.last_text)
            else:
                self.user_input.set("")
        else:
            self.user_input.set(tbl[ToolBarModel.seq_id_while_listing][1])
