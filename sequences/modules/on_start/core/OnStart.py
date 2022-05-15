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

from core_util.CoreModel import CoreModel
from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from process.Process import Process
from ui.Ui import Ui


class OnStart(CoreModel):

    def __init__(self):
        self.framework = Framework()
        self.ui = Ui()
        self.process = Process()

    def run(self):
        self.process.core_update.update_core()
        res = self.framework.databases.get_current_config_value("current_database")
        if res != MetadataEnum.ERROR:
            if self.framework.filesystem.get_file().check_exist(res):
                CoreModel.current_db_file_path = res
            else:
                CoreModel.current_db_file_path = None
        else:
            CoreModel.current_db_file_path = None
        self.ui.gui.run_gui()
