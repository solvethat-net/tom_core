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

import sqlite3

from core_util.CoreModel import CoreModel
from framework.Framework import Framework
from ui.Ui import Ui


class Connector(CoreModel):

    def __init__(self):
        self.all_entity = []
        self.certain_data = []
        self.connection = None
        self.cursor = None
        self.ui = Ui()
        self.framework = Framework()

    def open_connection(self, path):
        # Open database connection
        # TODO get slash by OS - win=92,linux=47
        try:
            self.connection = sqlite3.connect(path)
            self.cursor = self.connection.cursor()
            return self.cursor
        except:
            self.ui.terminal.print_warn_log("Error while opening connection '" + path + "'")

    def close_connection(self):
        # Close database connection
        self.connection.commit()
        self.connection.close()

    def get_table_size(self, entity_name):
        # Get length of table by number of lines
        try:
            self.cursor.execute("SELECT * FROM " + entity_name)
            size = len(self.cursor.fetchall())
            return size
        except:
            self.ui.terminal.print_warn_log("Error while reading table '" + entity_name + "'")

    def delete_entity(self, entity_name):
        # Delete entity by name argument
        try:
            self.cursor.execute("DROP TABLE " + entity_name)
            self.ui.terminal.print_info_log("Table '" + entity_name + "' successfully deleted")
        except:
            self.ui.terminal.print_warn_log("Error while deleting table '" + entity_name + "'")

    def get_all_entity_content(self, entity_name):
        # Get all data from table
        try:
            self.cursor.execute("SELECT * FROM " + entity_name)
            all_entity = self.cursor.fetchall()
            return all_entity
        except:
            self.ui.terminal.print_warn_log("Error while reading table '" + entity_name + "'")
            return False
