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

# Generated 2022-05-15 19:54:37.818594
from process.modules.current_database.CurrentDatabase import CurrentDatabase
from process.modules.decision_making.DecisionMaking import DecisionMaking
from process.modules.filesystem_controlling.FilesystemControlling import FilesystemControlling
from process.modules.metadata_obtaining.MetadataObtaining import MetadataObtaining
from process.modules.user_interaction.UserInteraction import UserInteraction


class Process:
    current_database = CurrentDatabase()
    decision_making = DecisionMaking()
    filesystem_controlling = FilesystemControlling()
    metadata_obtaining = MetadataObtaining()
    user_interaction = UserInteraction()
# End of class Process
