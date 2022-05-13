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

# Generated 2022-05-08 22:04:12.081266
# Class Languages
class Languages:

    def generate_cs(self):
        from framework.modules.languages.core.Cs import Cs
        return Cs().generate_cs()

    def determine_metadata_cs(self, sentence):
        from framework.modules.languages.core.Cs import Cs
        return Cs().determine_metadata_cs(sentence)

    def post_process_verb_cs(self, workVar):
        from framework.modules.languages.core.Cs import Cs
        return Cs().post_process_verb_cs(workVar)

    def determine_metadata_en(self, sentence):
        from framework.modules.languages.core.En import En
        return En().determine_metadata_en(sentence)

    def determine_metadata_es(self, sentence):
        from framework.modules.languages.core.Es import Es
        return Es().determine_metadata_es(sentence)

    def determine_metadata_fr(self, sentence):
        from framework.modules.languages.core.Fr import Fr
        return Fr().determine_metadata_fr(sentence)

    def determine_metadata_it(self, sentence):
        from framework.modules.languages.core.It import It
        return It().determine_metadata_it(sentence)

    def determine_metadata_pl(self, sentence):
        from framework.modules.languages.core.Pl import Pl
        return Pl().determine_metadata_pl(sentence)

    def determine_metadata_ru(self, sentence):
        from framework.modules.languages.core.Ru import Ru
        return Ru().determine_metadata_ru(sentence)

    def determine_metadata_sk(self, sentence):
        from framework.modules.languages.core.Sk import Sk
        return Sk().determine_metadata_sk(sentence)

# End of class Languages
