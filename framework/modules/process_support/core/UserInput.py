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

import re
from datetime import datetime
from langdetect import detect

from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from core_util.SynapseModel import SynapseModel
from framework.Framework import Framework
from ui.modules.gui.core.assets.model.GUIModel import GUIModel
from framework.modules.non_lang_expressions.core.model.NonLangOrientation import NonLangOrientation
from process.Process import Process
from sequences.Sequences import Sequences


class UserInput(GUIModel, CoreModel):

    def __init__(self):
        self.framework = Framework()
        self.process = Process()
        self.sequences = Sequences()

    def user_input_to_synapse_model(self, user_input, input_time, metadata):
        # Remove all white spaces and make list from sentence in data
        # Data: [0 Time, 1 Data[], 2 Certain Metadata[[],[],[]...], 3 General Metadata [0=source_files,1=Type,2=State]]
        # Log: [0 Time, 1 Enum = [0 module, 1 interface method], 2 Topic]
        list1 = [input_time, [], [], [3]]
        list2 = []
        try:
            lang = detect(user_input)
        except ChildProcessError:
            list2 = [[input_time, [user_input], [[]], metadata]]
            return list2
        user_input = user_input.lower()
        user_input = self.framework.process_support.wrap_chars_with_char(
            [chr(40), chr(41), chr(91), chr(93), chr(34), chr(39), chr(45), chr(58), chr(60), chr(62)], chr(32),
            user_input)
        user_input = re.split(chr(32), user_input)
        user_input = self.framework.process_support.remove_whitespaces(user_input)
        index = 0
        is_bracket_end = True
        for one in user_input:
            list1[1].append(one)
            if one == chr(40):
                is_bracket_end = False
            elif one == chr(41):
                is_bracket_end = True
            if is_bracket_end:
                result = self.decide_if_is_splittable(one)
                if result != MetadataEnum.ERROR or user_input.index(one) == len(user_input) - 1:
                    one_brackets = True
                    id_value = 1
                    while id_value <= 3:
                        if (index + id_value) < len(user_input) and (
                                user_input[index + id_value] == chr(40) or user_input[index + id_value] == chr(41)):
                            one_brackets = False
                        id_value += 1
                    if one_brackets:
                        list1[1][list1[1].index(one)] = self.decide_if_replace_end_char(one)
                        metadata[1] = result
                        metadata[2] = MetadataEnum.LIST
                        list1[3] = metadata
                        if len(list1[1]) > 2:
                            list1[2] = [[]] * len(list1[1])
                            list2.append(list1)
                        list1 = [input_time, [], [lang], [3]]
            index += 1
        return list2

    def decide_if_is_splittable(self, word):
        # Return type of sentence by character in string
        if chr(63) in word:
            return MetadataEnum.QUESTION
        elif chr(33) in word:
            return MetadataEnum.ORDER
        elif chr(10) in word:
            return MetadataEnum.SENTENCE
        elif chr(46) in word:
            word = self.decide_if_replace_end_char(word)
            if chr(46) in word:
                return MetadataEnum.ERROR
            else:
                return MetadataEnum.SENTENCE
        else:
            return MetadataEnum.ERROR

    def decide_if_replace_end_char(self, word):
        # Replace split character if is ending sentence
        if chr(63) in word:
            word = word[:word.index(chr(63))]
        elif chr(33) in word:
            word = word[:word.index(chr(33))]
        elif chr(10) in word:
            word = word[:word.index(chr(10))]
        elif chr(46) in word and not self.framework.process_support.has_string_numbers(word):
            if not NonLangOrientation.is_initialized:
                self.framework.databases.load_sdb_table_to_attribute(NonLangOrientation, "")
                NonLangOrientation.is_initialized = True
            passable = True
            if word != chr(46):
                if word in NonLangOrientation.abbreviation:
                    passable = False
                else:
                    if word[word.index(chr(46)):] in NonLangOrientation.file_types and word[
                                                                                       word.index(chr(46)):] != chr(46):
                        passable = False
                    elif word[word.index(chr(46)):] in NonLangOrientation.t_l_d and word[word.index(chr(46)):] != chr(
                            46):
                        passable = False

            if passable:
                word = word[:word.index(chr(46))]
        return word

    def treatment_entry(self, text):
        # Run saved sequence or process text another way with input_treatment
        seq_code = self.framework.databases.check_if_entry_exist_in_sequences(text)
        if seq_code:
            CoreModel.current_synapse_model = self.framework.event_player.run_sequence_by_table_name(seq_code, False, 0)
            self.append_to_key_list_if_recording(seq_code)
        else:
            synapse_model = SynapseModel()
            synapse_model.data = self.user_input_to_synapse_model(text, datetime.now(), [MetadataEnum.USER,
                                                                                         MetadataEnum.INPUT,
                                                                                         MetadataEnum.SENTENCE])
            synapse_model = self.sequences.input_treatment.run(synapse_model)
            if synapse_model:
                CoreModel.current_synapse_model = synapse_model
                self.append_to_key_list_if_recording()

    def append_to_key_list_if_recording(self, seq_code=None):
        # Append indexed entry to key list while running recording
        if not GUIModel.turn_off_listeners:
            if seq_code:
                self.framework.listeners.append_sequence_to_key_list(seq_code)
            else:
                tbl = self.framework.databases.get_all_current_entity("SEQUENCES")
                self.framework.listeners.append_sequence_to_key_list(tbl[-1][0])
