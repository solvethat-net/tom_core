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

import os
import shutil

from core_util.MetadataEnum import MetadataEnum
from framework.modules.filesystem.core.objects.ParentObject import ParentObject


class Directory(ParentObject):

    def copy(self):
        shutil.copytree(self.input, self.output)
        return MetadataEnum.COPIED

    def delete(self):
        shutil.rmtree(self.input)
        return MetadataEnum.DELETED

    def create(self):
        os.mkdir(self.input)
        return MetadataEnum.CREATED

    def move(self):
        shutil.move(self.input, self.output)
        return MetadataEnum.MOVED

    def open(self):
        os.startfile(self.input)
        return MetadataEnum.OPENED

    def close(self):
        # TODO
        pass

    def find(self):
        # TODO https: // stackoverflow.com / questions / 13067686 / search - files - in -all - drives - using - python
        pass

    def rename(self):
        os.rename(self.input, self.output)
        return MetadataEnum.RENAMED

    def check_exist(self, path):
        return os.path.isdir(path)

