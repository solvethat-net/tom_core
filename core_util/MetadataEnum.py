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

from enum import auto, Enum


class MetadataEnum(Enum):
    # Konvence metadat :
    # Zdroj dat, typ/druh dat, stav dat
    #  pro zdroj a typ/druh- pouze pod. jm nebo sloveso v infinitivu
    #  pro stav dat- pridavne jmeno nebo sloveso v minulem case stredniho rodu
    # Nesmi obsahovat synonima nebo stejne vyznamove dva prvky
    MOUSE_LEFT = auto()
    MOUSE_RIGHT = auto()
    MOUSE_MIDDLE = auto()
    MOUSE_MOVE = auto()
    MOUSE_SCROLL = auto()
    CONDITION_MOUSE_POSITION = auto()

    SEQUENCE = auto()
    WATCHER = auto()

    TOLERANT = auto()
    STRICT = auto()

    LIST = auto()
    QUESTION = auto()
    ORDER = auto()
    SENTENCE = auto()
    USER = auto()
    AVATAR = auto()
    SYSTEM = auto()
    SOURCE = auto()
    PRINT = auto()
    PRINTED = auto()
    INPUT = auto()
    OUTPUT = auto()
    OK = auto()
    ERROR = auto()
    FILE = auto()
    DIRECTORY = auto()
    NAME = auto()
    PATH = auto()
    URL = auto()
    WINDOWS = auto()
    LINUX = auto()
    MAC_OS = auto()

    CREATE = auto()
    CREATED = auto()
    DELETE = auto()
    DELETED = auto()
    MOVE = auto()
    MOVED = auto()
    COPY = auto()
    COPIED = auto()
    CUT = auto()
    CUTTED = auto()
    OPEN = auto()
    OPENED = auto()
    FIND = auto()
    FOUND = auto()
    SEND = auto()
    SENT = auto()
    WRITE = auto()
    WROTE = auto()
    CHECK = auto()
    CHECKED = auto()
    ERASE = auto()
    ERASED = auto()
    WAIT = auto()
    WAITED = auto()
    RENAME = auto()
    RENAMED = auto()
    UPLOAD = auto()
    UPLOADED = auto()
    START = auto()
    END = auto()
    CLOSE = auto()
    CLOSED = auto()
    NOUN = auto()
    VERB_PAST = auto()
    VERB_PRES = auto()
    VERB_INF = auto()
    VERB_DEF = auto()
    VERB_IMP = auto()
    PRONOUN = auto()
    PRONOUN_REVERSE = auto()
    OWNERSHIP = auto()
    COUPLES = auto()
    ADVERB = auto()
    PREPOSITIONS = auto()
    PARTICLE = auto()
    INTERJECTION = auto()
    PARTNERSHIP = auto()
    CONSEQUENCE = auto()
    EXPLANATION = auto()
    OPPOSITION = auto()
    EXCLUDE = auto()
    ADMISSION = auto()
    CONDITION = auto()
    LOOP = auto()
    CAUSE = auto()
    ORIGIN = auto()
    PLACE = auto()
    WAY = auto()
    TIME = auto()
    NUMERAL = auto()
    ADJECTIVE = auto()
    COUPLINGS = auto()
    SUBJECT = auto()
    CONTENT = auto()
    HTML = auto()
    MOUSE = auto()
    KEYBOARD = auto()
