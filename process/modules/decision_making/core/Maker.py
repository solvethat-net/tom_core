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

from core_util.MetadataEnum import MetadataEnum
from framework.Framework import Framework
from process.Process import Process


class Maker:

    def __init__(self):
        self.framework = Framework()
        self.process = Process()

    def define_user_input_type_and_process_it(self, synapse_model):
        # Method define type of user input and call process
        orders = [MetadataEnum.CREATE, MetadataEnum.DELETE, MetadataEnum.MOVE, MetadataEnum.COPY, MetadataEnum.CUT,
                  MetadataEnum.OPEN, MetadataEnum.SEND, MetadataEnum.WRITE, MetadataEnum.CHECK, MetadataEnum.ERASE,
                  MetadataEnum.WAIT, MetadataEnum.UPLOAD, MetadataEnum.START]
        for one in synapse_model.data:
            if one[3][1] == MetadataEnum.QUESTION:
                pass
                # synapse_model = self.process.current_database.readTreatment(synapse_model)
            else:
                bool_order = False
                target_metadata = None
                for meta_one in one[2]:
                    for meta in meta_one:
                        if meta in orders:
                            bool_order = True
                        if meta == MetadataEnum.FILE or meta == MetadataEnum.DIRECTORY:
                            target_metadata = meta
                if bool_order:
                    if target_metadata == MetadataEnum.FILE:
                        synapse_model = self.process.filesystem_controlling.control_file(synapse_model)

                    if target_metadata == MetadataEnum.DIRECTORY:
                        synapse_model = self.process.filesystem_controlling.control_dir(synapse_model)
                else:
                    # TODO topic ??
                    # synapse_model = self.process.current_database.writeTreatment(synapse_model)
                    pass
        return synapse_model
