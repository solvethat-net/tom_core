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

from framework.Framework import Framework


class Controller:

    def __init__(self):
        self.framework = Framework()

    def control_dir(self, synapse_model):
        # Determine what kind of action do with directory
        return self.framework.process_support.set_and_run_by_metadata(self.framework.filesystem.get_dir(), synapse_model)

    def control_file(self, synapse_model):
        # Determine what kind of action do with file
        return self.framework.process_support.set_and_run_by_metadata(self.framework.filesystem.get_file(),
                                                                      synapse_model)
