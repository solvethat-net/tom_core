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

from tkinter import Toplevel, PhotoImage, Button, DISABLED, NORMAL, Checkbutton, Label, Spinbox, StringVar, BooleanVar
from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from process.Process import Process
from ui.Ui import Ui
from ui.modules.gui.core.assets import Base64Imgs
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from ui.modules.gui.core.custom_widget.Combobox import Combobox


class BranchOutWindow(CoreModel, GUIModel):

    def __init__(self, title, condition_enum):
        self.framework = Framework()
        self.process = Process()
        self.ui = Ui()
        self.condition_enum = condition_enum
        self.window = Toplevel(GUIModel.root)
        self.window.title(title)
        self.window.geometry("360x180")
        self.window.protocol("WM_DELETE_WINDOW", self.close_event)
        win_pos_start_x = self.ui.gui.width_by_percent(GUIModel.root, 50) - 188
        win_pos_start_y = self.ui.gui.height_by_percent(GUIModel.root, 50) - 180
        self.window.geometry("+%s+%s" % (win_pos_start_x, win_pos_start_y))
        self.window.resizable(False, True)

        self.window.iconbitmap(default=Base64Imgs.core_logo_small)
        self.window.iconphoto(False, PhotoImage(data=Base64Imgs.core_logo_small))
        self.combobox_data = self.prepare_combobox_data()
        self.false_label = Label(self.window, text="Fail")
        self.true_label = Label(self.window, text="Success")
        self.tolerance_label = Label(self.window, text="Match threshold")
        self.false_combobox = Combobox(self.window, self.change_state_of_done_button, self.combobox_data)
        self.combobox_data = self.combobox_data[:2] + [
            (MetadataEnum.MOUSE_LEFT, "Left click on selection")] + [
                                 (MetadataEnum.MOUSE_RIGHT, "Right click on selection")] + self.combobox_data[2:]
        self.true_combobox = Combobox(self.window, self.change_state_of_done_button, self.combobox_data)
        self.true_combobox.bind_resize_parent_method(self.set_height_by_content)
        self.false_combobox.bind_resize_parent_method(self.set_height_by_content)
        self.done_button = Button(self.window, text="Confirm", bg='#309337', fg='white', borderwidth=0,
                                  command=self.done_event, state=DISABLED)
        self.only_selected_area_var = BooleanVar()
        self.only_selected_area_var.set(True)
        self.only_selected_area_checkbox = Checkbutton(self.window, variable=self.only_selected_area_var,
                                                       text='Search only within selected area', onvalue=True,
                                                       offvalue=False)
        self.threshold_spinbox_var = StringVar()
        # TODO pokud je prah 100% tak nelze mit odoznaceny checkbox search only within selected area
        self.threshold_spinbox_var.trace("w", self.check_entry_value)
        self.threshold_spinbox = Spinbox(self.window, from_=1, to=100, width=6, textvariable=self.threshold_spinbox_var,
                                         command=self.append_percent_char)
        self.threshold_spinbox_var.set("100 %")
        self.threshold_spinbox.bind("<MouseWheel>", self.spinbox_mouse_wheel_event)
        self.threshold_spinbox.bind('<Return>', self.check_entry_value)

        self.true_label.grid(row=0, column=0, padx=(26, 0), pady=(10, 3), sticky='W')
        self.true_combobox.grid(row=1, column=0, columnspan=5, padx=(29, 0), pady=(3, 5))
        self.false_label.grid(row=2, column=0, padx=(26, 0), pady=(5, 3), sticky='W')
        self.false_combobox.grid(row=3, column=0, columnspan=5, padx=(29, 0), pady=(3, 5))
        self.only_selected_area_checkbox.grid(row=4, column=0, padx=(25, 0), pady=(15, 5), sticky='W')
        self.threshold_spinbox.grid(row=5, column=0, padx=(29, 0), pady=(5, 5), sticky='W')
        self.tolerance_label.grid(row=5, column=0, padx=(115, 0))
        self.done_button.grid(row=6, column=0, columnspan=5, padx=(29, 0), pady=(15, 10), sticky='E,W')

        self.set_height_by_content()

    def check_entry_value(self, *args):
        # Check entered value and append percent symbol
        spin_box_val = self.threshold_spinbox_var.get()
        spin_box_val = spin_box_val.replace(" ", "")
        if "%" in spin_box_val:
            spin_box_val = spin_box_val[:spin_box_val.index("%")]
            if spin_box_val and 1 <= int(spin_box_val) <= 100:
                self.threshold_spinbox_var.set(spin_box_val + " %")
            else:
                self.threshold_spinbox_var.set("100 %")
        else:
            self.threshold_spinbox_var.set(spin_box_val + " %")

    def append_percent_char(self):
        # Check if append percent symbol
        spin_box_val = self.threshold_spinbox_var.get()
        spin_box_val = spin_box_val.replace(" ", "")
        if "%" in spin_box_val: spin_box_val = spin_box_val[:spin_box_val.index("%")]
        self.threshold_spinbox_var.set(spin_box_val + " %")

    def spinbox_mouse_wheel_event(self, event):
        # Value increment by mouse wheel roll
        spin_box_val = int(self.threshold_spinbox_var.get()[:len(self.threshold_spinbox_var.get()) - 2])
        if event.delta > 0:
            if spin_box_val < 100: spin_box_val = spin_box_val + 1
        elif event.delta < 0:
            if spin_box_val > 1: spin_box_val = spin_box_val - 1
        self.threshold_spinbox_var.set(str(spin_box_val) + " %")

    def prepare_combobox_data(self):
        # Get all SEQUENCES and CONDITIONS tables content from DB
        combobox_data = [("", ""), (MetadataEnum.END, "End running sequence")]
        sequences = self.framework.databases.get_all_current_entity("SEQUENCES")
        conditions = self.framework.databases.get_all_current_entity("CONDITIONS")
        if sequences and sequences != MetadataEnum.ERROR:
            if isinstance(sequences, list): combobox_data.extend(sequences)
        if conditions and conditions != MetadataEnum.ERROR:
            if isinstance(conditions, list): combobox_data.extend(conditions)
        return combobox_data

    def set_height_by_content(self):
        # Add up all widgets and set window height
        self.window.update()
        height = self.true_label.winfo_height() + self.true_combobox.winfo_height() + self.false_label.winfo_height() + self.false_combobox.winfo_height() + self.only_selected_area_checkbox.winfo_height() + self.threshold_spinbox.winfo_height() + self.done_button.winfo_height()
        self.window.geometry(str(self.window.winfo_width()) + "x" + str(height + 100))

    def close_event(self):
        # Destroy window and make area_selector_running false
        self.window.destroy()
        self.window.update()
        GUIModel.area_selector_running = False
        if not GUIModel.capturing_mouse_on and not GUIModel.capturing_keyboard_on:
            GUIModel.select_x1 = None
            GUIModel.select_y1 = None
            GUIModel.select_x2 = None
            GUIModel.select_y2 = None

    def change_state_of_done_button(self):
        # Change state of done button by changing of IF-ELSE combobox
        if self.true_combobox.get_listbox_select() or self.false_combobox.get_listbox_select():
            self.done_button.config(state=NORMAL)
        else:
            self.done_button.config(state=DISABLED)

    def done_event(self):
        # Create IF-ELSE indexes save condition to database and append to key list if recording is in progress
        true_value = ""
        false_value = ""
        if self.true_combobox.get_listbox_select():
            true_value = self.true_combobox.get_listbox_select()[0]
            if true_value and isinstance(true_value, MetadataEnum):
                if (GUIModel.capturing_keyboard_on or GUIModel.capturing_mouse_on) and (
                        true_value == MetadataEnum.MOUSE_LEFT or true_value == MetadataEnum.MOUSE_RIGHT):
                    GUIModel.do_not_capture_next_mouse_click = True
                true_value = true_value.name
        if self.false_combobox.get_listbox_select():
            false_value = self.false_combobox.get_listbox_select()[0]
            if false_value and isinstance(false_value, MetadataEnum): false_value = false_value.name
        if GUIModel.base64_image:
            GUIModel.base64_image = str(GUIModel.base64_image)[2:len(str(GUIModel.base64_image)) - 1]
            threshold = int(self.threshold_spinbox_var.get()[:len(self.threshold_spinbox_var.get()) - 2])
            threshold = threshold / 100
            if threshold == 1.0: threshold = 1
            threshold = str(threshold)
            if self.only_selected_area_var.get():
                position_string = str(GUIModel.select_x1) + " " + str(GUIModel.select_y1)
            else:
                position_string = ""
            if self.condition_enum == MetadataEnum.CONDITION:
                self.process.current_database.create_new_condition(GUIModel.base64_image, true_value, false_value,
                                                                   threshold, position_string)
            elif self.condition_enum == MetadataEnum.WATCHER:
                self.process.current_database.create_new_watcher(GUIModel.base64_image, true_value, false_value,
                                                                 threshold, position_string)
            if not GUIModel.turn_off_listeners:
                self.framework.listeners.append_condition_to_key_list(CoreModel.topic)
            self.window.destroy()
            self.window.update()
            GUIModel.area_selector_running = False
            GUIModel.sequence_list_view.load_sequences()
