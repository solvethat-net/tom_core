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
# Class EventPlayer
class EventPlayer:

    def run_sequence_by_table_name(self, uuid, custom_delay):
        from framework.modules.event_player.core.Player import Player
        return Player().run_sequence_by_table_name(uuid, custom_delay)

    def find_log_enum_in_uuid(self, uuid):
        from framework.modules.event_player.core.Player import Player
        return Player().find_log_enum_in_uuid(uuid)

    def run_process_method_by_log_enum(self, method, synapse_model):
        from framework.modules.event_player.core.Player import Player
        return Player().run_process_method_by_log_enum(method, synapse_model)

    def treatment_condition(self, uuid, custom_delay):
        from framework.modules.event_player.core.Player import Player
        return Player().treatment_condition(uuid, custom_delay)

    def treatment_watcher(self, uuid, custom_delay):
        from framework.modules.event_player.core.Player import Player
        return Player().treatment_watcher(uuid, custom_delay)

    def check_suspend(self):
        from framework.modules.event_player.core.Player import Player
        return Player().check_suspend()

    def run_stop_handler(self):
        from framework.modules.event_player.core.Player import Player
        return Player().run_stop_handler()

    def break_running(self):
        from framework.modules.event_player.core.Player import Player
        return Player().break_running()

    def suspend_running(self):
        from framework.modules.event_player.core.Player import Player
        return Player().suspend_running()

    def wait_for_resume(self):
        from framework.modules.event_player.core.Player import Player
        return Player().wait_for_resume()

    def resume(self):
        from framework.modules.event_player.core.Player import Player
        return Player().resume()

    def change_delay(self, delay):
        from framework.modules.event_player.core.Player import Player
        return Player().change_delay(delay)

# End of class EventPlayer
