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
# Class Listeners
class Listeners:

    def init_key_list(self):
        from framework.modules.listeners.core.KeyLogger import KeyLogger
        return KeyLogger().init_key_list()

    def get_recorded_data(self):
        from framework.modules.listeners.core.KeyLogger import KeyLogger
        return KeyLogger().get_recorded_data()

    def run_key_listener(self):
        from framework.modules.listeners.core.KeyLogger import KeyLogger
        return KeyLogger().run_key_listener()

    def run_mouse_listener(self):
        from framework.modules.listeners.core.KeyLogger import KeyLogger
        return KeyLogger().run_mouse_listener()

    def run_both(self):
        from framework.modules.listeners.core.KeyLogger import KeyLogger
        return KeyLogger().run_both()

    def stop_key_listener(self):
        from framework.modules.listeners.core.KeyLogger import KeyLogger
        return KeyLogger().stop_key_listener()

    def stop_mouse_listener(self):
        from framework.modules.listeners.core.KeyLogger import KeyLogger
        return KeyLogger().stop_mouse_listener()

    def stop_all(self):
        from framework.modules.listeners.core.KeyLogger import KeyLogger
        return KeyLogger().stop_all()

    def append_sequence_to_key_list(self, sequence_uuid):
        from framework.modules.listeners.core.SequenceAppender import SequenceAppender
        return SequenceAppender().append_sequence_to_key_list(sequence_uuid)

    def append_condition_to_key_list(self, condition_uuid):
        from framework.modules.listeners.core.SequenceAppender import SequenceAppender
        return SequenceAppender().append_condition_to_key_list(condition_uuid)

    def append_watcher_to_key_list(self, watcher_uuid):
        from framework.modules.listeners.core.SequenceAppender import SequenceAppender
        return SequenceAppender().append_watcher_to_key_list(watcher_uuid)

    def append_user_input_to_key_list(self, data):
        from framework.modules.listeners.core.SequenceAppender import SequenceAppender
        return SequenceAppender().append_user_input_to_key_list(data)

    def append_loop_sequence_to_key_list(self, uuid, loops):
        from framework.modules.listeners.core.SequenceAppender import SequenceAppender
        return SequenceAppender().append_loop_sequence_to_key_list(uuid, loops)

    def append_loop_condition_to_key_list(self, uuid, loops):
        from framework.modules.listeners.core.SequenceAppender import SequenceAppender
        return SequenceAppender().append_loop_condition_to_key_list(uuid, loops)

    def append_loop_watcher_to_key_list(self, uuid, loops):
        from framework.modules.listeners.core.SequenceAppender import SequenceAppender
        return SequenceAppender().append_loop_watcher_to_key_list(uuid, loops)

    def run_speech_listener(self):
        from framework.modules.listeners.core.SpeechListener import SpeechListener
        return SpeechListener().run_speech_listener()

    def stop_speech_listener(self):
        from framework.modules.listeners.core.SpeechListener import SpeechListener
        return SpeechListener().stop_speech_listener()

# End of class Listeners
