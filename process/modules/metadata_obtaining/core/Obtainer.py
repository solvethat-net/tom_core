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

import importlib

from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from langdetect import detect
from framework.Framework import Framework
from ui.Ui import Ui


class Obtainer(CoreModel):

    def __init__(self):
        self.framework = Framework()
        self.ui = Ui()

    def content_indexing_0(self, sentence):
        # Locally import language module and call determineMetadata+LANG method
        if len(sentence) > 0:
            try:
                lang = detect(self.framework.process_support.convert_array_to_string(sentence))
            except ChildProcessError:
                # Set language by configuration
                lang = CoreModel.language_list[0]
                self.ui.terminal.print_warn_log("Language doesn't recognized")
            if chr(45) in lang:
                lang = lang[0:lang.index("-")]
            try:
                imported_class = getattr(importlib.import_module("framework.modules.languages.Languages"),
                                         "Languages")
                method = getattr(imported_class(), "determine_metadata_" + lang.lower())
                return method(sentence)
            except ImportError:
                self.ui.terminal.print_warn_log("Module import error")

    def treatment_data(self, synapse_model):
        # Obtain metadata from content indexing
        for one in synapse_model.data:
            metadata = self.content_indexing_0(one[1])
            if metadata != MetadataEnum.ERROR:
                synapse_model.data[synapse_model.data.index(one)][2] = metadata
                synapse_model.data[synapse_model.data.index(one)][3][2] = MetadataEnum.LIST
        return synapse_model

    def treatment_non_lang_expressions(self, synapse_model):
        # Obtain other metadata unrelated to language
        return self.framework.non_lang_expressions.determine(synapse_model)
