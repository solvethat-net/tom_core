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

from framework.modules.databases.core.current.Read import Read
from framework.modules.databases.core.current.Update import Update
from framework.modules.databases.core.generic.Connector import Connector


class Current:

    def __init__(self):
        self.read = Read()
        self.update = Update()

    def create_current_db(self, db_path):
        conn = Connector()
        conn.open_connection(db_path)
        conn.close_connection()

    # Read calls block
    def get_all_current_entity(self, entity_name):
        return self.read.get_all_current_entity(entity_name)

    def get_all_sequence_entity(self, entity_name):
        return self.read.get_all_sequence_entity(entity_name)

    def get_certain_data(self, index):
        return self.read.get_certain_data(index)

    def check_if_entry_exist_in_sequences(self, text_entry):
        return self.read.check_if_entry_exist_in_sequences(text_entry)

    def get_just_sentence_from_seq_table(self):
        return self.read.get_just_sentence_from_seq_table()

    def get_condition_by_uuid(self, uuid):
        return self.read.get_condition_by_uuid(uuid)

    # Write calls block
    def update_current_entity_line(self, treatment_array, topic):
        return self.update.update_current_entity_line(treatment_array, topic)

    def write_current_entity_line(self, treatment_array, topic):
        return self.update.write_current_entity_line(treatment_array, topic)

    def write_to_conditions_table(self, data):
        return self.update.write_to_conditions_table(data)

    def write_to_sequence_table(self, data):
        return self.update.write_to_sequence_table(data)

    def update_line_in_sequence_table(self, array):
        return self.update.update_line_in_sequence_table(array)

    def update_line_in_conditions_table(self, array):
        return self.update.update_line_in_conditions_table(array)

    def delete_sequence(self, array, uuid):
        return self.update.delete_sequence(array, uuid)

    def delete_condition(self, array, uuid):
        return self.update.delete_condition(array, uuid)
