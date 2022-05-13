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

# Generated 2022-05-08 22:04:12.091140
# Class DecisionMaking
import datetime
from core_util.LogEnum import LogEnum


class DecisionMaking:

    def define_user_input_type_and_process_it(self, synapse_model):
        from process.modules.decision_making.core.Treatment import Treatment
        synapse_model.log.append([datetime.datetime.now(), LogEnum.decision_making_define_user_input_type_and_process_it,""])
        return Treatment().define_user_input_type_and_process_it(synapse_model)

# End of class DecisionMaking
