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
from keyboard import KEY_UP
from mouse import UP, LEFT, RIGHT, MIDDLE
from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from framework.modules.event_player.core.assets.BranchOutTreatment import BranchOutTreatment
from framework.modules.event_player.core.model.PlayerModel import PlayerModel


class SynapseModelTreatment(PlayerModel):

    def __init__(self, parent):
        self.parent = parent
        self.branch_out = BranchOutTreatment(self.parent)
        self.framework = Framework()

    def play_synapse_model(self, synapse_model):
        # Play synapse_model line by line with optional or original delay
        last_time = None
        act_time = None
        for one_data in synapse_model.data:
            self.parent.check_suspend()
            if PlayerModel.break_running:
                return
            if synapse_model.data.index(one_data) != 0:
                act_time = one_data[0]
                data = one_data[1]
                meta = one_data[2][0][0]
                if not PlayerModel.paused_running:
                    if PlayerModel.custom_delay:
                        if meta == MetadataEnum.MOUSE_MOVE and \
                                (synapse_model.data[synapse_model.data.index(one_data) - 1][2][0][
                                     0] == MetadataEnum.MOUSE_MOVE or
                                 synapse_model.data[synapse_model.data.index(one_data) + 1][2][0][
                                     0] == MetadataEnum.MOUSE_MOVE):
                            time.sleep((act_time - last_time).total_seconds())
                        elif meta == MetadataEnum.MOUSE_SCROLL and \
                                (synapse_model.data[synapse_model.data.index(one_data) - 1][2][0][
                                     0] == MetadataEnum.MOUSE_SCROLL or
                                 synapse_model.data[synapse_model.data.index(one_data) + 1][2][0][
                                     0] == MetadataEnum.MOUSE_SCROLL):
                            time.sleep((act_time - last_time).total_seconds())
                        elif data[0] == UP or data[0] == KEY_UP:
                            time.sleep((act_time - last_time).total_seconds())
                        else:
                            time.sleep(PlayerModel.custom_delay)
                    elif last_time is not None:
                        time.sleep((act_time - last_time).total_seconds())
                    if meta == MetadataEnum.MOUSE_LEFT:
                        self.framework.device_control.mouse_action(LEFT, data[0])
                    if meta == MetadataEnum.MOUSE_RIGHT:
                        self.framework.device_control.mouse_action(RIGHT, data[0])
                    if meta == MetadataEnum.MOUSE_MIDDLE:
                        self.framework.device_control.mouse_action(MIDDLE, data[0])
                    if meta == MetadataEnum.MOUSE_SCROLL:
                        self.framework.device_control.scroll(data[0])
                    if meta == MetadataEnum.MOUSE_MOVE:
                        self.framework.device_control.move_cursor(data[0], data[1])
                    if meta == MetadataEnum.CONDITION_MOUSE_POSITION:
                        self.framework.device_control.move_cursor(PlayerModel.condition_mouse_position[0],
                                                                  PlayerModel.condition_mouse_position[1])
                    if meta == MetadataEnum.KEYBOARD:
                        if len(data) > 2:
                            keys = " ".join(data[:-1])
                        else:
                            keys = data[0]
                        self.framework.device_control.keyboard_action(keys, data[-1])
                    if meta == MetadataEnum.SEQUENCE:
                        self.parent.run_sequence_by_table_name(data[0], PlayerModel.custom_delay)
                    if meta == MetadataEnum.CONDITION:
                        self.parent.treatment_condition(data[0], PlayerModel.custom_delay)
                    if meta == MetadataEnum.LOOP:
                        try:
                            loops = int(data[1])
                        except:
                            loops = 1
                        ind = 0
                        PlayerModel.loop_is_running = True
                        while ind < loops:
                            if PlayerModel.break_running:
                                return
                            if one_data[2][0][1] == MetadataEnum.SEQUENCE:
                                self.parent.run_sequence_by_table_name(data[0], PlayerModel.custom_delay)
                            elif one_data[2][0][1] == MetadataEnum.CONDITION:
                                self.parent.treatment_condition(data[0], PlayerModel.custom_delay)
                            elif one_data[2][0][1] == MetadataEnum.WATCHER:
                                self.parent.treatment_watcher(data[0], PlayerModel.custom_delay)
                            ind += 1
                        PlayerModel.loop_is_running = False
                else:
                    self.parent.wait_for_resume()
                    if PlayerModel.break_running:
                        return
            last_time = act_time
