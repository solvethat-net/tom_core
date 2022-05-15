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

# Generated 2021-04-28 16:22:32.146942
# Class LogEnum
from enum import Enum


class LogEnum(Enum):
    current_database_write_synapse_model = ["current_database", "write_synapse_model"]
    current_database_create_new_sequence = ["current_database", "create_new_sequence"]
    current_database_create_new_condition = ["current_database", "create_new_condition"]
    current_database_create_new_watcher = ["current_database", "create_new_watcher"]
    current_database_read_treatment = ["current_database", "read_treatment"]
    decision_making_define_user_input_type_and_process_it = ["decision_making", "define_user_input_type_and_process_it"]
    filesystem_controlling_control_dir = ["filesystem_controlling", "control_dir"]
    filesystem_controlling_control_file = ["filesystem_controlling", "control_file"]
    metadata_obtaining_treatment_data = ["metadata_obtaining", "treatment_data"]
    metadata_obtaining_treatment_non_lang_expressions = ["metadata_obtaining", "treatment_non_lang_expressions"]
    source_reading_treatment_source = ["source_reading", "treatment_source"]
    user_interaction_print_terminal_output = ["user_interaction", "print_terminal_output"]
    user_interaction_run_terminal_user_input_once = ["user_interaction", "run_terminal_user_input_once"]
