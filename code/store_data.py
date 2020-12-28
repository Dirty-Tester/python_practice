#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os

def open_dat_file(filepath):
    with open(filepath) as data:
      read_data = pd.read_table(data)
      return read_data

def get_filepath(path):
    for files in os.walk(path):
        return files

if __name__ == "__main__":
    get_filepath("code")
