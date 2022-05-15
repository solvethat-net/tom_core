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

from datetime import datetime

from core_util.LogEnum import LogEnum
from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework


class Reader:

    def __init__(self):
        self.framework = Framework()

    def treatment_source(self, synapse_model):
        path_to_source = ""
        for one in synapse_model.data[-1][2]:
            if MetadataEnum.INPUT in one:
                path_to_source = synapse_model.data[-1][1][synapse_model.data[-1][2].index(one)]
        if path_to_source:
            if self.framework.source_code.recognizeUrl(path_to_source):
                source_content = self.framework.io_streams.getSourceFromUrl(path_to_source)
            else:
                source_content = self.framework.io_streams.getFileLines(path_to_source)
            source_content_type_metadata = self.framework.source_code.recognizeSourceCodeType(source_content)
            if source_content_type_metadata == MetadataEnum.HTML:
                source_content = self.framework.source_code.treatmentHtml(source_content)
            synapse_model.data.extend(
                self.framework.process_support.user_input_to_synapse_model(
                    source_content,
                    datetime.now(),
                    [MetadataEnum.USER, MetadataEnum.INPUT, MetadataEnum.SENTENCE]))
            synapse_model.log.append(
                [datetime.now(), LogEnum.SourceReading_treatmentSource,
                 self.framework.process_support.set_topic_by_first_line(synapse_model)])
        return synapse_model
