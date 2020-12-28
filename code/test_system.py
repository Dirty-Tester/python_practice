#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

import product

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


 ## 最終行処理
class Test_datの処理(object):
    def test_特定の文字列の場合_Trueを返す(self,actual_data):
        assert product.lastline_contain_equal(actual_data) == True 
 
    def test_特定の文字列ではない場合_Falseを返す(self,invalid_data):
        assert product.lastline_contain_equal(invalid_data) == False
 
    def test_最終行を削除する(self,actual_data):
        deleted_data = product.delete_lastline(actual_data) # 削除したデータを入れる
        assert len(actual_data) - len(deleted_data) == 1 ### アクチュアルからデリートしたデータを引いて、一行消せてたら成功
    
    def test_列の処理(self,actual_data):
        last_line_deleted = product.delete_lastline(actual_data)
        renamed = product.rename_columns(last_line_deleted)
        assert renamed.columns[0] == 'elapsed_time'

    def test_矢印を削除(self,actual_data):
        l_l_d = product.delete_lastline(actual_data)
        renamed = product.rename_columns(l_l_d)
        deleted_arrow = product.delete_arrows(renamed)
        assert deleted_arrow.iat[0,0] == "0.00310000"

"""

 control_dataとactual_resultのヘッダと最終行処理をする
 一行目と一列目はヘッダ
 
"""

if __name__ == "__main__":
    pass