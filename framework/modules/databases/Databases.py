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

# Generated 2022-05-15 19:54:37.802968
# Class Databases
class Databases:

    def create_current_db(self, db_path):
        from framework.modules.databases.core.Current import Current
        return Current().create_current_db(db_path)

    def get_all_current_entity(self, entity_name):
        from framework.modules.databases.core.Current import Current
        return Current().get_all_current_entity(entity_name)

    def get_all_sequence_entity(self, entity_name):
        from framework.modules.databases.core.Current import Current
        return Current().get_all_sequence_entity(entity_name)

    def get_certain_data(self, index):
        from framework.modules.databases.core.Current import Current
        return Current().get_certain_data(index)

    def check_if_entry_exist_in_sequences(self, text_entry):
        from framework.modules.databases.core.Current import Current
        return Current().check_if_entry_exist_in_sequences(text_entry)

    def get_just_sentence_from_seq_table(self):
        from framework.modules.databases.core.Current import Current
        return Current().get_just_sentence_from_seq_table()

    def get_condition_by_uuid(self, uuid):
        from framework.modules.databases.core.Current import Current
        return Current().get_condition_by_uuid(uuid)

    def update_current_entity_line(self, treatment_array, topic):
        from framework.modules.databases.core.Current import Current
        return Current().update_current_entity_line(treatment_array, topic)

    def write_current_entity_line(self, treatment_array, topic):
        from framework.modules.databases.core.Current import Current
        return Current().write_current_entity_line(treatment_array, topic)

    def write_to_conditions_table(self, data):
        from framework.modules.databases.core.Current import Current
        return Current().write_to_conditions_table(data)

    def write_to_sequence_table(self, data):
        from framework.modules.databases.core.Current import Current
        return Current().write_to_sequence_table(data)

    def update_line_in_sequence_table(self, array):
        from framework.modules.databases.core.Current import Current
        return Current().update_line_in_sequence_table(array)

    def update_line_in_conditions_table(self, array):
        from framework.modules.databases.core.Current import Current
        return Current().update_line_in_conditions_table(array)

    def delete_sequence(self, array, uuid):
        from framework.modules.databases.core.Current import Current
        return Current().delete_sequence(array, uuid)

    def delete_condition(self, array, uuid):
        from framework.modules.databases.core.Current import Current
        return Current().delete_condition(array, uuid)

    def get_all_system_entity(self, entity):
        from framework.modules.databases.core.System import System
        return System().get_all_system_entity(entity)

    def write_to_orientation_table(self, entity, data):
        from framework.modules.databases.core.System import System
        return System().write_to_orientation_table(entity, data)

    def load_sdb_table_to_attribute(self, orientation_model, identifier):
        from framework.modules.databases.core.System import System
        return System().load_sdb_table_to_attribute(orientation_model, identifier)

    def delete_sdb_entity(self, entity):
        from framework.modules.databases.core.System import System
        return System().delete_sdb_entity(entity)

    def rewrite_databases_table(self, data):
        from framework.modules.databases.core.User import User
        return User().rewrite_databases_table(data)

    def write_to_databases_table(self, path, name):
        from framework.modules.databases.core.User import User
        return User().write_to_databases_table(path, name)

    def get_all_udb_entity(self, entity_name):
        from framework.modules.databases.core.User import User
        return User().get_all_udb_entity(entity_name)

    def get_current_config_value(self, current_configuration):
        from framework.modules.databases.core.User import User
        return User().get_current_config_value(current_configuration)

    def save_configuration(self, configuration, value):
        from framework.modules.databases.core.User import User
        return User().save_configuration(configuration, value)

    def write_to_paths_table(self, data):
        from framework.modules.databases.core.User import User
        return User().write_to_paths_table(data)

# End of class Databases
