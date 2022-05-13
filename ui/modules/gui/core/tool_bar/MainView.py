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

from tkinter import PhotoImage, Button, Menu

from framework.Framework import Framework
from ui.Ui import Ui
from ui.modules.gui.core.assets import Base64Imgs
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from ui.modules.gui.core.assets.model.ToolBarModel import ToolBarModel


class MainView(GUIModel, ToolBarModel):

    def __init__(self):
        self.framework = Framework()
        self.ui = Ui()

        self.core_logo_icon = PhotoImage(data=Base64Imgs.core_logo)
        self.mic_icon = PhotoImage(data=Base64Imgs.microphone)
        self.mic_on_rec_icon = PhotoImage(data=Base64Imgs.recording_microphone)
        self.seq_icon = PhotoImage(data=Base64Imgs.sequence)
        self.typing_icon = PhotoImage(data=Base64Imgs.typing)

        self.core_button = Button(GUIModel.root, image=self.core_logo_icon, borderwidth=0)
        self.seq_button = Button(GUIModel.root, command=self.seq_button_click, image=self.seq_icon, borderwidth=0)
        self.type_button = Button(GUIModel.root, command=self.type_button_click, image=self.typing_icon, borderwidth=0)
        self.mic_button = Button(GUIModel.root, command=self.mic_button_click, image=self.mic_icon, borderwidth=0)
        self.menu = Menu(GUIModel.root, tearoff=0)
        self.menu.add_command(label="Minimize", command=self.ui.gui.hide_tool_bar_frame)
        self.menu.add_command(label="New...", command=self.ui.gui.new_event)
        self.menu.add_command(label="Open...", command=self.ui.gui.open_event)
        self.menu.add_command(label="End application", command=self.ui.gui.kill_gui)

        self.core_button.bind("<ButtonPress-1>", self.start_move)
        self.core_button.bind("<ButtonRelease-1>", self.stop_move)
        self.core_button.bind("<B1-Motion>", self.on_motion)
        self.core_button.bind("<Button-3>", self.popup_menu)

        ToolBarModel.current_horizontal_method = self.show_base
        ToolBarModel.current_vertical_method = None
        self.load_saved_position()
        self.change_gui_orientation()

    def popup_menu(self, event):
        try:
            self.menu.tk_popup(event.x_root, event.y_root)
        finally:
            self.menu.grab_release()

    def show_base(self):
        # Show main mode of main view
        ToolBarModel.current_horizontal_method = self.show_base
        ToolBarModel.current_vertical_method = None
        if self.horizontal:
            self.core_button.grid(row=ToolBarModel.row_size, column=3)
            self.seq_button.grid(row=ToolBarModel.row_size, column=2)
            self.type_button.grid(row=ToolBarModel.row_size, column=1)
            self.mic_button.grid(row=ToolBarModel.row_size, column=0)
        else:
            self.core_button.grid(row=ToolBarModel.row_size, column=0)
            self.seq_button.grid(row=ToolBarModel.row_size, column=1)
            self.type_button.grid(row=ToolBarModel.row_size, column=2)
            self.mic_button.grid(row=ToolBarModel.row_size, column=3)

    def hide_all(self):
        # Hide all widgets
        self.mic_button.grid_forget()
        self.seq_button.grid_forget()
        self.type_button.grid_forget()

    def hide_all_views(self):
        # Hide all other views
        GUIModel.text_input_view.hide_all()
        GUIModel.sequence_view.hide_seq_list()
        GUIModel.sequence_view.hide_all()
        GUIModel.sequence_list_view.hide_all()

    def core_button_click(self):
        # Decide if go back to main view or hide all and let showed just core button
        if ToolBarModel.first_time:
            self.set_up_edges()
            ToolBarModel.first_time = False
        if ToolBarModel.main_view:
            if ToolBarModel.all_hidden:
                self.show_base()
                ToolBarModel.all_hidden = False
            else:
                self.hide_all()
                ToolBarModel.all_hidden = True
        else:
            self.hide_all_views()
            self.hide_all()
            self.show_base()
            ToolBarModel.all_hidden = False
            ToolBarModel.main_view = True

    def seq_button_click(self):
        # Hide all widgets and show main mode of sequence view
        if ToolBarModel.first_time:
            self.set_up_edges()
            ToolBarModel.first_time = False
        ToolBarModel.main_view = False
        self.hide_all()
        GUIModel.sequence_view.show()
        self.place_to_saved_edge()
        self.set_up_horizontal_and_vertical()

    def type_button_click(self):
        # Hide all widgets and show main mode of typing view
        if ToolBarModel.first_time:
            self.set_up_edges()
            ToolBarModel.first_time = False
        ToolBarModel.main_view = False
        self.hide_all()
        GUIModel.text_input_view.show_base()
        self.place_to_saved_edge()

    def mic_button_click(self):
        # Hide all widgets and show main mode of speech view
        if ToolBarModel.voice_recording:
            ToolBarModel.voice_recording = False
            self.mic_button.configure(image=self.mic_icon)
            self.framework.listeners.stop_speech_listener()
        else:
            ToolBarModel.voice_recording = True
            self.mic_button.configure(image=self.mic_on_rec_icon)
            self.framework.listeners.run_speech_listener()

    def change_gui_orientation(self):
        # Call current display method by actual position
        if not ToolBarModel.all_hidden:
            ToolBarModel.row_size = 0
            if ToolBarModel.vertical:
                if ToolBarModel.current_horizontal_method: ToolBarModel.current_horizontal_method()
                if ToolBarModel.current_vertical_method: ToolBarModel.current_vertical_method()
            else:
                if ToolBarModel.current_vertical_method: ToolBarModel.current_vertical_method()
                if ToolBarModel.current_horizontal_method: ToolBarModel.current_horizontal_method()

    def load_saved_position(self):
        # Place gui to saved position on start of application
        GUIModel.root.geometry("+%s+%s" % (0, 0))
        # position_x = self.framework.current_database.get_current_config_value("x_pos")
        # position_y = self.framework.current_database.get_current_config_value("y_pos")
        # self.geometry("+%s+%s" % (int(position_x), int(position_y)))
        GUIModel.root.update()
        self.set_up_horizontal_and_vertical()
        self.set_up_gui_model()

    def set_up_edges(self):
        # Set position variables by actual position
        GUIModel.root.update()
        position_x = self.framework.databases.get_current_config_value("x_pos")
        position_y = self.framework.databases.get_current_config_value("y_pos")
        ToolBarModel.right_edge = int(position_x) + GUIModel.root.winfo_width()
        ToolBarModel.bottom_edge = int(position_y) + GUIModel.root.winfo_height()

    def place_to_saved_edge(self):
        # Place gui to saved position
        if ToolBarModel.horizontal and ToolBarModel.vertical:
            GUIModel.root.update()
            x = ToolBarModel.right_edge - GUIModel.root.winfo_width()
            GUIModel.root.geometry("+%s+%s" % (x, GUIModel.y_pos))

        if not ToolBarModel.horizontal and not ToolBarModel.vertical:
            GUIModel.root.update()
            y = ToolBarModel.bottom_edge - GUIModel.root.winfo_height()
            GUIModel.root.geometry("+%s+%s" % (GUIModel.x_pos, y))

        if ToolBarModel.horizontal and not ToolBarModel.vertical:
            GUIModel.root.update()
            x = ToolBarModel.right_edge - GUIModel.root.winfo_width()
            y = ToolBarModel.bottom_edge - GUIModel.root.winfo_height()
            GUIModel.root.geometry("+%s+%s" % (x, y))

        self.set_up_gui_model()

    def set_up_horizontal_and_vertical(self):
        # Set horizontal and vertical variables by actual gui position
        change = False
        if GUIModel.root.winfo_x() + GUIModel.root.winfo_width() > self.ui.gui.width_by_percent(GUIModel.root, 80):
            if not ToolBarModel.horizontal:
                ToolBarModel.horizontal = True
                change = True
        elif GUIModel.root.winfo_x() < self.ui.gui.width_by_percent(GUIModel.root, 20):
            if ToolBarModel.horizontal:
                ToolBarModel.horizontal = False
                change = True
        if GUIModel.root.winfo_y() < self.ui.gui.height_by_percent(GUIModel.root, 15):
            if not ToolBarModel.vertical:
                ToolBarModel.vertical = True
                change = True
        elif GUIModel.root.winfo_y() + GUIModel.root.winfo_height() > self.ui.gui.height_by_percent(GUIModel.root, 85):
            if ToolBarModel.vertical:
                ToolBarModel.vertical = False
                change = True
        if change: self.change_gui_orientation()

    def get_mouse_position(self, event):
        # Get actual mouse position
        delta_x = event.x - GUIModel.root.x
        delta_y = event.y - GUIModel.root.y
        x = GUIModel.root.winfo_x() + delta_x
        y = GUIModel.root.winfo_y() + delta_y
        return [x, y]

    def start_move(self, event):
        # gui is moving by dragging core button
        GUIModel.root.x = event.x
        GUIModel.root.y = event.y
        ToolBarModel.mouse_position = self.get_mouse_position(event)

    def stop_move(self, event):
        # Decide if save gui new position or process core button click event
        position = self.get_mouse_position(event)
        if position[0] == ToolBarModel.mouse_position[0] and position[1] == ToolBarModel.mouse_position[1]:
            self.core_button_click()
            self.place_to_saved_edge()
        else:
            ToolBarModel.mouse_position = self.get_mouse_position(event)
            ToolBarModel.right_edge = GUIModel.root.winfo_rootx() + GUIModel.root.winfo_width()
            ToolBarModel.bottom_edge = GUIModel.root.winfo_rooty() + GUIModel.root.winfo_height()
            self.framework.databases.save_configuration("x_pos", GUIModel.root.winfo_rootx())
            self.framework.databases.save_configuration("y_pos", GUIModel.root.winfo_rooty())
            self.set_up_gui_model()
            GUIModel.root.x = None
            GUIModel.root.y = None

    def on_motion(self, event):
        # Setting position while moving with gui
        position = self.get_mouse_position(event)
        GUIModel.root.geometry("+%s+%s" % (position[0], position[1]))
        self.set_up_horizontal_and_vertical()

    def set_up_gui_model(self):
        # Setting model variables
        GUIModel.root.update()
        GUIModel.width = GUIModel.root.winfo_width()
        GUIModel.height = GUIModel.root.winfo_height()
        GUIModel.x_pos = GUIModel.root.winfo_rootx()
        GUIModel.y_pos = GUIModel.root.winfo_rooty()
