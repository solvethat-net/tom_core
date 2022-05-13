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

# USER DATABASE data create
import os
import sqlite3

# This script is initializing user database
# If you need to reset application you can run this script

# TODO NEEDS OWN GUI

# This part is checking if all dependencies are installed


# This part is creating new user database
db_path = str(os.path.dirname(os.path.abspath(__file__))).replace("core_util", "") + "database\\UDB.db"
connection = sqlite3.connect(db_path)
cursor = connection.cursor()

# 1. gui position
cursor.execute("CREATE TABLE CONFIG(configuration text, value text)")
cursor.execute("INSERT INTO CONFIG(configuration,value) VALUES('x_pos','0')")
cursor.execute("INSERT INTO CONFIG(configuration,value) VALUES('y_pos','0')")
cursor.execute("INSERT INTO CONFIG(configuration,value) VALUES('first_start','0')")
cursor.execute("INSERT INTO CONFIG(configuration,value) VALUES('language','en')")
cursor.execute("INSERT INTO CONFIG(configuration,value) VALUES('ocr_threshold','')")
cursor.execute("INSERT INTO CONFIG(configuration,value) VALUES('current_database','')")
# 2. paths = all dirs in \\\\user
cursor.execute("CREATE TABLE PATHS(shortcut text, path text)")
for one in os.listdir("C:\\Users\\" + os.getlogin()):
    if os.path.isdir("C:\\Users\\" + os.getlogin() + "\\" + one) and "." not in one:
        cursor.execute(
            "INSERT INTO PATHS VALUES('" + one.lower() + "','" + "C:\\Users\\" + os.getlogin() + "\\" + one + "')")
cursor.execute("CREATE TABLE DATABASES(path text, name text)")
connection.commit()
connection.close()
