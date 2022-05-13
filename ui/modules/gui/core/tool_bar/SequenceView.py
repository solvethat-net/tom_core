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

from threading import Thread
from tkinter import PhotoImage, Button

from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from process.Process import Process
from ui.modules.gui.core.area_selector.AreaSelector import AreaSelector
from ui.modules.gui.core.assets import Base64Imgs
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from ui.modules.gui.core.assets.model.ToolBarModel import ToolBarModel


class SequenceView(CoreModel, ToolBarModel, GUIModel):

    def __init__(self):
        self.process = Process()
        self.framework = Framework()

        self.recording_icon = PhotoImage(data=Base64Imgs.recording)
        self.stop_keyboard_icon = PhotoImage(data=Base64Imgs.stop_keyboard)
        self.stop_mouse_icon = PhotoImage(data=Base64Imgs.stop_mouse)
        self.up_icon = PhotoImage(data=Base64Imgs.up)
        self.down_icon = PhotoImage(data=Base64Imgs.down)
        self.keyboard_icon = PhotoImage(data=Base64Imgs.keyboard)
        self.mouse_icon = PhotoImage(data=Base64Imgs.mouse)
        self.save_icon = PhotoImage(data=Base64Imgs.save)
        self.kill_recording_icon = PhotoImage(data=Base64Imgs.cross)
        self.branch_out_icon = PhotoImage(data=Base64Imgs.branch_out)
        self.watcher_icon = PhotoImage(data=Base64Imgs.watcher)

        self.recording_button = Button(GUIModel.root, command=self.start_recording, image=self.recording_icon,
                                       borderwidth=0)
        self.stop_keyboard_button = Button(GUIModel.root, command=self.stop_keyboard_recording,
                                           image=self.stop_keyboard_icon, borderwidth=0)
        self.stop_mouse_button = Button(GUIModel.root, command=self.stop_mouse_recording, image=self.stop_mouse_icon,
                                        borderwidth=0)
        self.up_button = Button(GUIModel.root, command=self.up_btn_event, image=self.up_icon, borderwidth=0)
        self.down_button = Button(GUIModel.root, command=self.down_btn_event, image=self.down_icon, borderwidth=0)
        self.keyboard_button = Button(GUIModel.root, command=self.start_keyboard_recording, image=self.keyboard_icon,
                                      borderwidth=0)
        self.mouse_button = Button(GUIModel.root, command=self.start_mouse_recording, image=self.mouse_icon,
                                   borderwidth=0)
        self.save_button = Button(GUIModel.root, command=self.save_recording, image=self.save_icon, borderwidth=0)
        self.kill_recording_button = Button(GUIModel.root, command=self.kill_recording, image=self.kill_recording_icon,
                                            borderwidth=0)
        self.branch_out_button = Button(GUIModel.root, command=self.condition_event, image=self.branch_out_icon,
                                        borderwidth=0)
        self.watcher_button = Button(GUIModel.root, command=self.watcher_event, image=self.watcher_icon, borderwidth=0)

    def show(self):
        # Show main mode or recording mode
        if not GUIModel.turn_off_listeners:
            ToolBarModel.current_horizontal_method = self.show_recording
            ToolBarModel.current_vertical_method = None
            GUIModel.main_view.change_gui_orientation()
        else:
            ToolBarModel.current_horizontal_method = self.show_base
            ToolBarModel.current_vertical_method = None
            GUIModel.main_view.change_gui_orientation()

    def show_up_down(self, col):
        # Show up and down buttons by actual position
        # If is gui on top of the screen, show down for dropping down list
        self.down_button.grid_forget()
        self.up_button.grid_forget()
        if ToolBarModel.vertical:
            if ToolBarModel.list_is_dropped:
                self.up_button.grid(row=ToolBarModel.row_size, column=col)
            else:
                self.down_button.grid(row=ToolBarModel.row_size, column=col)
        else:
            if ToolBarModel.list_is_dropped:
                self.down_button.grid(row=ToolBarModel.row_size, column=col)
            else:
                self.up_button.grid(row=ToolBarModel.row_size, column=col)

    def show_base(self):
        # Show main mode of sequence view
        if ToolBarModel.horizontal:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=4)
            self.recording_button.grid(row=ToolBarModel.row_size, column=3)
            self.branch_out_button.grid(row=ToolBarModel.row_size, column=2)
            self.watcher_button.grid(row=ToolBarModel.row_size, column=1)
            self.show_up_down(0)
        else:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=0)
            self.recording_button.grid(row=ToolBarModel.row_size, column=1)
            self.branch_out_button.grid(row=ToolBarModel.row_size, column=2)
            self.watcher_button.grid(row=ToolBarModel.row_size, column=3)
            self.show_up_down(10)

    def show_recording(self):
        # Show recording mode
        if ToolBarModel.horizontal:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=7)

            if GUIModel.capturing_keyboard_on:
                self.stop_keyboard_button.grid(row=ToolBarModel.row_size, column=6)
            else:
                self.keyboard_button.grid(row=ToolBarModel.row_size, column=6)

            if GUIModel.capturing_mouse_on:
                self.stop_mouse_button.grid(row=ToolBarModel.row_size, column=5)
            else:
                self.mouse_button.grid(row=ToolBarModel.row_size, column=5)

            self.branch_out_button.grid(row=ToolBarModel.row_size, column=4)
            self.watcher_button.grid(row=ToolBarModel.row_size, column=3)

            self.save_button.grid(row=ToolBarModel.row_size, column=2)
            self.kill_recording_button.grid(row=ToolBarModel.row_size, column=1)
            self.show_up_down(0)
        else:
            GUIModel.main_view.core_button.grid(row=ToolBarModel.row_size, column=0)

            if GUIModel.capturing_keyboard_on:
                self.stop_keyboard_button.grid(row=ToolBarModel.row_size, column=1)
            else:
                self.keyboard_button.grid(row=ToolBarModel.row_size, column=1)

            if GUIModel.capturing_mouse_on:
                self.stop_mouse_button.grid(row=ToolBarModel.row_size, column=2)
            else:
                self.mouse_button.grid(row=ToolBarModel.row_size, column=2)

            self.branch_out_button.grid(row=ToolBarModel.row_size, column=3)
            self.watcher_button.grid(row=ToolBarModel.row_size, column=4)
            self.save_button.grid(row=ToolBarModel.row_size, column=5)
            self.kill_recording_button.grid(row=ToolBarModel.row_size, column=6)
            self.show_up_down(7)
        GUIModel.main_view.place_to_saved_edge()

    def show_seq_list(self):
        # Decide if show main or suspended mode of sequence list view
        self.hide_all()
        if ToolBarModel.suspended_sequence:
            ToolBarModel.current_horizontal_method = GUIModel.sequence_list_view.show_suspended_running
            ToolBarModel.current_vertical_method = None
        else:
            ToolBarModel.current_horizontal_method = GUIModel.sequence_list_view.show
            ToolBarModel.current_vertical_method = GUIModel.sequence_list_view.show
            ToolBarModel.list_is_dropped = True
        GUIModel.main_view.change_gui_orientation()
        GUIModel.main_view.place_to_saved_edge()

    def hide_seq_list(self):
        # Hide all widgets of sequence list view and set main mode as current display method
        if ToolBarModel.list_is_dropped:
            GUIModel.sequence_list_view.hide_all()
            ToolBarModel.list_is_dropped = False
            ToolBarModel.current_horizontal_method = self.show
            ToolBarModel.current_vertical_method = None
            GUIModel.main_view.change_gui_orientation()
            GUIModel.main_view.place_to_saved_edge()

    def hide_all(self):
        # Hide all widgets of sequence view
        GUIModel.main_view.core_button.grid_forget()
        self.hide_up_down()
        self.keyboard_button.grid_forget()
        self.mouse_button.grid_forget()
        self.stop_keyboard_button.grid_forget()
        self.stop_mouse_button.grid_forget()
        self.save_button.grid_forget()
        self.kill_recording_button.grid_forget()
        self.branch_out_button.grid_forget()
        self.recording_button.grid_forget()
        self.watcher_button.grid_forget()

    def hide_up_down(self):
        # Hide up and down buttons
        self.up_button.grid_forget()
        self.down_button.grid_forget()

    def down_btn_event(self):
        # Decide if call show or hide of sequence list view
        self.down_button.grid_forget()
        self.up_button.grid_forget()
        if ToolBarModel.vertical:
            ToolBarModel.row_size = 0
            if self.horizontal:
                self.up_button.grid(row=ToolBarModel.row_size, column=0)
            else:
                self.up_button.grid(row=ToolBarModel.row_size, column=10)
            self.show_seq_list()
        else:
            if self.horizontal:
                self.down_button.grid(row=ToolBarModel.row_size, column=0)
            else:
                self.down_button.grid(row=ToolBarModel.row_size, column=10)
            self.hide_seq_list()
        GUIModel.main_view.change_gui_orientation()
        GUIModel.main_view.place_to_saved_edge()

    def up_btn_event(self):
        # Decide if call show or hide of sequence list view
        self.down_button.grid_forget()
        self.up_button.grid_forget()
        if self.vertical:
            ToolBarModel.row_size = 0
            if self.horizontal:
                self.down_button.grid(row=ToolBarModel.row_size, column=0)
            else:
                self.down_button.grid(row=ToolBarModel.row_size, column=10)
            self.hide_seq_list()
        else:
            if self.horizontal:
                self.up_button.grid(row=ToolBarModel.row_size, column=0)
            else:
                self.up_button.grid(row=ToolBarModel.row_size, column=10)
            self.show_seq_list()
            GUIModel.main_view.change_gui_orientation()
            GUIModel.main_view.place_to_saved_edge()

    def start_recording(self):
        # Make turn_off_listeners False as recording indicator and show recording view
        GUIModel.turn_off_listeners = False
        self.framework.listeners.init_key_list()
        self.recording_event()
        self.start_keyboard_recording()
        self.start_mouse_recording()

    def start_keyboard_recording(self):
        # Call start method of keyboard listener, clicking to K in round button
        GUIModel.capturing_keyboard_on = True
        GUIModel.turn_off_listeners = False
        self.framework.listeners.run_key_listener()
        self.recording_event()

    def start_mouse_recording(self):
        # Call start method of mouse listener, clicking to M in round button
        GUIModel.capturing_mouse_on = True
        GUIModel.turn_off_listeners = False
        self.framework.listeners.run_mouse_listener()
        self.recording_event()

    def stop_keyboard_recording(self):
        # Call stop method of keyboard listener, clicking to K in square button
        GUIModel.capturing_keyboard_on = False
        self.recording_event()

    def stop_mouse_recording(self):
        # Call stop method of mouse listener, clicking to M in square button
        GUIModel.capturing_mouse_on = False
        self.recording_event()

    def recording_event(self):
        # Hide all widgets and show recording mode
        self.hide_all()
        ToolBarModel.current_horizontal_method = self.show_recording
        GUIModel.main_view.change_gui_orientation()
        GUIModel.main_view.place_to_saved_edge()

    def save_recording(self):
        # Show main mode and call stopping sequence that save record
        GUIModel.capturing_keyboard_on = False
        GUIModel.capturing_mouse_on = False
        GUIModel.turn_off_listeners = True
        GUIModel.select_x1 = None
        GUIModel.select_y1 = None
        GUIModel.select_x2 = None
        GUIModel.select_y2 = None
        ToolBarModel.current_horizontal_method = self.show_base
        self.hide_all()
        self.show_base()
        self.stop_recording()
        GUIModel.main_view.change_gui_orientation()
        GUIModel.main_view.place_to_saved_edge()

    def kill_recording(self):
        # Show main mode and don't call stopping sequence
        self.framework.listeners.stop_all()
        GUIModel.capturing_keyboard_on = False
        GUIModel.capturing_mouse_on = False
        GUIModel.turn_off_listeners = True
        if GUIModel.area_selector_running:
            GUIModel.area_selector.close_window()
            GUIModel.area_selector = None
            GUIModel.area_selector_running = False
            if GUIModel.post_area_select_treatment:
                GUIModel.post_area_select_treatment.close_event()
                GUIModel.post_area_select_treatment = None
        GUIModel.select_x1 = None
        GUIModel.select_y1 = None
        GUIModel.select_x2 = None
        GUIModel.select_y2 = None
        ToolBarModel.current_horizontal_method = self.show_base
        self.hide_all()
        self.show_base()
        GUIModel.main_view.change_gui_orientation()
        GUIModel.main_view.place_to_saved_edge()

    def record_save(self):
        # Stop mouse and keyboard listeners and save recorded sequence
        self.framework.listeners.stop_all()
        synapse_model = self.framework.listeners.get_recorded_data()
        if len(synapse_model.data) > 1: self.process.current_database.create_new_sequence(synapse_model)
        GUIModel.sequence_list_view.load_sequences()

    def stop_recording(self):
        # Run sequence recording save in new thread
        Thread(target=self.record_save, name="stop_recording-record_save").start()

    def condition_event(self):
        # Run area selector to get data for condition
        if not GUIModel.area_selector_running:
            GUIModel.area_selector = AreaSelector("Condition set up", MetadataEnum.CONDITION)

    def watcher_event(self):
        # Run area selector to get data for watcher loop
        if not GUIModel.area_selector_running:
            GUIModel.area_selector = AreaSelector("Watcher loop set up", MetadataEnum.WATCHER)
