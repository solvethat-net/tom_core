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

import base64
import io
import pyscreenshot


class ScreenShot:

    def __init__(self):
        return

    def capture_area(self, x1, y1, x2, y2):
        # Make screen shot of area and return image in base64
        im = pyscreenshot.grab(bbox=(x1, y1, x2, y2))
        buffer = io.BytesIO()
        im.save(buffer, format='JPEG')
        im.close()
        return base64.b64encode(buffer.getvalue())

    def capture_screen(self):
        # Make screen shot of all screen and return image in base64
        im = pyscreenshot.grab()
        buffer = io.BytesIO()
        im.save(buffer, format='JPEG')
        im.close()
        return base64.b64encode(buffer.getvalue())
