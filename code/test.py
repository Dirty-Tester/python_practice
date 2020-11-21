#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

import product

def test_正の数同士の引き算ができること_1():
    assert product.calculate_defference(5,3) == 2

def test_正の数同士の引き算ができること_2():
    assert product.calculate_defference(5,5) == 0


"""
input-actualの
差
絶対値を返す
    difference = 0を期待する場合、0を返すこと
    difference = 1を期待する場合、1を返すこと
"""


if __name__ == "__main__":
    pass