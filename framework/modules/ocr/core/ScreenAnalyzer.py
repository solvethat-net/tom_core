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

import base64
import cv2
import numpy as np
from framework.Framework import Framework
from ui.Ui import Ui


class ScreenAnalyzer:

    # TODO pozice na ktere je sub img nalezen je zkreslena pokud je zapojeno vice displayu
    # TODO Indexy casto obsahuji vice pozic !!!!

    def __init__(self):
        self.framework = Framework()
        self.ui = Ui()

    def find_image_on_screen(self, sub_image_base64_string, threshold):
        # Find base64 image on screen
        # Convert 'sub_image_base64' variable to numpy array
        sub_image_base64 = sub_image_base64_string.encode('ascii')
        sub_img_bytes = base64.b64decode(sub_image_base64)
        sub_img_arr = np.frombuffer(sub_img_bytes, dtype=np.uint8)
        sub_img = cv2.imdecode(sub_img_arr, flags=cv2.IMREAD_COLOR)
        # Get screen shot as base64 string and convert to numpy array
        screen_img_base64_string = self.framework.screen_capturer.capture_screen()
        screen_img_bytes = base64.b64decode(screen_img_base64_string)
        screen_img_arr = np.frombuffer(screen_img_bytes, dtype=np.uint8)
        screen_img = cv2.imdecode(screen_img_arr, flags=cv2.IMREAD_COLOR)
        result = cv2.matchTemplate(sub_img, screen_img, cv2.TM_CCOEFF_NORMED)

        location = np.where(result >= threshold)
        if len(location[0]) and len(location[1]):
            self.ui.terminal.print_info_log("Image found on screen")
            return [location[1], location[0]]
        else:
            self.ui.terminal.print_warn_log("Image not found on screen")
            return False

    def find_image_in_image(self, image_base64, sub_image_base64_string, threshold):
        # Find base64 image in another image
        # Convert 'sub_image_base64' variable to numpy array
        sub_image_base64 = sub_image_base64_string.encode('ascii')
        sub_img_bytes = base64.b64decode(sub_image_base64)
        sub_img_arr = np.frombuffer(sub_img_bytes, dtype=np.uint8)
        sub_img = cv2.imdecode(sub_img_arr, flags=cv2.IMREAD_COLOR)

        # sub_image_base64 = image_base64_string.encode('ascii')
        sub_img_bytes = base64.b64decode(image_base64)
        sub_img_arr = np.frombuffer(sub_img_bytes, dtype=np.uint8)
        img = cv2.imdecode(sub_img_arr, flags=cv2.IMREAD_COLOR)

        result = cv2.matchTemplate(sub_img, img, cv2.TM_CCOEFF_NORMED)

        location = np.where(result >= threshold)
        if len(location[0]) and len(location[1]):
            self.ui.terminal.print_info_log("Image found on screen")
            return [location[1], location[0]]
        else:
            self.ui.terminal.print_warn_log("Image not found on screen")
            return False
