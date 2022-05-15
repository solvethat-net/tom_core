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
from framework.Framework import Framework
from ui.Ui import Ui


class TerminalOutput(CoreModel):

    def __init__(self):
        self.framework = Framework()
        self.ui = Ui()

    def print_terminal_output(self, synapse_model):
        # Print all from data parameter
        for index in synapse_model.data:
            self.ui.terminal.print(
                CoreModel.avatar + chr(58) + chr(32) + self.framework.process_support.convert_array_to_string(index))
            synapse_model.data[synapse_model.data.index(index)][3][2] = MetadataEnum.PRINTED
        return synapse_model
