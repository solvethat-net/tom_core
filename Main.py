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

import os

from core_util.CoreModel import CoreModel
from sequences.Sequences import Sequences


class Main(CoreModel):

    def __init__(self):
        logo = open("properties/logo.txt", "r", encoding="utf8").read()
        # print('\033[94m' + logo + '\033[0m')
        print(logo)
        CoreModel.root_path = os.path.dirname(os.path.abspath(__file__))
        Sequences().on_start.run()


if __name__ == "__main__":
    Main()
# Run application with this script
