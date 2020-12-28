#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

import store_data as st


class Test_store_data(object):
    def test_ファイルパスを渡してdataframeを開くこと(self):
        assert type(st.open_dat_file("data/actual_data.dat")) == pd.core.frame.DataFrame

    def test_ファイルパスを渡してファイル形式ののファイルパスを返すこと(self):
        assert st.get_filepath("data") == ('data',[], ['control_data.dat', 'invalid_data.dat', 'actual_data.dat', 'LAG_C.dat'])