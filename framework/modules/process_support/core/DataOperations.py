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

import re
import inspect
from datetime import datetime
from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from framework.modules.non_lang_expressions.core.model.NonLangOrientation import NonLangOrientation
from framework.Framework import Framework
from ui.Ui import Ui


class DataOperations(NonLangOrientation, CoreModel):

    def __init__(self):
        self.attribute_array = []
        self.framework = Framework()
        self.ui = Ui()

    def to_camel_case(self, snake_text):
        # Convert snake_case to CamelCase
        parts = snake_text.split(chr(95))
        without_capital = parts[0] + "".join(x.title() for x in parts[1:])
        return without_capital[:1].upper() + without_capital[1:]

    def try_make_metadata_enum(self, value_str):
        # Return Metadata_Enum or string back if does not match
        value_str = value_str.replace(chr(32), "")
        try:
            return MetadataEnum[value_str.upper()]
        except:
            return value_str

    def has_string_numbers(self, input_string):
        # Check if string contain any numbers
        return any(char.isdigit() for char in input_string)

    def trans_file_list_to_array(self, file_path):
        # Make array list from file list
        array = []
        file_lines = self.framework.io_streams.getFileLines(CoreModel.root_path + file_path)
        for line in file_lines:
            if chr(10) in line:
                line = line.replace(chr(10), "")
            array.append(line)
        return array

    def trans_file_to_in_line_list(self, filePath):
        # Make inline list from file list
        file_lines = self.framework.io_streams.getFileLines(CoreModel.root_path + filePath)
        work_var = chr(32)
        for one in file_lines:
            if chr(10) in one:
                one = one[:one.index(chr(10))]
            if chr(39) in one:
                one = one[:one.index(chr(39))] + chr(39) + one[one.index(chr(39)):]
            work_var = work_var + one + chr(32)
        return work_var

    def remove_whitespaces(self, list_attribute):
        # Remove all white spaces from list and indexes
        ok = False
        while not ok and list_attribute:
            ok = True
            for temp in list_attribute:
                if not temp or temp == chr(32):
                    del list_attribute[list_attribute.index(temp)]
                    ok = False
        return list_attribute

    def compare_lists(self, original, challenger):
        # Compare if lists are similar
        result = []
        for one in challenger:
            ok = True
            if one[1] == original[1]:
                ok = False
            if ok:
                result.append(one)
        return result

    def transform_data_index_to_string(self, index):
        # Make string from data index of SynapseModel
        orientation = []
        data = ""
        for word in index[1]:
            data = data + str(word) + chr(32)
        data = data[:len(data) - 1]
        # for processing Metadata
        for one in index[2]:
            one_index = []
            for metaOne in one:
                if metaOne:
                    if isinstance(metaOne, MetadataEnum):
                        one_index.append(metaOne.name)
                    else:
                        one_index.append(str(metaOne))
            orientation.append(one_index)
        return [str(index[0]), data, str(orientation).replace(chr(39), "")[1:-1]]

    def make_list_from_string_with_brackets(self, text_var):
        # Find brackets in string and make list from content
        final_list = []
        while chr(91) in text_var:
            value = text_var[text_var.find(chr(91)) + 1:text_var.find(chr(93))]
            if chr(44) in value:
                sub_list = []
                for one in value.split(chr(44)):
                    sub_list.append(self.try_make_metadata_enum(one))
                final_list.append(sub_list)
            else:
                if value:
                    final_list.append([self.try_make_metadata_enum(value)])
                else:
                    final_list.append([])
            text_var = text_var.replace(text_var[text_var.find(chr(91)):text_var.find(chr(93)) + 1], "", 1)
        return final_list

    def transform_data_index_to_lists(self, index):
        # Make list from sentence splitting by space, input data is synapse_model data one line from database
        date_time_of_index = datetime.strptime(index[0], "%Y-%m-%d %H:%M:%S.%f")
        data = index[1].lower().split()
        orientation = self.make_list_from_string_with_brackets(index[2])
        return [date_time_of_index, self.remove_whitespaces(data), orientation]

    def post_db_read_condition_treatment(self, row):
        # Transform condition row from db into processable array
        true_cause = self.try_make_metadata_enum(row[3])
        false_cause = self.try_make_metadata_enum(row[4])
        threshold = float(row[5])
        if row[6]:
            position = self.remove_whitespaces(row[6].lower().split())
            position = [int(position[0]), int(position[1])]
        else:
            position = False
        return [row[0], row[1], row[2], true_cause, false_cause, threshold, position]

    def sort_data_by_score(self, challenger):
        # Sort by score in second index os parameter
        score_list = []
        for one in challenger:
            score_list.append(one[1])
        score_list = sorted(score_list, reverse=True)
        new_list = []
        for one in score_list:
            for dbOne in challenger:
                if one == dbOne[1] and dbOne[0] not in new_list:
                    new_list.append(dbOne[0])
        return list(dict.fromkeys(new_list))

    def base64_string_to_base64_format(self, string):
        return string.encode('ascii')

    def find_coincident(self, name_list, data_list):
        # Find parameters coincident with metadata
        bool_value = False
        self.attribute_array = []
        for one in data_list[2]:
            for nameOne in name_list:
                try:
                    metadata = MetadataEnum[nameOne.upper()]
                    if metadata in one:
                        self.attribute_array.append([nameOne, data_list[1][data_list[2].index(one)]])
                        bool_value = True
                except:
                    self.ui.terminal.print_warn_log("Metadata not found for name " + nameOne)
        return bool_value

    def set_and_run_by_metadata(self, generic_object, synapse_model):
        # Method set parameters of generic object and run methods
        list_attr = []
        list_method = []
        # Loop make list of method of class
        for one in inspect.getmembers(generic_object, predicate=inspect.ismethod):
            if chr(95) + chr(95) not in one[0]:
                list_method.append(one[0])
        # Loop make list of attributes of class
        for one in dir(generic_object):
            if chr(95) + chr(95) not in one and one not in list_method:
                list_attr.append(one)
        # Check if some element coincident with data[2] metadata
        for one in synapse_model.data:
            if self.find_coincident(list_attr, one):
                for oneArr in self.attribute_array:
                    setattr(generic_object, oneArr[0], oneArr[1])

            if self.find_coincident(list_method, one):
                for oneArr in self.attribute_array:
                    # TODO update General Metadata
                    if len(one) == 4:
                        one[3][2] = getattr(generic_object, oneArr[0])()
                    else:
                        getattr(generic_object, oneArr[0])()

        return synapse_model

    def set_topic_by_first_line(self, synapse_model):
        # Get first line of synapse_model
        return self.convert_array_to_string(synapse_model.data[0][1])

    def camel_case_to_snake_case(self, word):
        # Convert word in camelCase to snake_case
        return re.sub(r'(?<!^)(?=[A-Z])', chr(95), word).lower()

    def convert_array_to_string(self, array):
        # Convert array to string
        string = ""
        for word in array:
            string = string + word + chr(32)
        string.replace(string[:1], string[:1].upper())
        string = string[:len(string) - 1] + chr(46)
        return string

    def get_actual_date_time_in_czech_format(self):
        # Get actual formatted datetime
        now = datetime.now()
        return now.strftime("%d.%m.%Y-%H:%M:%S")

    def get_actual_date_time(self):
        # Get actual datetime
        return datetime.now()

    def wrap_chars_with_char(self, to_wrap, wrap_char, text):
        # Wrap specific character with another character
        for one in to_wrap:
            if one in text:
                text = text.replace(one, wrap_char + one + wrap_char)
        return text

    def reverse_list(self, list_attribute):
        # Reverse rank of list content
        reversed_list = []
        index = 1
        while index <= len(list_attribute):
            reversed_list.append(list_attribute[-index])
            index += 1
        return reversed_list
