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
from framework.Framework import Framework
from framework.modules.non_lang_expressions.core.model.NonLangOrientation import NonLangOrientation


class Determining(NonLangOrientation):

    def __init__(self):
        self.framework = Framework()
        self.links = []
        self.additional_metadata = None

    def determine(self, synapse_model):
        # Determine if add other expressions metadata
        orders = [MetadataEnum.CREATE, MetadataEnum.DELETE, MetadataEnum.MOVE, MetadataEnum.COPY, MetadataEnum.CUT,
                  MetadataEnum.OPEN, MetadataEnum.SEND, MetadataEnum.WRITE, MetadataEnum.CHECK, MetadataEnum.ERASE,
                  MetadataEnum.WAIT, MetadataEnum.UPLOAD, MetadataEnum.START]
        if not NonLangOrientation.is_initialized:
            self.framework.databases.load_sdb_table_to_attribute(NonLangOrientation, "")
            NonLangOrientation.is_initialized = True
        for one in synapse_model.data:
            self.links = []
            self.additional_metadata = None
            for data_attribute in one[1]:
                self.path_recognizing(data_attribute)
            for meta_index in one[2]:
                self.find_shortcut(meta_index)
            if self.links:
                self.links_postprocessing()
                if self.additional_metadata != MetadataEnum.FILE:
                    bool_order_is_there = False
                    for another_one in synapse_model.data[2]:
                        for sub_one in another_one:
                            if sub_one in orders:
                                bool_order_is_there = True
                    if bool_order_is_there:
                        self.additional_metadata = MetadataEnum.DIRECTORY
                # Add metadata INPUT
                synapse_model.data[synapse_model.data.index(one)][1].append(self.links[0])
                if self.additional_metadata:
                    synapse_model.data[synapse_model.data.index(one)][2].append(
                        [MetadataEnum.INPUT, self.additional_metadata])
                else:
                    synapse_model.data[synapse_model.data.index(one)][2].append([MetadataEnum.INPUT])
                if len(self.links) == 2:
                    # Add metadata OUTPUT
                    synapse_model.data[synapse_model.data.index(one)][1].append(self.links[0])
                    if self.additional_metadata:
                        synapse_model.data[synapse_model.data.index(one)][2].append(
                            [MetadataEnum.OUTPUT, self.additional_metadata])
                    else:
                        synapse_model.data[synapse_model.data.index(one)][2].append([MetadataEnum.OUTPUT])
        return synapse_model

    def add_link(self, link):
        # Append link to list
        if link not in self.links:
            self.links.append(link)

    def find_shortcut(self, meta_index):
        # Find shortcut in all metadata
        paths = self.framework.databases.get_all_udb_entity("PATHS")
        for one in paths:
            if one[0].lower() in meta_index or one[0].lower() == meta_index:
                self.add_link(one[1])

    def get_slash_kind(self, link):
        # Return slash or backslash by link argument content
        if chr(92) in link and chr(47) not in link:
            return chr(92)
        elif chr(47) in link and chr(92) not in link:
            return chr(47)

    def path_recognizing(self, data_index):
        # Append link to array if link seem like path or url
        if "http" in data_index or chr(47) in data_index or chr(92) in data_index and len(data_index) > 1:
            self.add_link(data_index)
        self.find_shortcut(data_index)
        if chr(46) in data_index:
            just_end = data_index[data_index.index(chr(46)):]
            if chr(32) + just_end + chr(32) in NonLangOrientation.file_types:
                self.add_link(data_index)
                self.additional_metadata = MetadataEnum.FILE
            if chr(32) + just_end + chr(32) in NonLangOrientation.t_l_d:
                self.add_link(data_index)

    def links_postprocessing(self):
        # Postprocessing of URL or file path
        if len(self.links) == 1 and chr(47) not in self.links[0]:
            # TODO use actual user position in other applications
            pass
        else:
            slash_arr = []
            no_slash_arr = []
            for link in self.links:
                if chr(47) in link or chr(92) in link:
                    slash_arr.append(link)
                if chr(47) not in link and chr(92) not in link:
                    no_slash_arr.append(link)

            if len(slash_arr) == 1 and len(no_slash_arr) == 1:
                input_value = slash_arr[0] + self.get_slash_kind(slash_arr[0]) + no_slash_arr[0]
                self.links = [input_value]
            elif len(slash_arr) == 2 and len(no_slash_arr) == 2:
                input_value = slash_arr[0] + self.get_slash_kind(slash_arr[0]) + no_slash_arr[0]
                output = slash_arr[1] + self.get_slash_kind(slash_arr[1]) + no_slash_arr[1]
                self.links = [input_value, output]
            elif len(slash_arr) == 2 and len(no_slash_arr) == 1:
                if self.links.index(no_slash_arr[0]) == 0:
                    input_value = slash_arr[0] + self.get_slash_kind(slash_arr[0]) + no_slash_arr[0]
                    output = slash_arr[1]
                    self.links = [input_value, output]
                else:
                    input_value = slash_arr[0]
                    output = slash_arr[1] + self.get_slash_kind(slash_arr[1]) + no_slash_arr[0]
                    self.links = [input_value, output]
