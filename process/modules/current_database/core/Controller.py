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

import datetime
import uuid
from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from ui.Ui import Ui


class Controller(CoreModel):

    def __init__(self):
        self.framework = Framework()
        self.ui = Ui()
        self.error_enum = [MetadataEnum.SYSTEM, MetadataEnum.OUTPUT, MetadataEnum.ERROR]
        self.ok_enum = [MetadataEnum.SYSTEM, MetadataEnum.OUTPUT, MetadataEnum.OK]

    def write_synapse_model(self, synapse_model):
        # Treatment data for self.write, check if data exist and call self.write index by index
        topic = CoreModel.topic
        self.ui.terminal.print_info_log("Checking if table " + CoreModel.topic + " exist")
        if self.framework.databases.get_all_sequence_entity(CoreModel.topic):
            for index in synapse_model.data:
                certain_data = self.framework.databases.get_certain_data(index)
                if certain_data:
                    db_result = self.framework.process_support.sort_data_by_score(certain_data)
                    db_result = self.framework.process_support.compare_lists(synapse_model.data, db_result)
                    if not db_result:
                        synapse_model.data[synapse_model.data.index(index)][3][2] = self.call_write_0(index, topic)
                    else:
                        synapse_model.data[synapse_model.data.index(index)][3][2] = MetadataEnum.ERROR
                else:
                    synapse_model.data[synapse_model.data.index(index)][3][2] = self.call_write_0(index, topic)
        else:
            for index in synapse_model.data:
                synapse_model.data[synapse_model.data.index(index)][3][2] = self.call_write_0(index, topic)
        return synapse_model

    def create_new_sequence(self, synapse_model):
        # Generate UUID and new name for save to table SEQUENCES
        CoreModel.topic = "S" + chr(95) + str(uuid.uuid4()).replace(chr(45), chr(95))
        self.write_synapse_model(synapse_model)
        str_uuid = CoreModel.topic
        date_time_now = str(datetime.datetime.now())
        title = "Unnamed sequence " + date_time_now[2:date_time_now.rindex(chr(46))]
        if len(synapse_model.log) > 1:
            str_uuid = synapse_model.log[-2][1].value
            str_uuid = str_uuid[0] + chr(46) + str_uuid[1] + chr(58) + CoreModel.topic
        if len(synapse_model.data) == 1:
            index = synapse_model.data[0]
            index[1] = index[1][0:-1]
            title = self.framework.process_support.transform_data_index_to_string(index)[1]
        self.framework.databases.write_to_sequence_table([str_uuid, title])

    def create_new_condition(self, data, true, false, threshold, position):
        # Generate UUID and save to table CONDITIONS
        CoreModel.topic = "C" + chr(95) + str(uuid.uuid4()).replace(chr(45), chr(95))
        date_time_now = str(datetime.datetime.now())
        title = "Unnamed condition " + date_time_now[2:date_time_now.rindex(chr(46))]
        self.framework.databases.write_to_conditions_table(
            [CoreModel.topic, title, data, true, false, threshold, position])

    def create_new_watcher(self, data, true, false, threshold, position):
        # Generate UUID and save to table CONDITIONS as watcher
        CoreModel.topic = "W" + chr(95) + str(uuid.uuid4()).replace(chr(45), chr(95))
        date_time_now = str(datetime.datetime.now())
        title = "Unnamed watcher " + date_time_now[2:date_time_now.rindex(chr(46))]
        self.framework.databases.write_to_conditions_table(
            [CoreModel.topic, title, data, true, false, threshold, position])

    def call_write_0(self, to_write, topic):
        # Call write method and return metadata enum
        return self.framework.databases.write_current_entity_line(
            self.framework.process_support.transform_data_index_to_string(to_write),
            topic)

    def read_treatment(self, synapse_model):
        # Check if data exist and get certain data by orientation
        certain_data = []
        if self.framework.databases.get_all_sequence_entity(synapse_model.log[-1][2]):
            for index in synapse_model.data:
                certain_data = self.framework.databases.get_certain_data(index)
            if certain_data:
                db_result = self.framework.process_support.sort_data_by_score(certain_data)
                for one in db_result:
                    db_result[db_result.index(one)] = one.extend(self.ok_enum)
                synapse_model.data = db_result
            else:
                for index in synapse_model.data:
                    synapse_model.data[synapse_model.data.index(index)][3] = self.error_enum
        else:
            for index in synapse_model.data:
                synapse_model.data[synapse_model.data.index(index)][3] = self.error_enum
        return synapse_model
