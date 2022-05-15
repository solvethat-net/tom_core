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

# Generated 2022-05-15 19:54:37.818594
# Class FilesystemControlling
import datetime
from core_util.LogEnum import LogEnum


class FilesystemControlling:

    def control_dir(self, synapse_model):
        from process.modules.filesystem_controlling.core.Controller import Controller
        synapse_model.log.append([datetime.datetime.now(), LogEnum.filesystem_controlling_control_dir,""])
        return Controller().control_dir(synapse_model)

    def control_file(self, synapse_model):
        from process.modules.filesystem_controlling.core.Controller import Controller
        synapse_model.log.append([datetime.datetime.now(), LogEnum.filesystem_controlling_control_file,""])
        return Controller().control_file(synapse_model)

# End of class FilesystemControlling
