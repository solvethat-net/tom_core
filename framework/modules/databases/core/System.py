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

from framework.modules.databases.core.system.Controller import Controller


class System:
    def __init__(self):
        self.system_controller = Controller()

    def get_all_system_entity(self, entity):
        return self.system_controller.get_all_system_entity(entity)

    def write_to_orientation_table(self, entity, data):
        return self.system_controller.write_to_orientation_table(entity, data)

    def load_sdb_table_to_attribute(self, orientation_model, identifier):
        return self.system_controller.load_sdb_table_to_attribute(orientation_model, identifier)

    def delete_sdb_entity(self, entity):
        return self.system_controller.delete_sdb_entity(entity)
