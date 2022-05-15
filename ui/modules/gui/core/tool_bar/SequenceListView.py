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

import threading
import time
from threading import Thread
from tkinter import StringVar, PhotoImage, Button, Entry, Listbox, Scrollbar, N, S, E, W, END, CENTER, DISABLED, NORMAL, \
    Canvas, Label, Spinbox
from tkinter.font import Font

from ui.modules.gui.core.custom_widget.Tooltip import Tooltip
from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from ui.Ui import Ui
from ui.modules.gui.core.assets import Base64Imgs
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from ui.modules.gui.core.assets.model.ToolBarModel import ToolBarModel


class SequenceListView(CoreModel, GUIModel, ToolBarModel):

    def __init__(self):
        self.delay_var = StringVar()
        self.loop_var = StringVar()
        self.rename_var = StringVar(GUIModel.root)
        self.loop_var = StringVar()

        self.delay_var.trace("w", lambda *args: self.delay_entry_character_limit())
        self.rename_var.trace("w", lambda *args: self.rename_var_character_limit())
        self.hold_selection = None

        self.delete_icon = PhotoImage(data=Base64Imgs.cross)
        self.edit_icon = PhotoImage(data=Base64Imgs.edit)
        self.run_seq_icon = PhotoImage(data=Base64Imgs.run_sequence)
        self.pause_icon = PhotoImage(data=Base64Imgs.pause)
        self.stop_icon = PhotoImage(data=Base64Imgs.stop)
        self.resume_icon = PhotoImage(data=Base64Imgs.resume)
        self.restart_icon = PhotoImage(data=Base64Imgs.restart)
        self.hourglass_icon = PhotoImage(data=Base64Imgs.hourglass)
        self.loop_icon = PhotoImage(data=Base64Imgs.cycle)

        self.delete_button = Button(GUIModel.root, image=self.delete_icon, borderwidth=0, command=self.delete_item)
        self.rename_button = Button(GUIModel.root, image=self.edit_icon, borderwidth=0, command=self.rename_item)
        self.delay_canvas = Canvas(GUIModel.root, width=15, height=25)
        self.delay_canvas.create_image((3, 5), image=self.hourglass_icon, anchor='nw')

        self.delay_entry = Entry(GUIModel.root, borderwidth=0, width=5, textvariable=self.delay_var, justify=CENTER)
        Tooltip(self.delay_entry, "Set delay of every single step")
        self.delay_entry.bind('<Delete>', self.delay_entry_delete_event)
        self.run_seq_button = Button(GUIModel.root, image=self.run_seq_icon, borderwidth=0, command=self.run_sequence)

        self.loop_canvas = Canvas(GUIModel.root, width=22, height=25)
        self.loop_canvas.create_image((3, 5), image=self.loop_icon, anchor='nw')

        self.loop_spinbox = Spinbox(GUIModel.root, textvariable=self.loop_var, width=5, justify=CENTER, borderwidth=0,
                                    highlightthickness=0)
        Tooltip(self.loop_spinbox, "Set number of repeating, type \"INF\" for infinity loop")
        self.loop_spinbox.bind("<MouseWheel>", self.spinbox_mouse_wheel_event)
        self.loop_var.trace("w", lambda *args: self.loop_widget_update())

        self.pause_running_button = Button(GUIModel.root, image=self.pause_icon, borderwidth=0,
                                           command=self.suspend_running)
        self.stop_running_button = Button(GUIModel.root, image=self.stop_icon, borderwidth=0, command=self.stop_running)
        self.resume_running_button = Button(GUIModel.root, image=self.resume_icon, borderwidth=0,
                                            command=self.resume_running)
        self.restart_running_button = Button(GUIModel.root, image=self.restart_icon, borderwidth=0,
                                             command=self.restart_running)
        self.loop_label = Label(GUIModel.root)
        self.edit_name_entry = Entry(GUIModel.root, textvariable=self.rename_var, borderwidth=0, justify=CENTER)
        self.edit_name_entry.bind('<Return>', self.confirm_renaming)
        self.edit_name_entry.bind('<Escape>', self.storno_renaming)
        self.name_entry_font = Font(font=self.edit_name_entry["font"])
        self.listbox = Listbox(GUIModel.root, borderwidth=0, highlightthickness=0, activestyle="none",
                               selectbackground="#f6e81d", selectforeground="Black", justify=CENTER,
                               exportselection=False)
        self.listbox.bind('<Escape>', self.storno_renaming)
        self.listbox.bind('<Delete>', self.delete_event)
        self.listbox.bind('<F2>', self.rename_event)
        self.listbox.bind('<<ListboxSelect>>', self.select_event)
        self.scrollbar = Scrollbar(GUIModel.root, command=self.listbox.yview, borderwidth=0)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.framework = Framework()
        self.ui = Ui()
        self.items = 0
        self.listbox_data = []
        self.renaming_in_progress = False
        self.loops = 0
        self.loops_index = 0
        self.infinity = False
        self.delay = None

    def spinbox_mouse_wheel_event(self, event):
        # Value increment by mouse wheel roll
        if "INFINITY" != self.loop_var.get():
            spin_box_val = int(self.loop_var.get())
            if event.delta > 0:
                spin_box_val += 1
            elif event.delta < 0:
                if spin_box_val > 0 and spin_box_val > self.loops_index:
                    spin_box_val -= 1
            self.loop_var.set(str(spin_box_val))

    def delay_entry_delete_event(self, args):
        self.delay_var.set("")

    def loop_entry_delete_event(self, args):
        self.loop_var.set("")

    def select_event(self, args):
        if self.listbox_data:
            self.enable_control()

    def show(self):
        # Manage main mode view show rank
        self.hide_all()
        # GUIModel.root.focus_set()
        if not ToolBarModel.seq_list_loaded:
            self.load_sequences()
            ToolBarModel.seq_list_loaded = True
        self.hide_all()
        ToolBarModel.row_size = 0
        if ToolBarModel.vertical:
            self.show_buttons_row()
            ToolBarModel.row_size += 1
            self.show_list_box()
        else:
            self.show_list_box()
            ToolBarModel.row_size += 1
            self.show_buttons_row()

    def show_list_box(self):
        # Show list box widget
        # self.listbox.selection_clear(0, END) # Deselect all
        self.listbox.grid(row=ToolBarModel.row_size, columnspan=20, sticky=(N, S, E, W))
        self.listbox.config(height=self.items)

    def show_buttons_row(self):
        # Show main mode buttons
        self.loop_spinbox.config(state=NORMAL)
        self.loop_spinbox.configure(width=5)
        if ToolBarModel.horizontal:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=8)
            self.run_seq_button.grid(row=ToolBarModel.row_size, column=7)
            self.delay_canvas.grid(row=ToolBarModel.row_size, column=6)
            self.delay_entry.grid(row=ToolBarModel.row_size, column=5, padx=3)
            self.loop_canvas.grid(row=ToolBarModel.row_size, column=4)
            self.loop_spinbox.grid(row=ToolBarModel.row_size, column=3, padx=3)
            self.rename_button.grid(row=ToolBarModel.row_size, column=2)
            self.delete_button.grid(row=ToolBarModel.row_size, column=1)
            GUIModel.sequence_view.show_up_down(0)
        else:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=0)
            self.run_seq_button.grid(row=ToolBarModel.row_size, column=1)
            self.delay_canvas.grid(row=ToolBarModel.row_size, column=2)
            self.delay_entry.grid(row=ToolBarModel.row_size, column=3, padx=3)
            self.loop_canvas.grid(row=ToolBarModel.row_size, column=4)
            self.loop_spinbox.grid(row=ToolBarModel.row_size, column=5, padx=3)
            self.rename_button.grid(row=ToolBarModel.row_size, column=6)
            self.delete_button.grid(row=ToolBarModel.row_size, column=7)
            GUIModel.sequence_view.show_up_down(8)

    def show_running(self):
        # Hide all and show running sequence mode widgets
        self.hide_all()
        if ToolBarModel.horizontal:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=7)
            self.stop_running_button.grid(row=ToolBarModel.row_size, column=6)
            self.pause_running_button.grid(row=ToolBarModel.row_size, column=5)
            self.delay_canvas.grid(row=ToolBarModel.row_size, column=4)
            self.delay_entry.grid(row=ToolBarModel.row_size, column=3, padx=3)
            self.loop_canvas.grid(row=ToolBarModel.row_size, column=2)
            self.loop_spinbox.grid(row=ToolBarModel.row_size, column=1)
            self.loop_label.grid(row=ToolBarModel.row_size, column=0, padx=(2, 0))
        else:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=0)
            self.stop_running_button.grid(row=ToolBarModel.row_size, column=1)
            self.pause_running_button.grid(row=ToolBarModel.row_size, column=2)
            self.delay_canvas.grid(row=ToolBarModel.row_size, column=3)
            self.delay_entry.grid(row=ToolBarModel.row_size, column=4, padx=3)
            self.loop_canvas.grid(row=ToolBarModel.row_size, column=5)
            self.loop_label.grid(row=ToolBarModel.row_size, column=6)
            self.loop_spinbox.grid(row=ToolBarModel.row_size, column=7, padx=(0, 2))

    def show_suspended_running(self):
        # Hide all and show suspended run mode widgets
        self.hide_all()
        self.loop_spinbox.config(state=NORMAL)
        if ToolBarModel.horizontal:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=8)
            self.stop_running_button.grid(row=ToolBarModel.row_size, column=7)
            self.restart_running_button.grid(row=ToolBarModel.row_size, column=6)
            self.resume_running_button.grid(row=ToolBarModel.row_size, column=5)
            self.delay_canvas.grid(row=ToolBarModel.row_size, column=4)
            self.delay_entry.grid(row=ToolBarModel.row_size, column=3, padx=3)
            self.loop_canvas.grid(row=ToolBarModel.row_size, column=2)
            self.loop_spinbox.grid(row=ToolBarModel.row_size, column=1)
            self.loop_label.grid(row=ToolBarModel.row_size, column=0, padx=(2, 0))
        else:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=0)
            self.stop_running_button.grid(row=ToolBarModel.row_size, column=1)
            self.restart_running_button.grid(row=ToolBarModel.row_size, column=2)
            self.resume_running_button.grid(row=ToolBarModel.row_size, column=3)
            self.delay_canvas.grid(row=ToolBarModel.row_size, column=4)
            self.delay_entry.grid(row=ToolBarModel.row_size, column=5, padx=3)
            self.loop_canvas.grid(row=ToolBarModel.row_size, column=6)
            self.loop_label.grid(row=ToolBarModel.row_size, column=7)
            self.loop_spinbox.grid(row=ToolBarModel.row_size, column=8, padx=(0, 2))

    def hide_all(self):
        # Hide all widgets of sequence list view
        GUIModel.main_view.core_button.grid_forget()
        self.delete_button.grid_forget()
        self.rename_button.grid_forget()
        self.delay_entry.grid_forget()
        self.run_seq_button.grid_forget()
        self.listbox.grid_forget()
        self.delay_canvas.grid_forget()
        self.loop_canvas.grid_forget()
        self.loop_spinbox.grid_forget()
        self.edit_name_entry.grid_forget()
        GUIModel.sequence_view.hide_up_down()
        self.pause_running_button.grid_forget()
        self.stop_running_button.grid_forget()
        self.resume_running_button.grid_forget()
        self.restart_running_button.grid_forget()
        self.loop_spinbox.grid_forget()
        self.loop_label.grid_forget()

    def hide_all_instead_of_list_box(self):
        # Hide all widgets of sequence list view instead of list box
        GUIModel.main_view.core_button.grid_forget()
        self.delete_button.grid_forget()
        self.rename_button.grid_forget()
        self.delay_entry.grid_forget()
        self.run_seq_button.grid_forget()
        self.delay_canvas.grid_forget()
        self.loop_canvas.grid_forget()
        self.loop_spinbox.grid_forget()
        self.edit_name_entry.grid_forget()
        GUIModel.sequence_view.hide_up_down()
        self.pause_running_button.grid_forget()
        self.stop_running_button.grid_forget()
        self.resume_running_button.grid_forget()
        self.restart_running_button.grid_forget()
        self.loop_spinbox.grid_forget()
        self.loop_label.grid_forget()

    def show_base(self):
        # Set main mode view as vertical and horizontal method and call
        ToolBarModel.current_horizontal_method = self.show
        ToolBarModel.current_vertical_method = self.show
        GUIModel.main_view.change_gui_orientation()
        GUIModel.main_view.place_to_saved_edge()

    def show_rename(self):
        # Show rename mode by clicking on pencil button
        ToolBarModel.current_horizontal_method = self.show_rename
        ToolBarModel.current_vertical_method = None
        self.hide_all()
        if ToolBarModel.horizontal:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=1)
            self.edit_name_entry.grid(row=ToolBarModel.row_size, column=0)
        else:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=0)
            self.edit_name_entry.grid(row=ToolBarModel.row_size, column=1)

    def set_running_mode_view(self):
        # Set running sequence mode and place gui to saved position
        self.show_running()
        if len(self.loop_var.get()) < 10:
            self.loop_spinbox.configure(width=len(self.loop_var.get()))
        elif len(self.loop_var.get()) > 10:
            self.loop_spinbox.configure(width=10)
        elif len(self.loop_var.get()) < 2:
            self.loop_spinbox.configure(width=2)
        self.loop_spinbox.config(state=DISABLED)
        GUIModel.main_view.place_to_saved_edge()

    def reload_list(self):
        # Hide all widgets of sequence list view, reload content of list box and than show main mode
        self.hide_all()
        self.load_sequences()
        self.show()

    def load_sequences(self):
        # Empty list box widget and load content
        self.listbox.delete(0, 'end')
        self.listbox_data = []
        sequences = self.framework.databases.get_all_current_entity("SEQUENCES")
        conditions = self.framework.databases.get_all_current_entity("CONDITIONS")
        if sequences and sequences != MetadataEnum.ERROR:
            if isinstance(sequences, list):
                self.listbox_data.extend(sequences)
                for one in sequences: self.listbox.insert(END, one[1])
                self.items = len(sequences)
                if self.items > 20: self.items = 20
        if conditions and conditions != MetadataEnum.ERROR:
            if isinstance(conditions, list):
                self.listbox_data.extend(conditions)
                for one in conditions: self.listbox.insert(END, one[1])
                self.items = len(self.listbox_data)
                if self.items > 20: self.items = 20
        if not len(self.listbox_data): self.listbox.insert(END, "Nothing to show")
        self.disable_control()

    def disable_control(self):
        self.run_seq_button.config(state=DISABLED)
        self.rename_button.config(state=DISABLED)
        self.delete_button.config(state=DISABLED)

    def enable_control(self):
        self.run_seq_button.config(state=NORMAL)
        self.rename_button.config(state=NORMAL)
        self.delete_button.config(state=NORMAL)

    def get_selected_item(self):
        # Get selected row of list box widget
        if self.listbox_data:
            return self.listbox_data[self.listbox.curselection()[0]]
        else:
            return False

    def delete_event(self, args):
        # Delete event
        self.delete_item()

    def delete_item(self):
        # Get selected row and call delete in user database by identifiers
        that_index = self.get_selected_item()
        if that_index:
            self.hold_selection = self.listbox.curselection()[0]
            if self.framework.sequences_support.is_sequence(that_index[0]):
                if chr(58) in that_index[0]:
                    seq_code = that_index[0]
                    seq_code = seq_code[seq_code.index(chr(58)) + 1:]
                else:
                    seq_code = that_index[0]
                self.framework.databases.delete_sequence(that_index, seq_code)
            else:
                self.framework.databases.delete_condition(that_index, that_index[0])
            self.load_sequences()
            self.reload_list()
            if self.listbox_data:
                if self.hold_selection + 1 <= len(self.listbox_data):
                    self.listbox.select_set(self.hold_selection)
                else:
                    self.listbox.select_set(len(self.listbox_data) - 1)
                self.enable_control()
            GUIModel.main_view.place_to_saved_edge()

    def rename_event(self, args):
        # Rename event
        self.rename_item()

    def rename_item(self):
        # Show name in text entry widget
        select = self.get_selected_item()
        if select:
            self.hold_selection = self.listbox.curselection()[0]
            self.renaming_in_progress = True
            self.show_rename()
            self.rename_var.set(select[1])
            self.edit_name_entry.configure(width=50)
            self.edit_name_entry.focus()
            GUIModel.main_view.place_to_saved_edge()

    def confirm_renaming(self, args):
        # Is bind to Enter key, get selected row of list box and update row in user database
        if self.renaming_in_progress and self.rename_var.get():
            select = self.get_selected_item()
            if self.framework.sequences_support.is_sequence(select[0]):
                self.framework.databases.update_line_in_sequence_table([select[0], self.rename_var.get()])
                self.storno_renaming(args)
            else:
                self.framework.databases.update_line_in_conditions_table([select[0], self.rename_var.get()])
            self.reload_list()
            self.listbox.select_set(self.hold_selection)
            self.enable_control()

    def storno_renaming(self, args):
        # Is bind to Esc key, set main mode to all current method
        if self.renaming_in_progress:
            ToolBarModel.current_horizontal_method = self.show
            ToolBarModel.current_vertical_method = self.show
            GUIModel.main_view.change_gui_orientation()
            GUIModel.main_view.place_to_saved_edge()
            self.renaming_in_progress = False

    def rename_var_character_limit(self):
        # Kerning calculation checking if width of name text is not bigger than 280px
        ind = 0
        while self.name_entry_font.measure(self.rename_var.get()) > 280:
            self.rename_var.set(self.rename_var.get()[0:len(self.rename_var.get()) - ind])
            ind += 1

    def delay_entry_character_limit(self):
        # Checking if length of text entry widget is not longer than 4 chars
        if len(self.delay_var.get()) > 4: self.delay_var.set(self.delay_var.get()[0:4])

    def loop_widget_update(self):
        # Set spinbox size by his text var to max length 10 chars, min. 2 chars
        if ToolBarModel.suspended_sequence:
            if len(self.loop_var.get()) < 10:
                self.loop_spinbox.configure(width=len(self.loop_var.get()))
            elif len(self.loop_var.get()) > 10:
                self.loop_spinbox.configure(width=10)
            elif len(self.loop_var.get()) < 2:
                self.loop_spinbox.configure(width=2)

    def check_and_append_to_key_list(self):
        # Get selected row from list box widget and append to listeners event list while running recording
        that_index = self.get_selected_item()
        if not GUIModel.turn_off_listeners:
            loops = self.get_loop_value()
            if loops and self.framework.sequences_support.is_sequence(that_index[0]):
                self.framework.listeners.append_loop_sequence_to_key_list(that_index[0], loops)
            elif self.framework.sequences_support.is_sequence(that_index[0]):
                self.framework.listeners.append_sequence_to_key_list(that_index[0])
            elif loops and self.framework.sequences_support.is_condition(that_index[0]):
                self.framework.listeners.append_loop_condition_to_key_list(that_index[0], loops)
            elif self.framework.sequences_support.is_condition(that_index[0]):
                self.framework.listeners.append_condition_to_key_list(that_index[0])
            elif loops and self.framework.sequences_support.is_watcher(that_index[0]):
                self.framework.listeners.append_loop_watcher_to_key_list(that_index[0], loops)
            elif self.framework.sequences_support.is_watcher(that_index[0]):
                self.framework.listeners.append_watcher_to_key_list(that_index[0])
        return that_index

    def start_by_type(self, code, delay):
        # Start sequence by type
        if self.framework.sequences_support.is_sequence(code):
            self.framework.event_player.run_sequence_by_table_name(code, delay)
        elif self.framework.sequences_support.is_condition(code):
            self.framework.event_player.treatment_condition(code, delay)
        elif self.framework.sequences_support.is_watcher(code):
            self.framework.event_player.treatment_watcher(code, delay)

    def get_loop_value(self):
        if self.loop_var.get():
            if "." in self.loop_var.get(): self.loop_var.set(self.loop_var.get()[:self.loop_var.get().index(".")])
            if "," in self.loop_var.get(): self.loop_var.set(self.loop_var.get()[:self.loop_var.get().index(",")])
            if "INF" in self.loop_var.get().upper():
                return "INF"
            else:
                return int(self.loop_var.get())
        else:
            return False

    def prepare_delay_var(self):
        self.delay = None
        if self.delay_var.get():
            self.delay = self.delay_var.get()
            if "," in self.delay:
                self.delay = self.delay.replace(",", ".")
                self.delay_var.set(str(self.delay))
            if " " in self.delay: self.delay = self.delay.replace(" ", "")
            self.delay = float(self.delay)

    def prepare_loop_vars(self):
        self.loops = self.get_loop_value()
        self.infinity = self.loops == "INF"
        if not self.loops or self.infinity: self.loops = 1
        self.loop_var.set(str(self.loops))
        if self.infinity: self.loop_var.set("INFINITY")

    def run_sequence(self):
        # Get delay and loop vars, set up ToolBarModel run vars and call "start_by_type" in cycle in new thread
        self.prepare_delay_var()
        self.prepare_loop_vars()
        that_index = self.check_and_append_to_key_list()
        self.set_running_mode_view()
        GUIModel.main_view.place_to_saved_edge()
        ToolBarModel.running_sequence = True
        ToolBarModel.interrupt_run = False
        ToolBarModel.suspended_sequence = False
        ToolBarModel.restarting = False

        def run_0():
            self.loops_index = 0
            while self.loops_index < self.loops:
                self.loop_label.config(text=str(self.loops_index + 1) + " of")
                if ToolBarModel.interrupt_run: break
                self.start_by_type(that_index[0], self.delay)
                if ToolBarModel.interrupt_run: break
                self.loops_index += 1
                if self.infinity: self.loops += 1
            if not ToolBarModel.restarting: self.show_base()
            ToolBarModel.running_sequence = False

        Thread(target=run_0, name="run_sequence-run_0").start()

    def suspend_running(self):
        self.framework.event_player.suspend_running()
        self.show_suspended_running()

    def resume_running(self):
        # Switch suspended bool to False, show running sequence mode and resume event player
        self.loop_spinbox.config(state=DISABLED)
        self.prepare_delay_var()
        self.prepare_loop_vars()
        if self.loops <= self.loops_index:
            self.loops = self.loops_index + 1
            self.loop_var.set(str(self.loops))
        if self.delay_var.get(): self.framework.event_player.change_delay(float(self.delay_var.get()))
        ToolBarModel.suspended_sequence = False
        ToolBarModel.restarting = False
        self.set_running_mode_view()
        GUIModel.main_view.place_to_saved_edge()
        self.framework.event_player.resume()

    def stop_running(self):
        # Call stop on event handler and set main mode as current display method
        ToolBarModel.interrupt_run = True
        ToolBarModel.suspended_sequence = False
        ToolBarModel.restarting = False
        self.framework.event_player.break_running()
        ToolBarModel.current_horizontal_method = self.show
        ToolBarModel.current_vertical_method = self.show
        GUIModel.main_view.change_gui_orientation()
        GUIModel.main_view.place_to_saved_edge()

    def restart_running(self):
        # Stop running sequence and decide if again run in new thread as loop
        ToolBarModel.interrupt_run = True
        ToolBarModel.suspended_sequence = False
        ToolBarModel.restarting = True
        self.framework.event_player.break_running()
        while ToolBarModel.running_sequence: time.sleep(0.01)
        self.run_sequence()
        ToolBarModel.restarting = False
