#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd

def calculate_difference(num_control,num_actual):
  num_of_difference = abs(num_control-num_actual)
  return num_of_difference

def calculate_average():
  average_result=[]

  for col,val in df.iteritems():
    average_result.apennd(val.mean())

  return average_result 


