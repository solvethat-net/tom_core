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

# Generated 2022-05-08 22:04:12.081266
# Class ProcessSupport
class ProcessSupport:

    def to_camel_case(self, snake_text):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().to_camel_case(snake_text)

    def try_make_metadata_enum(self, value_str):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().try_make_metadata_enum(value_str)

    def has_string_numbers(self, input_string):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().has_string_numbers(input_string)

    def trans_file_list_to_array(self, file_path):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().trans_file_list_to_array(file_path)

    def trans_file_to_in_line_list(self, filePath):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().trans_file_to_in_line_list(filePath)

    def remove_whitespaces(self, list_attribute):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().remove_whitespaces(list_attribute)

    def compare_lists(self, original, challenger):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().compare_lists(original, challenger)

    def transform_data_index_to_string(self, index):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().transform_data_index_to_string(index)

    def make_list_from_string_with_brackets(self, text_var):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().make_list_from_string_with_brackets(text_var)

    def transform_data_index_to_lists(self, index):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().transform_data_index_to_lists(index)

    def post_db_read_condition_treatment(self, row):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().post_db_read_condition_treatment(row)

    def sort_data_by_score(self, challenger):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().sort_data_by_score(challenger)

    def base64_string_to_base64_format(self, string):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().base64_string_to_base64_format(string)

    def find_coincident(self, name_list, data_list):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().find_coincident(name_list, data_list)

    def set_and_run_by_metadata(self, generic_object, synapse_model):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().set_and_run_by_metadata(generic_object, synapse_model)

    def set_topic_by_first_line(self, synapse_model):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().set_topic_by_first_line(synapse_model)

    def camel_case_to_snake_case(self, word):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().camel_case_to_snake_case(word)

    def convert_array_to_string(self, array):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().convert_array_to_string(array)

    def get_actual_date_time_in_czech_format(self):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().get_actual_date_time_in_czech_format()

    def get_actual_date_time(self):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().get_actual_date_time()

    def wrap_chars_with_char(self, to_wrap, wrap_char, text):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().wrap_chars_with_char(to_wrap, wrap_char, text)

    def reverse_list(self, list_attribute):
        from framework.modules.process_support.core.DataOperations import DataOperations
        return DataOperations().reverse_list(list_attribute)

    def convert_base64_to_numpy_arr(self, data):
        from framework.modules.process_support.core.PictureOperations import PictureOperations
        return PictureOperations().convert_base64_to_numpy_arr(data)

    def equal(im1, im2):
        from framework.modules.process_support.core.PictureOperations import PictureOperations
        return PictureOperations().equal(im1, im2)

    def user_input_to_synapse_model(self, user_input, input_time, metadata):
        from framework.modules.process_support.core.UserInput import UserInput
        return UserInput().user_input_to_synapse_model(user_input, input_time, metadata)

    def decide_if_is_splittable(self, word):
        from framework.modules.process_support.core.UserInput import UserInput
        return UserInput().decide_if_is_splittable(word)

    def decide_if_replace_end_char(self, word):
        from framework.modules.process_support.core.UserInput import UserInput
        return UserInput().decide_if_replace_end_char(word)

    def treatment_entry(self, text):
        from framework.modules.process_support.core.UserInput import UserInput
        return UserInput().treatment_entry(text)

    def append_to_key_list_if_recording(self, seq_code=None):
        from framework.modules.process_support.core.UserInput import UserInput
        return UserInput().append_to_key_list_if_recording(seq_code=None)

# End of class ProcessSupport
