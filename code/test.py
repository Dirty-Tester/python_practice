#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import product


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
 
def test_特定の文字列の場合_Trueを返す():
    assert product.lastline_is_equal("===") == True 
 
def test_特定の文字列以外の場合_Falseを返す():
    assert product.lastline_is_equal("") == False
 
 
"""
 一列目の最終行の内容を返す
 
 文字列(===)を示していたら←〇
 
 捨てる←"==="を抜いたデータ返す
 
 文字列(===)がなかったら←〇
 "Log file error"を返す
 
 
 dataframeを入れる前に
 control_dataとactual_resultのヘッダと最終行処理をする
 一行目と一列目はヘッダ
 
"""

if __name__ == "__main__":
    pass