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

import os

from core_util.CoreModel import CoreModel
from framework.Framework import Framework
from process.Process import Process
import random
import time


class Cheat(CoreModel):

    def __init__(self):
        self.process = Process()
        self.framework = Framework()
        self.email = None

    def rand_delay_in_sec(self):
        time.sleep(random.uniform(1, 2))

    def begin_set_up(self):
        self.rand_delay_in_sec()
        self.framework.event_player.treatment_condition("C_bfa02fa0_796d_4e8b_87c6_e6dca49eb785", False,
                                                        None)  # klik na novou identitu
        self.rand_delay_in_sec()
        self.framework.event_player.treatment_watcher("W_ef9c0b0f_e453_4d39_90e6_c397719cd34a", False,
                                                      None)  # cekani na nacteni
        self.rand_delay_in_sec()
        self.framework.event_player.treatment_condition("C_4137dc7b_dec7_4cc8_8ddd_19cc2ac3c0ff", False,
                                                        None)  # maximalizovat

    def go_to_page(self, url):
        self.framework.clipboard.set_clipboard(url)
        self.rand_delay_in_sec()
        self.framework.device_control.left_click_to_position(900, 55)  # klik do hypertextu
        self.framework.device_control.ctrl_v()
        self.rand_delay_in_sec()
        self.framework.device_control.press_and_release_key("return")

    def new_tab(self):
        self.framework.event_player.treatment_condition("C_f87bc027_2aba_4b86_a813_13b5415691c6", False,
                                                        None)  # klik na novou zalozku

    def new_mail(self):
        self.go_to_page("10minutemail.com")
        self.framework.event_player.treatment_watcher("W_984463b1_6697_4ba0_9168_d277e32438f4", False, None)
        self.framework.event_player.treatment_watcher("W_e09c08e1_f808_4163_a26e_de19133e363b", False, None)
        self.rand_delay_in_sec()
        self.framework.event_player.treatment_condition("C_f3474158_89dd_411e_848b_80873ebd5a83", False, None)
        self.rand_delay_in_sec()
        self.email = self.framework.clipboard.get_clipboard()

    def load_car(self):
        self.go_to_page("http://sprinte.rs/601bc17cd46b3/52")
        self.framework.event_player.treatment_watcher("W_3667cb04_e976_4313_97a7_e13d6c2f1978", False, None)

    def sign_up(self):
        self.load_car()
        self.rand_delay_in_sec()
        self.framework.device_control.random_click_into_area(1049, 465, 1176, 493)
        self.framework.event_player.treatment_watcher("W_014b9f5b_cfd5_439e_8dbf_548085f1f119", False, None)
        self.rand_delay_in_sec()
        self.framework.event_player.run_sequence_by_table_name("S_23b23464_0cd0_4fe3_890d_25b21f4a9b21", False, None)
        self.rand_delay_in_sec()
        self.framework.clipboard.set_clipboard(self.email)
        self.rand_delay_in_sec()
        self.framework.device_control.ctrl_v()
        self.framework.device_control.random_click_into_area(891, 626, 1013, 644)

    def wait_for_mail(self):
        self.framework.event_player.treatment_watcher("W_790e555a_c18b_4913_b8f6_5378cec7511b", False, None)
        self.rand_delay_in_sec()
        self.framework.event_player.run_sequence_by_table_name("S_5bb7e4b3_aafd_41b6_a2eb_71354d8974fa", False, None)
        self.rand_delay_in_sec()

    def finish(self):
        self.load_car()
        self.rand_delay_in_sec()
        self.framework.device_control.random_click_into_area(1055, 465, 1175, 492)
        self.framework.event_player.treatment_watcher("W_1c476b1b_141c_48cb_9c79_05618ce5aaa7", False, None)
        self.framework.device_control.random_click_into_area(1028, 464, 1053, 482)

    def run(self):
        print("OK, GO !")
        ind = 0
        self.framework.event_player.treatment_condition("C_362c92bf_e8ff_4fa8_9f21_9b0c1ed11589", False,
                                                        None)  # prepne na ENG klavesnici

        while True:
            self.framework.event_player.treatment_condition("C_203ff98c_8e56_41b8_b4eb_c075512f7141", False,
                                                            None)  # klik na TOR
            self.begin_set_up()
            self.new_mail()
            self.new_tab()
            self.sign_up()
            self.framework.event_player.treatment_condition("C_aa32b14d_a900_4ce9_917b_2f4ad60a1a20", False, None)
            self.wait_for_mail()
            self.finish()
            # playsound("notify.mp3")
            ind += 1
            print("ACT: ", ind)
            self.rand_delay_in_sec()
        os._exit(0)
