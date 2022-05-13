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

import requests


class UrlRequests:

    def __init__(self):
        return

    def getSourceFromUrl(self, url):
        # Return source code from url
        return self.httpGETRequest(url, "").text

    def httpGETRequest(self, url, params):
        # Make http GET request with or without params
        if params:
            return requests.get(url, params)
        else:
            return requests.get(url)

    def httpPOSTRequest(self, url, params):
        # Make http POST request with or without params
        if params:
            return requests.post(url, params)
        else:
            return requests.post(url)
