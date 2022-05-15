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

import importlib
import inspect
import time
from datetime import datetime
import keyboard
from threading import Lock, Thread
from core_util.LogEnum import LogEnum
from core_util.SynapseModel import SynapseModel
from framework.Framework import Framework
from framework.modules.event_player.core.assets.BranchOutTreatment import BranchOutTreatment
from framework.modules.event_player.core.assets.SynapseModelTreatment import SynapseModelTreatment
from framework.modules.event_player.core.model.PlayerModel import PlayerModel
from ui.Ui import Ui


class Player(PlayerModel):

    def __init__(self):
        self.framework = Framework()
        self.ui = Ui()
        self.model_treatment = SynapseModelTreatment(self)
        self.branch_out_treatment = BranchOutTreatment(self)

    def run_sequence_by_table_name(self, uuid, custom_delay):
        # Get sequence table from database and play events line by line
        PlayerModel.custom_delay = custom_delay
        if not PlayerModel.handler_is_running:
            Thread(target=self.run_stop_handler, name="run_sequence_by_table_name-run_stop_handler").start()
        PlayerModel.paused_running = False
        synapse_model = SynapseModel()
        if self.find_log_enum_in_uuid(uuid):
            seq_name = uuid[uuid.index(chr(58)) + 1:]
            synapse_model.data = self.framework.databases.get_all_sequence_entity(seq_name)
            method = uuid[:uuid.index(chr(58))].split(chr(46))
            self.ui.terminal.print_info_log("Running method " + str(method))
            synapse_model = self.run_process_method_by_log_enum(method, synapse_model)
        else:
            synapse_model.data = self.framework.databases.get_all_sequence_entity(uuid)
            self.ui.terminal.print_info_log("Running sequence " + uuid)
            self.model_treatment.play_synapse_model(synapse_model)
        if not PlayerModel.loop_is_running:
            self.stop_stop_handler_0()
        return synapse_model

    def find_log_enum_in_uuid(self, uuid):
        # Get all LogEnum attributes and compare uuid with them
        attributes = inspect.getmembers(LogEnum, lambda a: not (inspect.isroutine(a)))
        for one in [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]:
            if one[0] != "value" and one[0] != "name":
                if one[1].value[0] in uuid:
                    return True
        return False

    def run_process_method_by_log_enum(self, method, synapse_model):
        # Run process module method with synapse_model argument
        class_name = self.framework.process_support.to_camel_case(method[0])
        object_var = getattr(importlib.import_module("process.modules." + method[0] + chr(46) + class_name), class_name)
        return getattr(object_var(), method[1])(synapse_model)

    def treatment_condition(self, uuid, custom_delay):
        # Select by condition by UUID and pass to process
        PlayerModel.custom_delay = custom_delay
        PlayerModel.break_running = False
        condition = self.framework.databases.get_condition_by_uuid(uuid)
        self.check_suspend()
        if PlayerModel.break_running:
            return
        np_arr = self.framework.process_support.convert_base64_to_numpy_arr(condition[2])
        check_result = self.branch_out_treatment.ocr_check_process(condition[2], np_arr, condition[5], condition[6])
        if check_result:
            self.branch_out_treatment.check_result_treatment(condition[3], PlayerModel.ocr_check_position,
                                                             PlayerModel.ocr_check_np_arr, None)
        else:
            self.branch_out_treatment.check_result_treatment(None, None, None, condition[4])

    def treatment_watcher(self, uuid, custom_delay):
        # Select by watcher by UUID and pass to process
        PlayerModel.custom_delay = custom_delay
        PlayerModel.watcher_check_var = None
        PlayerModel.loop_is_running = True
        if not PlayerModel.handler_is_running:
            Thread(target=self.run_stop_handler, name="treatment_watcher-run_stop_handler").start()
        PlayerModel.paused_running = False
        condition = self.framework.databases.get_condition_by_uuid(uuid)
        np_arr = self.framework.process_support.convert_base64_to_numpy_arr(condition[2])
        # Thread(target=self.branch_out_treatment.watching_loop, args=(condition, np_arr,)).start()
        while not PlayerModel.break_running:
            check_result = self.branch_out_treatment.ocr_check_process(condition[2], np_arr, condition[5], condition[6])
            if check_result and not PlayerModel.paused_running:
                self.branch_out_treatment.check_result_treatment(condition[3], PlayerModel.ocr_check_position,
                                                                 PlayerModel.ocr_check_np_arr, None)
            elif not check_result and not PlayerModel.paused_running:
                self.branch_out_treatment.check_result_treatment(None, None, None, condition[4])
            time.sleep(5)
        self.stop_stop_handler_0()

    def check_suspend(self):
        # Check if suspend running play
        if PlayerModel.paused_running:
            self.wait_for_resume()

    def run_stop_handler(self):
        # Run keyboard listener that suspend simulating of events
        PlayerModel.handler_is_running = True
        PlayerModel.break_running = False
        PlayerModel.keyboard_lock = Lock()
        PlayerModel.keyboard_lock.acquire()

        def handler_0(event):
            # Pause running sequence if ESC is pressed double time - with max 1 second delay
            if event.name == "esc" and event.event_type == "down":
                if PlayerModel.esc_once_pressed:
                    delay_sec = (datetime.now() - PlayerModel.esc_once_pressed).total_seconds()
                    if delay_sec <= 1:
                        if not PlayerModel.paused_running and not PlayerModel.break_running:
                            PlayerModel.paused_running = True
                            Ui().gui.show_pause_running_sequence_view()
                    else:
                        PlayerModel.esc_once_pressed = datetime.now()
                else:
                    PlayerModel.esc_once_pressed = datetime.now()

        keyboard._listener.add_handler(handler_0)
        self.keyboard_lock.acquire()
        keyboard._listener.remove_handler(handler_0)

    def stop_stop_handler_0(self):
        # Stop keyboard listener
        self.ui.terminal.print_info_log("Stopping all running sequences")
        keyboard.unhook_all()
        if self.keyboard_lock.locked():
            self.keyboard_lock.release()
        PlayerModel.handler_is_running = False
        self.break_running()

    def break_running(self):
        PlayerModel.paused_running = False
        PlayerModel.break_running = True
        PlayerModel.loop_is_running = False

    def suspend_running(self):
        # Suspend running simulating of events
        PlayerModel.paused_running = True

    def wait_for_resume(self):
        # Wait loop with one second delay
        self.ui.terminal.print_info_log("Suspend all running sequences")
        while PlayerModel.paused_running: time.sleep(0.1)

    def resume(self):
        # Resume suspended simulation of events
        self.ui.terminal.print_info_log("Resume suspended sequences")
        PlayerModel.paused_running = False

    def change_delay(self, delay):
        # Change delay between steps
        PlayerModel.custom_delay = delay
