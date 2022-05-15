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
# Class NonLangExpressions
class NonLangExpressions:

    def determine(self, synapse_model):
        from framework.modules.non_lang_expressions.core.Determining import Determining
        return Determining().determine(synapse_model)

    def add_link(self, link):
        from framework.modules.non_lang_expressions.core.Determining import Determining
        return Determining().add_link(link)

    def find_shortcut(self, meta_index):
        from framework.modules.non_lang_expressions.core.Determining import Determining
        return Determining().find_shortcut(meta_index)

    def get_slash_kind(self, link):
        from framework.modules.non_lang_expressions.core.Determining import Determining
        return Determining().get_slash_kind(link)

    def path_recognizing(self, data_index):
        from framework.modules.non_lang_expressions.core.Determining import Determining
        return Determining().path_recognizing(data_index)

    def links_postprocessing(self):
        from framework.modules.non_lang_expressions.core.Determining import Determining
        return Determining().links_postprocessing()

# End of class NonLangExpressions
