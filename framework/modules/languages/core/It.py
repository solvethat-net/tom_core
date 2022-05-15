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

from framework.modules.languages.core.it.Determining import Determining
from framework.modules.languages.core.it.model.DetermineModel import DetermineModel


class It(DetermineModel):

    def __init__(self):
        self.determinate = Determining()

    def determine_metadata_it(self, sentence):
        DetermineModel.indexInSentence = 0
        DetermineModel.preposition = False
        DetermineModel.phrase = ""
        DetermineModel.members = []
        # Use parser for all indexes of sentence
        for workVar in sentence:
            DetermineModel.members.append([])
            DetermineModel.verb = False
            self.determinate.add_member(self.determinate.determine_metadata_by_name(workVar))
            DetermineModel.indexInSentence += 1
        return DetermineModel.members
