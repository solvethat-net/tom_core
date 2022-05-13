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

import sqlite3

from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from framework.modules.databases.core.generic.Connector import Connector


class Controller(Connector, CoreModel):

    def __init__(self):
        super().__init__()

    def open_sdb_connection(self):
        return self.open_connection(CoreModel.root_path + chr(92) + "database" + chr(92) + "SDB.db")

    def delete_sdb_entity(self, entity):
        self.open_sdb_connection()
        self.delete_entity(entity)
        self.close_connection()

    def get_all_system_entity(self, entity):
        # Select all data from entity by parameter "entity"
        self.open_sdb_connection()
        try:
            result = self.get_all_entity_content(entity)
        except:
            self.ui.terminal.print_warn_log("Error while reading table '" + entity + "'")
            self.close_connection()
            return MetadataEnum.ERROR
        self.close_connection()

        result_arr_arr = []
        if len(result) == 1 and len(result[0]) == 1:
            return result[0][0]

        elif len(result) > 1 and len(result[0]) == 1:
            for one in result:
                result_arr_arr.append(one[0])
            return result_arr_arr

        elif len(result) > 0 and len(result[0]) > 1:
            for one in result:
                result_arr = []
                for oneOne in one:
                    result_arr.append(oneOne)
                result_arr_arr.append(result_arr)

            return result_arr_arr

    def write_to_orientation_table(self, entity, data):
        # Write data to entity data[0=index identifier, 1=data]
        self.open_sdb_connection()
        try:
            self.cursor.execute("INSERT INTO " + entity + " VALUES" + chr(40) + chr(39) + data + chr(39) + chr(41))
        except sqlite3.Error as error:
            try:
                self.cursor.execute("CREATE TABLE " + entity + "(content text)")
                self.cursor.execute("INSERT INTO " + entity + " VALUES" + chr(40) + chr(39) + data + chr(39) + chr(41))
            except sqlite3.Error as error:
                print("Error while writing to table " + entity)
        self.close_connection()

    def load_sdb_table_to_attribute(self, orientation_model, identifier):
        # Find coincident DB tables by attribute in orientation_model class
        self.open_sdb_connection()
        for one in dir(orientation_model):
            if (chr(95) + chr(95)) not in one:
                if identifier:
                    result = self.get_all_entity_content(identifier + chr(95) + one)
                else:
                    result = self.get_all_entity_content(one)
                if result:
                    setattr(orientation_model, one, result[0][0])
        self.close_connection()
        return orientation_model
