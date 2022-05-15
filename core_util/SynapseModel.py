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

class SynapseModel(object):

    def __init__(self):
        self.data = []  # [0 Time, 1 Data[], 2 Certain metadata[[],[]...], 3 General metadata [0=Source,1=Type,2=State]]
        self.log = []  # [0 Time, 1 Enum = [0 Module, 1 Interface method], 2 Topic]
