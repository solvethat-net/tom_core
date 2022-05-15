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

from process.modules.user_interaction.core.terminal.TerminalInput import TerminalInput
from process.modules.user_interaction.core.terminal.TerminalOutput import TerminalOutput


class TerminalIface:

    def __init__(self):
        self.terminal_out_put = TerminalOutput()
        self.terminal_input = TerminalInput()

    def print_terminal_output(self, synapse_model):
        return self.terminal_out_put.print_terminal_output(synapse_model)

    def run_terminal_user_input_once(self, synapse_model):
        return self.terminal_input.run_terminal_user_input_once(synapse_model)
