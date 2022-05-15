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
from sequences.modules.input_treatment.InputTreatment import InputTreatment
from sequences.modules.on_start.OnStart import OnStart
from sequences.modules.read_and_execute.ReadAndExecute import ReadAndExecute


class Sequences:
    input_treatment = InputTreatment()
    on_start = OnStart()
    read_and_execute = ReadAndExecute()
# End of class Sequences
