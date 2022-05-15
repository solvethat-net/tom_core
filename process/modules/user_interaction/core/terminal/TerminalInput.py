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

from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
import datetime
from framework.Framework import Framework
from ui.Ui import Ui


class TerminalInput(CoreModel):

    def __init__(self):
        self.framework = Framework()
        self.ui = Ui()

    def run_terminal_user_input_once(self, synapse_model):
        # Print question on terminal
        if synapse_model.data:
            for one in synapse_model.data:
                if one[3][1] == MetadataEnum.QUESTION:
                    arr = self.framework.process_support.transform_data_index_to_string(one)
                    self.ui.terminal.print(CoreModel.avatar + chr(58) + chr(32) + arr[1])
                    synapse_model.data.extend(
                        self.framework.process_support.user_input_to_synapse_model(
                            self.ui.terminal.input(CoreModel.user_name + chr(58) + chr(32)),
                            datetime.datetime.now(),
                            [MetadataEnum.USER, MetadataEnum.INPUT,
                             MetadataEnum.SENTENCE]))
        else:
            synapse_model.data = self.framework.process_support.user_input_to_synapse_model(
                self.ui.terminal.input(CoreModel.user_name + chr(58) + chr(32)),
                datetime.datetime.now(),
                [MetadataEnum.USER, MetadataEnum.INPUT,
                 MetadataEnum.SENTENCE])
        return synapse_model
