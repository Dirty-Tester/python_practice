#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas_converter as pc
import store_data

import pandas as pd

def create_table():
  calculate_result = pd.dataframe(columns['a1','a2','a3'])
  return calculate_result


def calculate_difference(num_control,num_actual):
  num_of_difference = abs(num_control-num_actual)
  return num_of_difference

def calculate_average(df):

  df_average = df.mean(axis=0)

  return 

if __name__ == "__main__":
  files = store_data.open_dat_file("./data/actual_data.dat")
  target = pc.main_converter(files,"actual")
  print(calculate_average(target))
  