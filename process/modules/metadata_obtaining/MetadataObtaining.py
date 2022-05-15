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

# Generated 2022-05-15 19:54:37.818594
# Class MetadataObtaining
import datetime
from core_util.LogEnum import LogEnum


class MetadataObtaining:

    def treatment_data(self, synapse_model):
        from process.modules.metadata_obtaining.core.Obtainer import Obtainer
        synapse_model.log.append([datetime.datetime.now(), LogEnum.metadata_obtaining_treatment_data,""])
        return Obtainer().treatment_data(synapse_model)

    def treatment_non_lang_expressions(self, synapse_model):
        from process.modules.metadata_obtaining.core.Obtainer import Obtainer
        synapse_model.log.append([datetime.datetime.now(), LogEnum.metadata_obtaining_treatment_non_lang_expressions,""])
        return Obtainer().treatment_non_lang_expressions(synapse_model)

# End of class MetadataObtaining
