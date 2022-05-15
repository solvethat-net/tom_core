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

from tkinter import Frame, Entry, Listbox, END, Scrollbar, CENTER, PhotoImage, Button

from framework.Framework import Framework
from ui.modules.gui.core.assets import Base64Imgs


class Combobox(Frame):

    def __init__(self, parent, on_change_method=None, listbox_data=None):
        super(Combobox, self).__init__(parent)
        if listbox_data is None:
            listbox_data = []
        self.parent = parent
        self.framework = Framework()
        self.listbox_dropped = False
        self.listbox_initialized = False
        self.get_filtered = False
        self.on_change_method = on_change_method
        self.listbox_data = []
        self.items = 0
        self.original_parent_height = self.parent.winfo_height()
        self.filter_indexes_arr = []
        self.parent_resize_method = None
        self.button_up_image = PhotoImage(data=Base64Imgs.arrow_up)
        self.button_down_image = PhotoImage(data=Base64Imgs.arrow_down)
        self.button = Button(self, image=self.button_down_image, borderwidth=0, command=self.show_hide_listbox)
        # PhotoImage - Garbage Collector bug solution
        self.text_entry = Entry(self, width=46, justify=CENTER)
        self.listbox = Listbox(self, width=50, highlightthickness=0, activestyle="none", selectbackground="#f6e81d",
                               selectforeground="Black", justify=CENTER, exportselection=False)
        self.scrollbar = Scrollbar(self, command=self.listbox.yview, borderwidth=0)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.text_entry.bind('<Key>', self.text_entry_change_event)
        self.text_entry.bind('<BackSpace>', self.backspace_event)
        self.text_entry.bind('<Down>', self.arrow_down_event)
        self.listbox.bind('<Up>', self.arrow_up_event)
        self.listbox.bind('<<ListboxSelect>>', self.listbox_item_select_event)
        self.text_entry.bind('<FocusIn>', self.text_entry_focus_in_event)
        self.set_listbox_data(listbox_data)
        self.text_entry.grid(row=1, columnspan=2)
        self.button.grid(row=1, column=2)

    def set_listbox_data(self, data_array):
        # Set listbox content by data_array param
        self.listbox.delete(0, 'end')
        self.listbox_data = data_array
        for one in data_array: self.listbox.insert(END, one[1])
        if not len(self.listbox_data): self.listbox.insert(END, "Nothing to show")
        self.listbox_initialized = True
        self.get_filtered = False
        self.listbox.select_set(0)

    def reset_listbox(self):
        # Fill listbox with original init data and set height
        for one in self.listbox_data: self.listbox.insert(END, one[1])
        self.get_filtered = False
        self.listbox.select_set(0)
        self.set_heights()

    def get_listbox_select(self):
        # Get selected row of listbox widget
        if self.listbox_data:
            if self.get_filtered:
                return self.listbox_data[self.filter_indexes_arr[self.listbox.curselection()[0]]]
            else:
                return self.listbox_data[self.listbox.curselection()[0]]
        else:
            return False

    def bind_resize_parent_method(self, method):
        # Set resize parent method
        self.parent_resize_method = method

    def set_heights(self):
        # Set height of listbox and his parent by listbox content
        self.items = self.get_listbox_size()
        if self.items > 20: self.items = 20
        self.listbox.config(height=self.items)
        if self.parent_resize_method: self.parent_resize_method()

    def get_listbox_size(self):
        # Get listbox size by actual event
        if self.get_filtered:
            return len(self.filter_indexes_arr)
        else:
            return len(self.listbox_data)

    def show_hide_listbox(self):
        # Manage display of listbox by pressing arrows
        if not self.listbox_dropped:
            self.button.config(image=self.button_up_image)
            self.listbox.grid(row=2, columnspan=3)
            self.listbox_dropped = True
            self.set_heights()
        else:
            self.button.config(image=self.button_down_image)
            self.listbox.grid_forget()
            self.listbox_dropped = False
            self.set_heights()

    def arrow_up_event(self, event):
        # Set focus to text entry when first item is selected
        if self.listbox.curselection()[0] == 0: self.text_entry.focus_set()

    def arrow_down_event(self, event):
        # Set focus to listbox when press down arrow
        if self.items > 0:
            self.listbox.focus_set()
            self.listbox.select_set(0)
            self.listbox_item_select_event(event)

    def backspace_event(self, event):
        # Replace selected substring if selection is present and call filter method
        if self.text_entry.selection_present():
            start_select_index = self.text_entry.index("sel.first")
            end_select_index = self.text_entry.index("sel.last")
            new_val = self.text_entry.get().replace(self.text_entry.get()[start_select_index:end_select_index], "")
            self.text_entry.delete(0, END)
            self.text_entry.insert(0, new_val)
        self.text_entry_change_event(event)

    def text_entry_change_event(self, event):
        # Filter listbox content by string in entry widget
        self.listbox.delete(0, 'end')
        self.filter_indexes_arr = []
        self.text_entry.update()
        if self.text_entry.get():
            for one in self.listbox_data:
                if self.text_entry.get().lower() in one[1].lower():
                    self.listbox.insert(END, one[1])
                    self.filter_indexes_arr.append(self.listbox_data.index(one))
            if not len(self.filter_indexes_arr):
                self.listbox.insert(END, "Nothing to show")
            else:
                self.get_filtered = True
                self.set_heights()
        else:
            self.reset_listbox()

    def text_entry_focus_in_event(self, event):
        # Set widget focus bool and hide listbox
        if not self.listbox_dropped: self.show_hide_listbox()

    def listbox_item_select_event(self, event):
        # Set selected row as text entry value
        self.text_entry.delete(0, END)
        if self.get_listbox_select():
            self.text_entry.insert(0, self.get_listbox_select()[1])
            if self.on_change_method: self.on_change_method()
