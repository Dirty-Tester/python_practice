#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

import store_data as st


class Test_store_data(object):
    def test_ファイルパスを渡してdataframeを開くこと(self):
        assert type(st.open_dat_file("data/actual_data.dat")) == pd.core.frame.DataFrame