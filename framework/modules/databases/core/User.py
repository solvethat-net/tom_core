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

from framework.modules.databases.core.user.Controller import Controller


class User:
    def __init__(self):
        self.user_controller = Controller()

    def rewrite_databases_table(self, data):
        return self.user_controller.rewrite_databases_table(data)

    def write_to_databases_table(self, path, name):
        return self.user_controller.write_to_databases_table(path, name)

    def get_all_udb_entity(self, entity_name):
        return self.user_controller.get_all_udb_entity(entity_name)

    def get_current_config_value(self, current_configuration):
        return self.user_controller.get_current_config_value(current_configuration)

    def save_configuration(self, configuration, value):
        return self.user_controller.save_configuration(configuration, value)

    def write_to_paths_table(self, data):
        return self.user_controller.write_to_paths_table(data)
