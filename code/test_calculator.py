#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

import calculator

# テストデータの準備
@pytest.fixture
def test_data():
    with open('data/calculate_data.dat') as data:
      read_data = pd.read_table(data)
      return (read_data)

class Test_テストで呼び出したデータがデータフレームで入っていること(object):
    def test_dataがデータフレームかどうか確かめる(self,test_data):
        assert type(test_data) == pd.core.frame.DataFrame

# 計算する系
## actualの1,2行目にデータがあったら起こる機能
    ## input = control_dataで処理対象となった値
    ## actual = actual_resultの同列の2子下の値


## 期待値と結果の差を計算する。
class Test_期待値と結果の差を計算する(object):
    def test_正の数同士の差が計算できること_1(self):
        assert calculator.calculate_difference(5,3) == 2

    def test_正の数同士の差が計算できること_2(self):
        assert calculator.calculate_difference(5,5) == 0

    def test_正の数同士の差の結果がマイナスだったとき差が計算できること(self):
        assert calculator.calculate_difference(5,7) == 2

    def test_負の数と正の数の結果がマイナスだったとき差が計算できること(self):
        assert calculator.calculate_difference(-5,7) == 12

# 他のモジュールとの兼ね合いがあるから一旦後回し(テストデータを入れたら一応できるかも)
    ## calculate_resultとactual_resultの行数が同じであること
    ## 計算結果をpandasのdataframeに格納する
        ## dataframeになしかしらデータが入っていること
        ## dataframeのデータとcalculate_resultのデータが同じであること


#　最終計算
## calculate_resultの列ごとの平均値を算出し、列ごとの変数に代入する-①
    ## 平均値が出せる

class test_平均値の計算(object):
    def test_格納されたdataframeに平均値行が追加されている(self,test_data):
        # 下は変えてないけど、データに'average'という行があったら、1を返すようにする
        # assert calculator.calculate_average(test_data) == [64.3,65.44,48.74]

    # def test_追加されている平均値行に値が入っている(self,test_data):
        # assert calculator.calculate_average(test_data)で、追加された平均値行のデータがNULLがないことを確認したい

    # def test_追加されている平均値行に格納されている値が正しい(self,test_data):
        # assert calculator.calculate_average(test_data)の平均値行のデータがあっていることの確認


        ## <column>_average3つできるはず

## control_dataの処理対象となった列の最大値を取得し、変数に代入する-②
    ## 列の最大値を取得できること
        ## 格納されているデータの最大値を取得できること
        ## 格納されている配列(変数ごと)に最大値を取得できること
        ## dataframeの型でやるやつはそのあとでやる
    ## 0の場合、0の除算となる

## ①/②*100を算出し、変数に代入する-③誤差率
    ## ①/②*100の計算が出来ること
    ## 変数に代入できること

## ①と②と③をテキストファイルに出力する
    ## column_average,1,2,3
    ## max_data,1,2,3,
    ## error_rate,③
    ## not_caliculated_column=XXX

## 処理しやすい形で出す