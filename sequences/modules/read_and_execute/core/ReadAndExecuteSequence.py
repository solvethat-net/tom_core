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

from core_util.CoreModel import CoreModel
from process.Process import Process


class ReadAndExecuteSequence(CoreModel):

    def __init__(self):
        self.process = Process()

    def run(self, synapse_model):
        synapse_model = self.process.metadata_obtaining.treatment_non_lang_expressions(synapse_model)
        synapse_model = self.process.source_reading.treatment_source(synapse_model)
        synapse_model = self.process.metadata_obtaining.treatment_data(synapse_model)
        synapse_model = self.process.current_database.write_synapse_model(synapse_model)
        return synapse_model
