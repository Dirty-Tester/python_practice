#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

import store_data as st


class Test_store_data(object):
    def test_ファイルパスを渡してdataframeを開くこと(self):
        assert type(st.open_dat_file("data/actual_data.dat")) == pd.core.frame.DataFrame

    def test_ファイルパスを渡すとwalkすること(self):
        assert st.get_filepath("data") == ('data',[], ['control_data.dat', 'invalid_data.dat', 'actual_data.dat', 'LAG_C.dat'])
    
    def test_walkしたファイルの中のdatファイルを探す(self):
        assert st.explore_datfile("data") == ['control_data.dat', 'invalid_data.dat', 'actual_data.dat', 'LAG_C.dat']
        