#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

import store_data as st


class Test_store_data(object):
    def test_ファイルパスを渡してdataframeを開くこと(self):
        assert type(st.open_dat_file("data/actual_data.dat")) == pd.core.frame.DataFrame

    def test_ファイルパスを渡すとwalkすること(self):
        assert st.get_filepath("./") == ['./data/control_data.dat', './data/invalid_data.dat', './data/actual_data.dat', './data/calculate_data.dat', './data/LAG_C.dat', './data2/control_data.dat', './data2/invalid_data.dat', './data2/actual_data.dat', './data2/LAG_C.dat']
    