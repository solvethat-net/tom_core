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

from framework.Framework import Framework
from framework.modules.languages.core.cs.model.DetermineModel import DetermineModel
from core_util.MetadataEnum import MetadataEnum
from framework.modules.languages.core.cs.model.MetadataSynonym import MetadataSynonym
from framework.modules.languages.core.cs.model.OrientationModel import OrientationModel


class Determining(DetermineModel, OrientationModel, MetadataSynonym):

    def __init__(self):
        self.framework = Framework()

    def add_member(self, metadata):
        # Add metadata to list
        if metadata not in DetermineModel.members[DetermineModel.index_in_sentence]:
            DetermineModel.members[DetermineModel.index_in_sentence].append(metadata)

    def determine_metadata_by_name(self, word):
        # Find metadata in synonyms array
        meta = None
        for one in MetadataSynonym.synonyms:
            if word in one[1]:
                meta = one[0]
        return meta

    def determine_word(self, workVar):
        # Determine suitable metadata for word in sentence context
        # print(workVar)
        # .......................................................................................................Sloveso
        verb = False
        # Definiční slovesa
        if chr(32) + workVar + chr(32) in OrientationModel.verbs_def:
            verb = True
            self.add_member(MetadataEnum.VERB_DEF)

        # Minulý čas
        for onePast in OrientationModel.verbs_past:
            if chr(32) + workVar + chr(32) in onePast:
                verb = True
                self.add_member(MetadataEnum.VERB_PAST)
                DetermineModel.time[1] = True

        # Přítomný čas
        for onePresence in OrientationModel.verbs_presence:
            if chr(32) + workVar + chr(32) in onePresence:
                verb = True
                self.add_member(MetadataEnum.VERB_PRES)
                DetermineModel.time[0] = True

        # Rozkazovací způsob
        for oneImp in OrientationModel.verbs_imperative:
            if chr(32) + workVar + chr(32) in oneImp:
                verb = True
                self.add_member(MetadataEnum.VERB_IMP)
                infinit = OrientationModel.verbs_infinitive[OrientationModel.verbs_imperative.index(oneImp)]
                metadata = self.determine_metadata_by_name(infinit)
                if metadata:
                    self.add_member(metadata)

        # Infinitiv
        if workVar in OrientationModel.verbs_infinitive:
            self.add_member(MetadataEnum.VERB_INF)
            verb = True
            metadata = self.determine_metadata_by_name(workVar)
            if metadata:
                self.add_member(metadata)

        if not verb:
            # ...........................................................................................Podstatné jméno
            if chr(32) + workVar + chr(32) in OrientationModel.nouns or workVar == "kdo" or workVar == "co":
                self.add_member(MetadataEnum.NOUN)
                metadata = self.determine_metadata_by_name(workVar)
                if metadata:
                    self.add_member(metadata)
            else:
                koncovky = ["ata", "a", "e", "i", "í", "ně", "eň", "y"]
                for koncovka in koncovky:
                    if koncovka in workVar and workVar.index(koncovka) == (
                            len(workVar) - len(koncovka)):
                        self.add_member(MetadataEnum.NOUN)
            # ...................................................................................................Zájmena
            if chr(32) + workVar + chr(32) in OrientationModel.pronouns:
                self.add_member(MetadataEnum.PRONOUN)

            if workVar == "si" or workVar == "se":
                self.add_member(MetadataEnum.PRONOUN_REVERSE)

            # Prevod zajmen
            if workVar == "já":
                workVar = "ty"
                self.add_member(MetadataEnum.PRONOUN)

            if workVar == "ty":
                workVar = "já"
                self.add_member(MetadataEnum.PRONOUN)

            # ...............................................................................................Vlastnictví
            if chr(32) + workVar + chr(32) in OrientationModel.ownership:
                self.add_member(MetadataEnum.OWNERSHIP)

            # ....................................................................................................Spojky
            if chr(32) + workVar + chr(32) in OrientationModel.couplings:
                self.add_member(MetadataEnum.COUPLINGS)

            # .................................................................................................Příslovce
            if chr(32) + workVar + chr(32) in OrientationModel.adverb:
                self.add_member(MetadataEnum.ADVERB)

            # .................................................................................................Předložky
            if chr(32) + workVar + chr(32) in OrientationModel.prepositions:
                DetermineModel.preposition = True
                self.add_member(MetadataEnum.PREPOSITIONS)

            # ...................................................................................................Částice
            if chr(32) + workVar + chr(32) in OrientationModel.particle:
                self.add_member(MetadataEnum.PARTICLE)

            # ................................................................................................Citoslovce
            if chr(32) + workVar + chr(32) in OrientationModel.interjection:
                self.add_member(MetadataEnum.INTERJECTION)

            # ........................................................................................Příslovečné určeni
            # ..............................................................................................Společenství
            if workVar == "bez" or workVar == "s" or workVar == "spolu" or workVar == "a" or workVar == "i" or workVar == "ani" or workVar == "nebo" or workVar == "či" or workVar == "přímo" or workVar == "nadto" or workVar == "jednak":
                self.add_member(MetadataEnum.PARTNERSHIP)
            if workVar == "jak":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "jak" and workVar == "tak":
                self.add_member(MetadataEnum.PARTNERSHIP)
            if workVar == "hned":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "hned" and workVar == "hned":
                self.add_member(MetadataEnum.PARTNERSHIP)
            if workVar == "zčásti":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "zčásti" and workVar == "zčásti":
                self.add_member(MetadataEnum.PARTNERSHIP)
            if workVar == "dílem":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "dílem" and workVar == "dílem":
                self.add_member(MetadataEnum.PARTNERSHIP)

            # ........................................................................................Příčina a důsledek
            if workVar == "kvůli" or workVar == "protože" or workVar == "proč" or workVar == "neboť" or workVar == "vždyť" or workVar == "totiž" or workVar == "však" or workVar == "také" or "příčin" in workVar:
                self.add_member(MetadataEnum.CAUSE)
            if workVar == "proto" or workVar == "tudíž" or workVar == "tedy":
                self.add_member(MetadataEnum.CONSEQUENCE)
            if workVar == "a":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "a" and workVar == "proto":
                self.add_member(MetadataEnum.CONSEQUENCE)
            if workVar == "a":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "a" and workVar == "tak":
                self.add_member(MetadataEnum.CONSEQUENCE)
            if workVar == "a":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "a" and workVar == "tudíž":
                self.add_member(MetadataEnum.CONSEQUENCE)
            if workVar == "a":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "a" and workVar == "tedy":
                self.add_member(MetadataEnum.CONSEQUENCE)

            # ................................................................................................Vysvětlení
            if workVar == "totiž" or workVar == "vždyť":
                self.add_member(MetadataEnum.EXPLANATION)

            # .........................................................................................Odpor a výlučnost
            if workVar == "ale" or workVar == "avšak" or workVar == "však" or workVar == "leč" or workVar == "nýbrž" or workVar == "naopak" or workVar == "jenomže" or workVar == "jenže" or workVar == "sice-ale" or workVar == "jistě-ale":
                self.add_member(MetadataEnum.OPPOSITION)
            if workVar == "sice":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "sice" and workVar == "ale":
                self.add_member(MetadataEnum.OPPOSITION)
            if workVar == "jistě":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "jistě" and workVar == "ale":
                self.add_member(MetadataEnum.OPPOSITION)
            if workVar == "nebo" or workVar == "anebo" or workVar == "buď-nebo":
                self.add_member(MetadataEnum.EXCLUDE)
            if workVar == "buď":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "buď" and workVar == "nebo":
                self.add_member(MetadataEnum.EXCLUDE)

            # ......................................................................................Podmínka a přípustka
            if workVar == "navzdory" or workVar == "přestože" or workVar == "případě":
                self.add_member(MetadataEnum.ADMISSION)
            if workVar == "i":
                DetermineModel.phrase = workVar
            if DetermineModel.phrase == "i" and (
                    workVar == "když" or workVar == "přes"):
                self.add_member(MetadataEnum.ADMISSION)
            if workVar == "pokud" or workVar == "jestliže":
                self.add_member(MetadataEnum.CONDITION)

            # .............................................................................................Místo a původ
            if workVar == "z" or workVar == "od" or workVar == "odkud":
                self.add_member(MetadataEnum.ORIGIN)

            if workVar == "kde" or workVar == "kam" or workVar == "kudy":
                self.add_member(MetadataEnum.PLACE)

            # ....................................................................................................Způsob
            if workVar == "jako" or workVar == "jak" or workVar == "až" or workVar == "tak" or workVar == "jakým":
                if workVar == "jak":
                    DetermineModel.phrase = "jak"

                if workVar == "jakým":
                    DetermineModel.phrase = "jakým"

                self.add_member(MetadataEnum.WAY)

            if workVar[len(workVar) - 1:] == "e" or workVar[
                                                    len(
                                                        workVar) - 1:] == "ě":
                self.add_member(MetadataEnum.WAY)

            # .......................................................................................................Čas
            if (
                    workVar == "dlouho" or workVar == "často") and DetermineModel.phrase == "jak":
                self.add_member(MetadataEnum.TIME)

            if workVar == "kdy" or workVar == "odkdy" or workVar == "dokdy" or workVar == "kdy":
                self.add_member(MetadataEnum.TIME)
            # ...............................................................................................Kalkulativa
            if workVar == "kolik":
                if DetermineModel.preposition:
                    self.add_member(MetadataEnum.TIME)
                else:
                    self.add_member(MetadataEnum.NUMERAL)

            if workVar == "moc" and DetermineModel.phrase == "jak":
                self.add_member(MetadataEnum.NUMERAL)

            if chr(32) + workVar + chr(32) in OrientationModel.rate:
                if DetermineModel.preposition:
                    self.add_member(MetadataEnum.TIME)
                else:
                    self.add_member(MetadataEnum.NUMERAL)
            else:
                jednotky = ["mm", "cm", "dm", "m", "km", "ml", "l", "hl", "mg", "g", "kg"]
                kalkulativa = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]  # 10
                operator = ["+", "-", "*", "/"]  # 4
                for symb in kalkulativa:
                    if symb == workVar:
                        if DetermineModel.preposition:
                            self.add_member(MetadataEnum.TIME)
                        else:
                            self.add_member(MetadataEnum.NUMERAL)

                for symb in jednotky:
                    if symb == workVar:
                        self.add_member(MetadataEnum.NUMERAL)

                for symb in operator:
                    if symb == workVar:
                        self.add_member(MetadataEnum.NUMERAL)

            # ..................................................................................Předpony přídavných jmen
            predpony = ["prach", "rozto", "vele", "nej", "roz", "pra", "pře", "u"]

            for predpona in predpony:
                if predpona in workVar and workVar.index(predpona) == 0:
                    self.add_member(MetadataEnum.ADJECTIVE)

            # .............................................................................................Pádové otázky
            padoveOtazky = ["koho", "čeho", "komu", "čemu", "kom", "čem", "kým", "čím"]
            if workVar in padoveOtazky:
                self.add_member(MetadataEnum.SUBJECT)
            # ............................................................................................Prídavná jména
            for oneAdject in OrientationModel.nouns_adjective:
                if chr(32) + workVar + chr(32) in oneAdject:
                    self.add_member(MetadataEnum.ADJECTIVE)

            # ...................................................................................................Objekty
            for oneObject in OrientationModel.nouns_objects:
                if chr(32) + workVar + chr(32) in oneObject:
                    self.add_member(MetadataEnum.SUBJECT)
                    if DetermineModel.preposition:
                        self.add_member(MetadataEnum.PLACE)
                        nounValue = OrientationModel.nouns_orientation[OrientationModel.nouns_objects.index(oneObject)]
                        self.add_member(nounValue)
                        metadata = self.determine_metadata_by_name(nounValue)
                        if metadata:
                            self.add_member(metadata)

    # Určí čas slovesa a změní jeho osobu
    def verbProcessing(self, workVar):
        # TODO chybi predpony ??????????????????????????????????????????????????????????????????????????????????????????
        # Převod osob (1. -> 3.)  (2. -> 1.)
        if workVar == "jsem":
            workVar = "je"
            DetermineModel.time[0] = True
        if workVar == "jsme":
            # potreba overeni zda I_jakozto Steve neni jednou z I....V pak zustava!!!
            workVar = "jsou"
            DetermineModel.time[0] = True
        if workVar == "jsi":
            workVar = "jsem"
            DetermineModel.time[0] = True
        if workVar == "jste":
            workVar = "jsme"
            DetermineModel.time[0] = True

        # Minulý čas
        if "js" in workVar:
            if "jsi" in workVar:
                workVar = workVar[:workVar.index("js")]
                workVar = workVar + "jsem"
            else:
                workVar = workVar[:workVar.index("js")]
            DetermineModel.time[1] = True

        # Budoucí čas
        if ("po" in workVar and workVar.index("po") == 0) or (
                "pů" in workVar and workVar.index("pů") == 0):
            if "u" in workVar and workVar.index("u") == len(
                    workVar) - 1:
                workVar = workVar[:len(workVar) - 1]
                workVar = workVar + "e"
                DetermineModel.time[2] = True
            if "eme" in workVar and workVar.index("eme") == len(
                    workVar) - 3:
                workVar = workVar[:len(workVar) - 3]
                workVar = workVar + "ou"
                DetermineModel.time[2] = True
            if "eš" in workVar and workVar.index("eš") == len(
                    workVar) - 2:
                workVar = workVar[:len(workVar) - 2]
                workVar = workVar + "u"
                DetermineModel.time[2] = True
            if "ete" in workVar and workVar.index("ete") == len(
                    workVar) - 3:
                workVar = workVar[:len(workVar) - 3]
                workVar = workVar + "eme"
                DetermineModel.time[2] = True
        elif "bud" in workVar:
            workVar = workVar[:workVar.index(chr(32))]
            workVar = workVar[workVar.index(chr(32)):]
            if "budu" in workVar:
                workVar = "bude"
                DetermineModel.time[2] = True
            if "budeme" in workVar:
                # potreba overeni zda I_jakozto Steve neni jednou z I....V pak zustava!!!
                workVar = "bude"
                DetermineModel.time[2] = True
            if "budeš" in workVar:
                workVar = "budu"
                DetermineModel.time[2] = True
            if "budete" in workVar:
                workVar = "budeme"
                DetermineModel.time[2] = True

        # Převod osob ve slovese
        if "m" in workVar and workVar[len(workVar) - 1:] == "m":
            workVar = workVar[:len(workVar) - 1]
            DetermineModel.time[0] = True
        if "me" in workVar and workVar[
                               len(workVar) - 2:] == "me":
            workVar = workVar[:len(workVar) - 2]
            if workVar[len(workVar) - 1:] == "e":
                workVar = workVar[:len(workVar) - 1]
                workVar = workVar + "ou"
            elif workVar[len(workVar) - 1:] == "á":
                workVar = workVar[:len(workVar) - 1]
                workVar = workVar + "ají"
            DetermineModel.time[0] = True
        if "te" in workVar and workVar[
                               len(workVar) - 2:] == "te":
            workVar = workVar[:len(workVar) - 2]
            workVar = workVar + "me"
            DetermineModel.time[0] = True
        if "i" in workVar and workVar[len(workVar) - 1:] == "i":
            workVar = workVar[:len(workVar) - 1]
            workVar = workVar + "e"
            DetermineModel.time[0] = True
        if "u" in workVar and workVar[len(workVar) - 1:] == "u":
            workVar = workVar[:len(workVar) - 1]
            workVar = workVar + "e"
            DetermineModel.time[0] = True
        if "eš" in workVar and workVar[
                               len(workVar) - 2:] == "eš":
            workVar = workVar[:len(workVar) - 2]
            workVar = workVar + "u"
            DetermineModel.time[0] = True
        if "š" in workVar and workVar[len(workVar) - 1:] == "š":
            workVar = workVar[:len(workVar) - 1]
            if ("í" or "á") == workVar[len(workVar) - 1:]:
                workVar = workVar + "m"
            else:
                workVar = workVar + "ši"
            DetermineModel.time[0] = True
        return workVar
