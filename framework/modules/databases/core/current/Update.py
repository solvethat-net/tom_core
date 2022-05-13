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

from core_util.MetadataEnum import MetadataEnum
from framework.modules.databases.core.current.Controller import Controller


class Update(Controller):

    def update_current_entity_line(self, treatment_array, topic):
        # Update line in user database by link
        self.open_current_db_connection()
        try:
            self.cursor.execute(
                "UPDATE " + topic + " SET time" + chr(61) + chr(39) + treatment_array[0] + chr(39) + chr(
                    44) + " note" + chr(61) + chr(39) + treatment_array[2] + chr(39) + " WHERE link" + chr(61) + chr(
                    39) +
                treatment_array[1] + chr(39))
            self.close_connection()
            return MetadataEnum.OK
        except:
            self.close_connection()
            return MetadataEnum.ERROR

    def write_current_entity_line(self, treatment_array, topic):
        # Insert treatment_array to user database
        self.open_current_db_connection()
        try:
            self.cursor.execute(
                "INSERT INTO " + topic + " VALUES" + chr(40) + chr(39) + treatment_array[0] + chr(39) + chr(44) + chr(
                    39) + treatment_array[1] + chr(39) + chr(44) + chr(39) + treatment_array[2] + chr(39) + chr(41))
            self.close_connection()
            return MetadataEnum.OK
        except:
            self.cursor.execute("CREATE TABLE " + topic + "(time text,data text,orientation text)")
            self.cursor.execute(
                "INSERT INTO " + topic + " VALUES" + chr(40) + chr(39) + treatment_array[0] + chr(39) + chr(44) + chr(
                    39) + treatment_array[1] + chr(39) + chr(44) + chr(39) + treatment_array[2] + chr(39) + chr(41))
            self.close_connection()
            return MetadataEnum.OK

    def write_to_conditions_table(self, data):
        # Write data to CONDITIONS entity [uuid, name, data, true, false, threshold, position]
        self.open_current_db_connection()
        try:
            self.cursor.execute(
                "INSERT INTO CONDITIONS VALUES" + chr(40) + chr(39) + data[0] + chr(39) + chr(44) + chr(39) + data[
                    1] + chr(39) + chr(44) + chr(39) + data[2] + chr(39) + chr(44) + chr(39) + data[3] + chr(39) + chr(
                    44) + chr(39) + data[4] + chr(39) + chr(44) + chr(39) + data[5] + chr(39) + chr(44) + chr(39) +
                data[6] + chr(39) + chr(41))
            self.close_connection()
        except:
            try:
                self.cursor.execute(
                    "CREATE TABLE CONDITIONS(uuid text, name text, data text, true text, false text, threshold text, position text)")
                self.cursor.execute(
                    "INSERT INTO CONDITIONS VALUES" + chr(40) + chr(39) + data[0] + chr(39) + chr(44) + chr(39) + data[
                        1] + chr(39) + chr(44) + chr(39) + data[2] + chr(39) + chr(44) + chr(39) + data[3] + chr(
                        39) + chr(
                        44) + chr(39) + data[4] + chr(39) + chr(44) + chr(39) + data[5] + chr(39) + chr(44) + chr(39) +
                    data[6] + chr(39) + chr(41))
                self.close_connection()
            except:
                self.ui.terminal.print_warn_log("Error while writing to table CONDITIONS")

    def write_to_sequence_table(self, data):
        # Write data to SEQUENCES entity data[0=uuid, 1=name]
        self.open_current_db_connection()
        try:
            self.cursor.execute(
                "INSERT INTO SEQUENCES VALUES" + chr(40) + chr(39) + data[0] + chr(39) + chr(44) + chr(39) + data[
                    1] + chr(39) + chr(41))
            self.close_connection()
        except:
            try:
                self.cursor.execute("CREATE TABLE SEQUENCES(uuid text, name text)")
                self.cursor.execute(
                    "INSERT INTO SEQUENCES VALUES" + chr(40) + chr(39) + data[0] + chr(39) + chr(44) + chr(39) + data[
                        1] + chr(39) + chr(41))
                self.close_connection()
            except:
                self.ui.terminal.print_warn_log("Error while creating table SEQUENCES")

    def update_line_in_sequence_table(self, array):
        # Update line in table SEQUENCES by UUID
        self.open_current_db_connection()
        try:
            self.cursor.execute(
                "UPDATE SEQUENCES SET name" + chr(61) + chr(39) + array[1] + chr(39) + " WHERE uuid" + chr(61) + chr(
                    39) + array[0] + chr(39))
            self.close_connection()
        except:
            self.close_connection()
            self.ui.terminal.print_warn_log("Error while creating table SEQUENCES")

    def update_line_in_conditions_table(self, array):
        # Update line in table CONDITIONS by UUID
        self.open_current_db_connection()
        try:
            self.cursor.execute(
                "UPDATE CONDITIONS SET name" + chr(61) + chr(39) + array[1] + chr(39) + " WHERE uuid" + chr(61) + chr(
                    39) + array[0] + chr(39))
            self.close_connection()
        except:
            self.close_connection()
            self.ui.terminal.print_warn_log("Error while creating table CONDITIONS")

    def delete_sequence(self, array, uuid):
        # Remove line by array with content to remove and table by uuid
        self.open_current_db_connection()
        try:
            sql = 'DELETE FROM SEQUENCES WHERE uuid=?'
            self.cursor.execute(sql, (array[0],))
            self.delete_entity(uuid)
            self.close_connection()
        except:
            self.ui.terminal.print_warn_log("Error while removing from table SEQUENCES")

    def delete_condition(self, array, uuid):
        # Remove line by array with content to remove
        self.open_current_db_connection()
        try:
            sql = 'DELETE FROM CONDITIONS WHERE uuid=?'
            self.cursor.execute(sql, (array[0],))
            self.delete_entity(uuid)
            self.close_connection()
        except:
            self.ui.terminal.print_warn_log("Error while removing from table CONDITIONS")
