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

from framework.Framework import Framework
from framework.modules.languages.core.cs.Determining import Determining
from framework.modules.languages.core.cs.model.DetermineModel import DetermineModel
from framework.modules.languages.core.cs.model.OrientationModel import OrientationModel


class Cs(DetermineModel, OrientationModel):

    def __init__(self):
        self.determinate = Determining()
        self.service = Framework()

    def generate_cs(self):
        return self.generator.startGenerating()

    def determine_metadata_cs(self, sentence):
        if not DetermineModel.initialized:
            self.service.system_database.load_sdb_table_to_attribute(OrientationModel, "cs")
            DetermineModel.initialized = True
        # Restart variables on sentence process start
        DetermineModel.index_in_sentence = 0
        DetermineModel.preposition = False

        DetermineModel.phrase = ""
        DetermineModel.members = []
        # Use parser for all indexes of sentence
        for workVar in sentence:
            DetermineModel.members.append([])
            DetermineModel.verb = False
            self.determinate.determine_word(workVar)
            DetermineModel.index_in_sentence += 1
        return DetermineModel.members

    def post_process_verb_cs(self, workVar):
        self.determinate.verbProcessing(workVar)
