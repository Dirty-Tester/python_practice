#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

import product

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

class Test_テストで呼び出したデータがdetaframeで入っていること(object):
    def test_Actualがデータフレームかどうか確かめる(self,actual_data):
        assert type(actual_data) == pd.core.frame.DataFrame

    def test_Controlがデータフレームかどうか確かめる(self,control_data):
        assert type(control_data) == pd.core.frame.DataFrame


##　期待値と結果の差を計算する。
class Test_calculate_defference(object):

    def test_正の数同士の差が計算できること_1(self):
        assert product.calculate_defference(5,3) == 2

    def test_正の数同士の差が計算できること_2(self):
        assert product.calculate_defference(5,5) == 0

    def test_正の数同士の差の結果がマイナスだったとき差が計算できること(self):
        assert product.calculate_defference(5,7) == 2

    def test_負の数と正の数の結果がマイナスだったとき差が計算できること(self):
        assert product.calculate_defference(-5,7) == 12

 ## 最終行処理
class Test_lastline_contain_equal(object):
    def test_特定の文字列の場合_Trueを返す(self):
        assert product.lastline_contain_equal("===") == True 
 
    def test_特定の文字列ではない場合_Falseを返す(self):
        assert product.lastline_contain_equal(20202.34) == False
 

"""
 一列目の最終行の内容を返す
 
 捨てる←"==="を抜いたデータ返す
 
 dataframeを入れる前に
 control_dataとactual_resultのヘッダと最終行処理をする
 一行目と一列目はヘッダ
 
"""

if __name__ == "__main__":
    pass