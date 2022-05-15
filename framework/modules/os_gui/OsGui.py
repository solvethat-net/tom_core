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

# Generated 2022-05-15 19:54:37.818594
# Class OsGui
class OsGui:

    def getOSobject(self, osMetadata):
        from framework.modules.os_gui.core.GUIQueryTreatment import GUIQueryTreatment
        return GUIQueryTreatment().getOSobject(osMetadata)

    def getCurrentDir(self):
        from framework.modules.os_gui.core.GUIQueryTreatment import GUIQueryTreatment
        return GUIQueryTreatment().getCurrentDir()

    def getWindowTitle(self, **kwargs):
        from framework.modules.os_gui.core.GUIQueryTreatment import GUIQueryTreatment
        return GUIQueryTreatment().getWindowTitle(**kwargs)

    def getActualWindow(self, **kwargs):
        from framework.modules.os_gui.core.GUIQueryTreatment import GUIQueryTreatment
        return GUIQueryTreatment().getActualWindow(**kwargs)

# End of class OsGui
