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

class FileRequests:

    def __init__(self):
        return

    def appendContentToFile(self, filepath, contentToAppend):
        # Append content to existing file
        file = open(filepath, "a+")
        file.write(contentToAppend.encode("utf8"))
        file.close()

    def overwriteFileContent(self, filepath, newContent):
        # Write to file as to new file what overwrite content existing file
        file = open(filepath, "w+")
        file.write(newContent)
        file.close()

    def getReadStream(self, filepath):
        # Get input read stream for file on file path
        return open(filepath, "r", encoding="utf-8")

    def getFileContent(self, filepath):
        # Get all content of file on file path
        stream = self.getReadStream(filepath)
        fileContent = stream.read()
        stream.close()
        return fileContent

    def getFileLines(self, filepath):
        # Get all lines of file on file path
        stream = self.getReadStream(filepath)
        fileContentLines = stream.readlines()
        stream.close()
        return fileContentLines
