#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

import pandas_converter

# テスト用データの準備
@pytest.fixture
def invalid_data():
    with open("data/invalid_data.dat") as data:
      read_data = pd.read_table(data)
      return read_data

@pytest.fixture
def control_data():
    with open("data/control_data.dat") as data:
      read_data = pd.read_table(data)
      return read_data

@pytest.fixture
def actual_data():
    with open("data/actual_data.dat") as data:
      read_data = pd.read_table(data)
      return read_data

class Test_テストで呼び出したデータがデータフレームで入っていること(object):
    def test_Actualがデータフレームかどうか確かめる(self,actual_data):
        assert type(actual_data) == pd.core.frame.DataFrame

    def test_Controlがデータフレームかどうか確かめる(self,control_data):
        assert type(control_data) == pd.core.frame.DataFrame

class Test_dataframeの処理(object):
    def test_Actualの場合は2行削除して一行目に特定の値(self,actual_data):
        del_actual_data = pandas_converter.manage_line(actual_data,"actual")
        assert del_actual_data.iat[0,0] == "0.01300000-->"
    
    def test_Controlの場合は2行削除(self,control_data):
        del_control_data = pandas_converter.manage_line(control_data,"control")
        assert len(control_data) - len(del_control_data) == 2

 ## 最終行処理
class Test_datの処理(object):
    def test_特定の文字列の場合_Trueを返す(self,actual_data):
        assert pandas_converter.lastline_contain_equal(actual_data) == True 
 
    def test_特定の文字列ではない場合_Falseを返す(self,invalid_data):
        assert pandas_converter.lastline_contain_equal(invalid_data) == False
 
    def test_最終行を削除する(self,actual_data):
        deleted_data = pandas_converter.delete_lastline(actual_data) # 削除したデータを入れる
        assert len(actual_data) - len(deleted_data) == 1 ### アクチュアルからデリートしたデータを引いて、一行消せてたら成功
    
    def test_列の処理(self,actual_data):
        last_line_deleted = pandas_converter.delete_lastline(actual_data)
        renamed = pandas_converter.rename_columns(last_line_deleted)
        assert renamed.columns[0] == 'elapsed_time'

    def test_矢印を削除(self,actual_data):
        l_l_d = pandas_converter.delete_lastline(actual_data)
        renamed = pandas_converter.rename_columns(l_l_d)
        deleted_arrow = pandas_converter.delete_arrows(renamed)
        assert deleted_arrow.iat[0,0] == "0.00310000"

"""

 control_dataとactual_resultのヘッダと最終行処理をする
 一行目と一列目はヘッダ
 
"""

if __name__ == "__main__":
    pass