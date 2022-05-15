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
from core_util.SynapseModel import SynapseModel


class CoreModel:
    avatar = "Tom AI"
    user_name = "Sick-E"
    language_list = ["en-GB", "es-ES", "fr-FR", "ru-RU", "it-IT", "pl-PL", "cs-CS", "sk-SK"]
    OS = MetadataEnum.WINDOWS
    root_path = None
    topic = ""
    current_synapse_model = SynapseModel()
    current_db_file_path = None
