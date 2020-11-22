#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def calculate_defference(num_control,num_actual):
  num_of_difference = abs(num_control-num_actual)
  return num_of_difference


def lastline_contain_equal(input_data):
    last_line = input_data.iat[-1, 0]#0列目の最終行を取得
    if last_line == "===":
        return True
    else:
        return False

def delete_lastline(input_data):
    deleted_data = input_data[:-1]
    return deleted_data
 
if __name__ == "__main__":
  pass
  """
  データの確認用(やむおえず)
    with open("data/actual_data.dat") as data:
      read_data = pd.read_table(data)
      print(read_data)
  """