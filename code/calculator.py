#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def calculate_difference(num_control,num_actual):
  num_of_difference = abs(num_control-num_actual)
  return num_of_difference

def calculate_average(test_data):
    result_average = sum(test_data) / len(test_data)
    return result_average

