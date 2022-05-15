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
# Class CurrentDatabase
import datetime
from core_util.LogEnum import LogEnum


class CurrentDatabase:

    def write_synapse_model(self, synapse_model):
        from process.modules.current_database.core.Controller import Controller
        synapse_model.log.append([datetime.datetime.now(), LogEnum.current_database_write_synapse_model,""])
        return Controller().write_synapse_model(synapse_model)

    def create_new_sequence(self, synapse_model):
        from process.modules.current_database.core.Controller import Controller
        synapse_model.log.append([datetime.datetime.now(), LogEnum.current_database_create_new_sequence,""])
        return Controller().create_new_sequence(synapse_model)

    def create_new_condition(self, data, true, false, threshold, position):
        from process.modules.current_database.core.Controller import Controller
        return Controller().create_new_condition(data, true, false, threshold, position)

    def create_new_watcher(self, data, true, false, threshold, position):
        from process.modules.current_database.core.Controller import Controller
        return Controller().create_new_watcher(data, true, false, threshold, position)

    def read_treatment(self, synapse_model):
        from process.modules.current_database.core.Controller import Controller
        synapse_model.log.append([datetime.datetime.now(), LogEnum.current_database_read_treatment,""])
        return Controller().read_treatment(synapse_model)

# End of class CurrentDatabase
