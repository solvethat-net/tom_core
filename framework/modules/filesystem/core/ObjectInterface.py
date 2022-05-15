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

from framework.modules.filesystem.core.objects.Directory import Directory
from framework.modules.filesystem.core.objects.File import File


class ObjectInterface:

    def __init__(self):
        self.file = File()
        self.directory = Directory()

    # Getter of file object
    def get_file(self):
        return self.file

    # Getter of directory object
    def get_dir(self):
        return self.directory
