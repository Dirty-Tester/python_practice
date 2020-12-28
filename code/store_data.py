#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def open_dat_file(filepath):
    with open(filepath) as data:
      read_data = pd.read_table(data)
      return read_data