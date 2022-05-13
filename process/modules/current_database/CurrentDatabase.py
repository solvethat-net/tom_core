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

# Generated 2022-05-08 22:04:12.091140
# Class CurrentDatabase
import datetime
from core_util.LogEnum import LogEnum


class CurrentDatabase:

    def write_treatment(self, synapse_model):
        from process.modules.current_database.core.Treatment import Treatment
        synapse_model.log.append([datetime.datetime.now(), LogEnum.current_database_write_treatment,""])
        return Treatment().write_treatment(synapse_model)

    def create_new_sequence(self, synapse_model):
        from process.modules.current_database.core.Treatment import Treatment
        synapse_model.log.append([datetime.datetime.now(), LogEnum.current_database_create_new_sequence,""])
        return Treatment().create_new_sequence(synapse_model)

    def create_new_condition(self, data, true, false, threshold, position):
        from process.modules.current_database.core.Treatment import Treatment
        return Treatment().create_new_condition(data, true, false, threshold, position)

    def create_new_watcher(self, data, true, false, threshold, position):
        from process.modules.current_database.core.Treatment import Treatment
        return Treatment().create_new_watcher(data, true, false, threshold, position)

    def read_treatment(self, synapse_model):
        from process.modules.current_database.core.Treatment import Treatment
        synapse_model.log.append([datetime.datetime.now(), LogEnum.current_database_read_treatment,""])
        return Treatment().read_treatment(synapse_model)

# End of class CurrentDatabase
