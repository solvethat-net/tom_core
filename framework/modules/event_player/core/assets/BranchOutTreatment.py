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

import time

from mouse import LEFT, DOWN, UP, RIGHT
from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from framework.modules.event_player.core.model.PlayerModel import PlayerModel
from ui.Ui import Ui


class BranchOutTreatment(PlayerModel):

    def __init__(self, parent):
        self.parent = parent
        self.framework = Framework()
        self.ui = Ui()

    def true_cause(self, event, check_result, np_arr):
        # Decide if end running sequence or run custom process
        if event:
            if event == MetadataEnum.END:
                self.end_event()
            elif event == MetadataEnum.MOUSE_LEFT:
                self.mouse_event(check_result, np_arr, LEFT)
            elif event == MetadataEnum.MOUSE_RIGHT:
                self.mouse_event(check_result, np_arr, RIGHT)
            else:
                self.decide_what_run(event)

    def false_cause(self, event):
        # Decide if end running sequence or run custom process
        if event:
            if event == MetadataEnum.END:
                self.end_event()
            else:
                self.decide_what_run(event)

    def end_event(self):
        # Stop running sequence
        self.ui.terminal.print_info_log("Stopping sequence")
        Ui().gui.stop_running_sequence()

    def decide_what_run(self, uuid):
        # Decide if run sequence or condition
        if self.framework.sequences_support.is_sequence(uuid):
            self.parent.run_sequence_by_table_name(uuid, PlayerModel.custom_delay)
        elif self.framework.sequences_support.is_condition(uuid):
            self.parent.treatment_condition(uuid, PlayerModel.custom_delay)
        elif self.framework.sequences_support.is_watcher(uuid):
            self.parent.treatment_watcher(uuid, PlayerModel.custom_delay)

    def mouse_event(self, check_result, np_arr, button):
        # Move cursor to center of selected area and click there
        y = check_result[0]
        x = check_result[1]
        x = x + round(np_arr.shape[1] / 2)
        y = y + round(np_arr.shape[0] / 2)
        self.framework.device_control.move_cursor(x, y)
        PlayerModel.condition_mouse_position = [x, y]
        self.framework.device_control.mouse_action(button, DOWN)
        self.framework.device_control.mouse_action(button, UP)

    def treatment_ocr_in_area(self, base64, threshold, image_base64):
        # Find saved base64 image in screen shot of area
        return self.framework.ocr.find_image_in_image(image_base64, base64, threshold)

    def treatment_ocr_full_screen(self, base64, threshold):
        # Find saved base64 image in screen shot of full screen
        return self.framework.ocr.find_image_on_screen(base64, threshold)

    def watcher_method_processing_loop(self, condition):
        # Run while loop processing condition methods by their cause
        while not PlayerModel.break_running:
            if PlayerModel.watcher_check_var:
                self.check_result_treatment(condition[3], PlayerModel.ocr_check_position,
                                            PlayerModel.ocr_check_np_arr, None)
            else:
                self.check_result_treatment(None, None, None, condition[4])

    def watching_loop(self, condition, np_arr):
        # Run while loop that is calling check method
        while not PlayerModel.break_running:
            if not PlayerModel.paused_running:
                PlayerModel.watcher_check_var = self.ocr_check_process(condition[2], np_arr, condition[5], condition[6])

    def check_result_treatment(self, success_event, position, np_arr, fail_event):
        # Decide what cause is ocr check result and process it
        if PlayerModel.custom_delay:
            time.sleep(PlayerModel.custom_delay)
        if success_event:
            self.parent.check_suspend()
            if PlayerModel.break_running:
                return
            self.true_cause(success_event, [position[1], position[0]], np_arr)
        elif fail_event:
            self.parent.check_suspend()
            if PlayerModel.break_running:
                return
            self.false_cause(fail_event)

    def ocr_check_process(self, base64, np_arr, threshold, position):
        # Process condition or watcher
        # Compare saved base64 with new one from same area or find on full screen
        def set_player_model_vars(check_result_to_set, np_arr_arg):
            # Set up PlayerModel vars with args
            PlayerModel.ocr_check_position = check_result_to_set
            PlayerModel.ocr_check_np_arr = np_arr_arg

        if position:
            x2 = position[0] + np_arr.shape[1]
            y2 = position[1] + np_arr.shape[0]
            captured_base64 = self.framework.screen_capturer.capture_area(position[0], position[1], x2, y2)
            if threshold == 1:
                if captured_base64 == base64.encode('ascii'):
                    set_player_model_vars([position[0], position[1]], np_arr)
                    return True
                else:
                    return False
            else:
                check_result = self.framework.ocr.find_image_in_image(captured_base64, base64, threshold)
                if check_result:
                    check_result[0] = check_result[0] + position[0]
                    check_result[1] = check_result[1] + position[1]
                    set_player_model_vars(check_result, np_arr)
                    return True
                else:
                    return False
        else:
            check_result = self.framework.ocr.find_image_on_screen(base64, threshold)
            if check_result:
                set_player_model_vars(check_result, np_arr)
                return True
            else:
                return False
