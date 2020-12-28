#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def lastline_contain_equal(input_data):
    last_line = input_data.iat[-1, 0]#0列目の最終行を取得
    if last_line == "===":
        return True
    else:
        return False

def delete_lastline(input_data):
    deleted_data = input_data[:-1]
    return deleted_data

def rename_columns(inputdata):
    return inputdata.rename(columns={"Unnamed: 0":"elapsed_time"})

def delete_arrows(inputdata):
    inputdata.elapsed_time = inputdata.elapsed_time.str.strip("-->")
    return inputdata

if __name__ == "__main__":
 # データの確認用(やむおえず)
    with open("data/actual_data.dat") as data:
      read_data = delete_lastline(pd.read_table(data))
      rd = read_data.rename(columns={"Unnamed: 0":"elapsed_time"})
      print(rd['elapsed_time'])
      print(rd.columns.values)
      print(rd.index.values)
      deleted_arrow = delete_arrows(rd)
      print(deleted_arrow)
      print(deleted_arrow.iat[1, 0])