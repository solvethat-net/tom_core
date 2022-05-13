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


class MetadataSynonym:
    orders = [MetadataEnum.CREATE, MetadataEnum.DELETE, MetadataEnum.MOVE, MetadataEnum.COPY, MetadataEnum.CUT,
              MetadataEnum.OPEN, MetadataEnum.SEND, MetadataEnum.WRITE, MetadataEnum.CHECK, MetadataEnum.ERASE,
              MetadataEnum.WAIT, MetadataEnum.UPLOAD, MetadataEnum.START]
    synonyms = [
        [MetadataEnum.CREATE, " Создать "],
        [MetadataEnum.DELETE, " Удалить "],
        [MetadataEnum.MOVE, " Переместить "],
        [MetadataEnum.COPY, " скопировать "],
        [MetadataEnum.CUT, " вырезать "],
        [MetadataEnum.OPEN, " открыть "],
        [MetadataEnum.SEND, " отправить "],
        [MetadataEnum.WRITE, " записать "],
        [MetadataEnum.CHECK, " проверить "],
        [MetadataEnum.ERASE, " стереть "],
        [MetadataEnum.WAIT, " ждать "],
        [MetadataEnum.UPLOAD, " загрузить "],
        [MetadataEnum.START, " запустить "],
        [MetadataEnum.FILE, " файл "],
        [MetadataEnum.DIRECTORY, " директория "],
    ]
