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

from framework.modules.databases.core.current.Controller import Controller


class Read(Controller):

    def get_all_current_entity(self, entity_name):
        # Get all data from table
        self.open_current_db_connection()
        all_entity = self.get_all_entity_content(entity_name)
        self.close_connection()
        return all_entity

    def get_all_sequence_entity(self, entity_name):
        # Get all data from table
        self.all_entity = self.get_all_current_entity(entity_name)
        if self.all_entity:
            # Convert data to list
            for index in self.all_entity:
                self.all_entity[
                    self.all_entity.index(index)] = self.framework.process_support.transform_data_index_to_lists(index)
            return self.all_entity
        else:
            return False

    def get_certain_data(self, index):
        # Get data by links
        found = False
        if self.all_entity:
            for line in self.all_entity:
                if set(index[2]).intersection(line[2]):
                    if set(index[1]).intersection(line[1]):
                        score = len(set(index[1]).intersection(line[1])) + len(set(index[2]).intersection(line[2]))
                    else:
                        score = len(set(index[2]).intersection(line[2]))
                    self.certain_data.append([line, score])
                    found = True
        return found

    def check_if_entry_exist_in_sequences(self, text_entry):
        # Check entry in table SEQUENCES and return match or False
        self.open_current_db_connection()
        tbl = self.get_all_entity_content("SEQUENCES")
        self.close_connection()
        if tbl:
            for one in tbl:
                if one[1] == text_entry:
                    return one[0]
        return False

    def get_just_sentence_from_seq_table(self):
        # Return array of user entered sentence
        self.open_current_db_connection()
        content = self.get_all_entity_content("SEQUENCES")
        self.close_connection()
        final_content = []
        for one in content:
            if chr(46) in one[1]: final_content.append(one)
        return final_content

    def get_condition_by_uuid(self, uuid):
        # Get line from CONDITIONS table by UUID param
        self.open_current_db_connection()
        try:
            self.cursor.execute(
                "SELECT * FROM CONDITIONS WHERE uuid" + chr(61) + chr(39) + uuid + chr(39))
            line = self.cursor.fetchall()
            self.close_connection()
            return self.framework.process_support.post_db_read_condition_treatment(line[0])
        except:
            self.ui.terminal.print_warn_log("No CONDITIONS match for uuid " + uuid)
            return False
