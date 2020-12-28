#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
import pytest

import calculator

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