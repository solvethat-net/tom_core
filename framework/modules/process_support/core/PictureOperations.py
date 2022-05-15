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
from PIL import ImageChops
import math, operator
import cv2
import numpy

from framework.Framework import Framework


class PictureOperations:

    def __init__(self):
        self.framework = Framework()

    def convert_base64_to_numpy_arr(self, data):
        # Convert data param in base64 to numpy array
        image_base64_string = data.encode('ascii')
        img_bytes = base64.b64decode(image_base64_string)
        img_arr = numpy.frombuffer(img_bytes, dtype=numpy.uint8)
        np_arr = cv2.imdecode(img_arr, flags=cv2.IMREAD_COLOR)
        return np_arr

    # def rmsdiff(im1, im2):
    #     "Calculate the root-mean-square difference between two images"
    #
    #     h = ImageChops.difference(im1, im2).histogram()
    #
    #     # calculate rms
    #     return math.sqrt(reduce(operator.add,
    #                             map(lambda h, i: h * (i ** 2), h, range(256))
    #                             ) / (float(im1.size[0]) * im1.size[1]))

    def equal(im1, im2):
        return ImageChops.difference(im1, im2).getbbox() is None
