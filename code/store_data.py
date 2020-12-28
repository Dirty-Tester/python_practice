#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import os

def open_dat_file(filepath):
    with open(filepath) as data:
      read_data = pd.read_table(data)
      return read_data

def get_filepath(fpath):
    file_list = []
    for curDir, _dirs, files in os.walk(fpath):
        for f in files:
            if f.endswith(".dat"):
                cpath = os.path.join(curDir,f)
                file_list.append(cpath)
            
    return file_list

if __name__ == "__main__":
    print(get_filepath("code"))

