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
# Class IoStreams
class IoStreams:

    def appendContentToFile(self, filepath, contentToAppend):
        from framework.modules.io_streams.core.FileRequests import FileRequests
        return FileRequests().appendContentToFile(filepath, contentToAppend)

    def overwriteFileContent(self, filepath, newContent):
        from framework.modules.io_streams.core.FileRequests import FileRequests
        return FileRequests().overwriteFileContent(filepath, newContent)

    def getReadStream(self, filepath):
        from framework.modules.io_streams.core.FileRequests import FileRequests
        return FileRequests().getReadStream(filepath)

    def getFileContent(self, filepath):
        from framework.modules.io_streams.core.FileRequests import FileRequests
        return FileRequests().getFileContent(filepath)

    def getFileLines(self, filepath):
        from framework.modules.io_streams.core.FileRequests import FileRequests
        return FileRequests().getFileLines(filepath)

    def getSourceFromUrl(self, url):
        from framework.modules.io_streams.core.UrlRequests import UrlRequests
        return UrlRequests().getSourceFromUrl(url)

    def httpGETRequest(self, url, params):
        from framework.modules.io_streams.core.UrlRequests import UrlRequests
        return UrlRequests().httpGETRequest(url, params)

    def httpPOSTRequest(self, url, params):
        from framework.modules.io_streams.core.UrlRequests import UrlRequests
        return UrlRequests().httpPOSTRequest(url, params)

# End of class IoStreams
