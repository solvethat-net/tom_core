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

from framework.modules.languages.core.ru.model.DetermineModel import DetermineModel
from framework.modules.languages.core.ru.model.MetadataSynonym import MetadataSynonym


class Determining(DetermineModel, MetadataSynonym):

    def __init__(self):
        return

    def add_member(self, metadata):
        if metadata not in DetermineModel.members[DetermineModel.index_in_sentence]:
            DetermineModel.members[DetermineModel.index_in_sentence].append(metadata)

    def determine_metadata_by_name(self, word):
        meta = None
        for one in MetadataSynonym.synonyms:
            if word in one[1]:
                meta = one[0]
        return meta
