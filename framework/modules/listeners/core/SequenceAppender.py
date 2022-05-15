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

from datetime import datetime

from core_util.MetadataEnum import MetadataEnum
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from framework.modules.listeners.core.listeners.model.ListenersModel import ListenersModel


class SequenceAppender(ListenersModel, GUIModel):

    def __init__(self):
        pass

    def append_sequence_to_key_list(self, sequence_uuid):
        # Append sequence UUID
        if not GUIModel.is_focused or not GUIModel.turn_off_listeners:
            ListenersModel.key_list.append([datetime.now(), [sequence_uuid], [[MetadataEnum.SEQUENCE]],
                                            [MetadataEnum.USER, MetadataEnum.INPUT, MetadataEnum.CREATED]])

    def append_condition_to_key_list(self, condition_uuid):
        # Append condition UUID
        if not GUIModel.is_focused or not GUIModel.turn_off_listeners:
            ListenersModel.key_list.append([datetime.now(), [condition_uuid], [[MetadataEnum.CONDITION]],
                                            [MetadataEnum.USER, MetadataEnum.INPUT, MetadataEnum.CREATED]])

    def append_watcher_to_key_list(self, watcher_uuid):
        # Append condition UUID
        if not GUIModel.is_focused or not GUIModel.turn_off_listeners:
            ListenersModel.key_list.append([datetime.now(), [watcher_uuid], [[MetadataEnum.WATCHER]],
                                            [MetadataEnum.USER, MetadataEnum.INPUT, MetadataEnum.CREATED]])

    def append_user_input_to_key_list(self, data):
        # Append processed text entry
        if not GUIModel.is_focused or not GUIModel.turn_off_listeners:
            ListenersModel.key_list.append(data)

    def append_loop_sequence_to_key_list(self, uuid, loops):
        # Append loop of sequences
        if not GUIModel.is_focused or not GUIModel.turn_off_listeners:
            ListenersModel.key_list.append(
                [datetime.now(), [uuid, loops], [[MetadataEnum.LOOP, MetadataEnum.SEQUENCE]],
                 [MetadataEnum.USER, MetadataEnum.INPUT, MetadataEnum.CREATED]])

    def append_loop_condition_to_key_list(self, uuid, loops):
        # Append loop of conditions
        if not GUIModel.is_focused or not GUIModel.turn_off_listeners:
            ListenersModel.key_list.append(
                [datetime.now(), [uuid, loops], [[MetadataEnum.LOOP, MetadataEnum.CONDITION]],
                 [MetadataEnum.USER, MetadataEnum.INPUT, MetadataEnum.CREATED]])

    def append_loop_watcher_to_key_list(self, uuid, loops):
        # Append loop of watchers
        if not GUIModel.is_focused or not GUIModel.turn_off_listeners:
            ListenersModel.key_list.append(
                [datetime.now(), [uuid, loops], [[MetadataEnum.LOOP, MetadataEnum.WATCHER]],
                 [MetadataEnum.USER, MetadataEnum.INPUT, MetadataEnum.CREATED]])
