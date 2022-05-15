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
# Class SequencesSupport
class SequencesSupport:

    def is_sequence(self, code):
        from framework.modules.sequences_support.core.TypeDeterminer import TypeDeterminer
        return TypeDeterminer().is_sequence(code)

    def is_condition(self, code):
        from framework.modules.sequences_support.core.TypeDeterminer import TypeDeterminer
        return TypeDeterminer().is_condition(code)

    def is_watcher(self, code):
        from framework.modules.sequences_support.core.TypeDeterminer import TypeDeterminer
        return TypeDeterminer().is_watcher(code)

# End of class SequencesSupport
