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

from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from framework.modules.databases.core.generic.Connector import Connector


class Controller(Connector, CoreModel):

    def __init__(self):
        super().__init__()

    def open_udb_connection(self):
        return self.open_connection(CoreModel.root_path + chr(92) + "database" + chr(92) + "UDB.db")

    def get_all_udb_entity(self, entity_name):
        # Get all data from table
        self.open_udb_connection()
        all_entity = self.get_all_entity_content(entity_name)
        self.close_connection()
        return all_entity

    def get_current_config_value(self, current_configuration):
        # Get configuration value by title
        self.open_udb_connection()
        try:
            self.cursor.execute(
                "SELECT * FROM CONFIG WHERE configuration" + chr(61) + chr(39) + current_configuration + chr(39))
            line = self.cursor.fetchall()
            self.close_connection()
            to_return = line[0][1]
            return to_return
        except:
            self.ui.terminal.print_warn_log("No configuration match for " + current_configuration)
            return MetadataEnum.ERROR

    def save_configuration(self, configuration, value):
        # Entity for saving configuration
        self.open_udb_connection()
        try:
            self.cursor.execute(
                "UPDATE CONFIG SET " + "value" + chr(61) + chr(
                    39) + str(value) + chr(39) + " WHERE configuration" + chr(61) + chr(39) + str(configuration) + chr(
                    39))
            self.close_connection()
        except:
            self.ui.terminal.print_warn_log("Error while creating table CONFIG")

    def write_to_paths_table(self, data):
        # Write data to entity data[0=index identifier, 1=data]
        self.open_udb_connection()
        try:
            self.cursor.execute(
                "INSERT INTO PATHS VALUES" + chr(40) + chr(39) + data[0] + chr(39) + chr(44) + chr(39) + data[1] + chr(
                    39) + chr(41))
            self.close_connection()
        except:
            try:
                self.cursor.execute("CREATE TABLE PATHS(shortcut text, path text)")
                self.cursor.execute(
                    "INSERT INTO PATHS VALUES" + chr(40) + chr(39) + data[0] + chr(39) + chr(44) + chr(39) + data[
                        1] + chr(39) + chr(41))
                self.close_connection()
            except:
                self.ui.terminal.print_warn_log("Error while creating table PATHS")

    def write_to_databases_table(self, path, name):
        # Write data to entity databases
        self.open_udb_connection()
        all_entity = self.get_all_entity_content("DATABASES")
        for one in all_entity:
            if one[0] == path and one[1] == name:
                return
        try:
            self.cursor.execute(
                "INSERT INTO DATABASES VALUES" + chr(40) + chr(39) + path + chr(39) + chr(44) + chr(39) + name + chr(
                    39) + chr(41))
            self.close_connection()
        except:
            try:
                self.cursor.execute("CREATE TABLE DATABASES(path text, name text)")
                self.cursor.execute(
                    "INSERT INTO PATHS VALUES" + chr(40) + chr(39) + path + chr(39) + chr(44) + chr(39) + name + chr(
                        39) + chr(41))
                self.close_connection()
            except:
                self.ui.terminal.print_warn_log("Error while creating table DATABASES")

    def rewrite_databases_table(self, data):
        # Rewrite all entity databases content
        self.open_udb_connection()
        self.delete_entity("DATABASES")
        try:
            self.cursor.execute("CREATE TABLE DATABASES(path text, name text)")
            for one in data:
                self.cursor.execute(
                    "INSERT INTO DATABASES VALUES" + chr(40) + chr(39) + one[0] + chr(39) + chr(44) + chr(39) + one[
                        1] + chr(39) + chr(41))
            self.close_connection()
        except:
            self.ui.terminal.print_warn_log("Error while rewriting table DATABASES")
