#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import product

def test_正の数同士の引き算ができること_1():
    input_control = 5
    input_result = 3
    expected = 2
    assert product.calculate_defference(input_control,input_result) == expected

"""
input-actualの
差
絶対値を返す
    difference = 0を期待する場合、0を返すこと
    difference = 1を期待する場合、1を返すこと
"""


if __name__ == "__main__":
    pass