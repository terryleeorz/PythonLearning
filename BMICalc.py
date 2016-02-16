#!/usr/bin/env python3
# -*- coding: utf-8 -*-

height = input('Please input your Height(mm):')
weight = input('Please input your Weight(kg):')
height = int(height) / 100
weight = int(weight)
BMI = weight / (height * height)

result = ''
if BMI < 18.5:
    result = '过轻'
elif BMI < 25:
    result = '正常'
elif BMI < 28:
    result = '过重'
elif BMI < 32:
    result = '肥胖'
else:
    result = '严重肥胖'

print(result)
