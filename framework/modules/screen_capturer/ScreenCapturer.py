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

# Generated 2022-05-08 22:04:12.081266
# Class ScreenCapturer
class ScreenCapturer:

    def start_recording_all_screen(self):
        from framework.modules.screen_capturer.core.ScreenRecord import ScreenRecord
        return ScreenRecord().start_recording_all_screen()

    def stop_recording_all_screen(self):
        from framework.modules.screen_capturer.core.ScreenRecord import ScreenRecord
        return ScreenRecord().stop_recording_all_screen()

    def start_recording_area(self):
        from framework.modules.screen_capturer.core.ScreenRecord import ScreenRecord
        return ScreenRecord().start_recording_area()

    def stop_recording_area(self):
        from framework.modules.screen_capturer.core.ScreenRecord import ScreenRecord
        return ScreenRecord().stop_recording_area()

    def capture_area(self, x1, y1, x2, y2):
        from framework.modules.screen_capturer.core.ScreenShot import ScreenShot
        return ScreenShot().capture_area(x1, y1, x2, y2)

    def capture_screen(self):
        from framework.modules.screen_capturer.core.ScreenShot import ScreenShot
        return ScreenShot().capture_screen()

# End of class ScreenCapturer
