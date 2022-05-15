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

# Generated 2022-05-15 19:54:37.818594
# Class Terminal
class Terminal:

    def empty_input(self):
        from ui.modules.terminal.core.Input import Input
        return Input().empty_input()

    def input_with_text(self, text):
        from ui.modules.terminal.core.Input import Input
        return Input().input_with_text(text)

    def print_in_color(self, message, color):
        from ui.modules.terminal.core.Output import Output
        return Output().print_in_color(message, color)

    def print_info_log(self, message):
        from ui.modules.terminal.core.Output import Output
        return Output().print_info_log(message)

    def print_warn_log(self, message):
        from ui.modules.terminal.core.Output import Output
        return Output().print_warn_log(message)

# End of class Terminal
