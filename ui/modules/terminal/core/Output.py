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

import bcolors

from framework.Framework import Framework


class Output:

    def __init__(self):
        self.framework = Framework()

    def print_in_color(self, message, color):
        # Print colored message in terminal
        # TODO solve printing color multiplatform
        # print(color + message + bcolors.ENDC)
        print(message)

    def print_info_log(self, message):
        # Print blue colored message
        message = str(self.framework.process_support.get_actual_date_time()) + chr(32) + "INFO" + chr(58) + chr(
            32) + message
        self.print_in_color(message, bcolors.BLUE)

    def print_warn_log(self, message):
        # Print red colored message
        message = str(self.framework.process_support.get_actual_date_time()) + chr(32) + "WARN" + chr(58) + chr(
            32) + message
        self.print_in_color(message, bcolors.FAIL)
