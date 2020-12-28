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
    with open("data/actual_data.dat") as a_data:
      read_a_data = delete_lastline(pd.read_table(a_data))
      rd = read_a_data.rename(columns={"Unnamed: 0":"elapsed_time"})
      deleted_arrow = delete_arrows(rd)

      for column_name, item in deleted_arrow.iteritems():
            if column_name == 'elapsed_time':
                  continue
            else:
              print(column_name)
              deleted_arrow_zero = deleted_arrow[~(deleted_arrow[(column_name)] == 0)]
              if (deleted_arrow_zero[(column_name)].sum()) == 0:
                    deleted_arrow = deleted_arrow.drop(columns = column_name)
              else:
                  continue

processiong_act_data = deleted_arrow

print(processiong_act_data)