#!/usr/bin/env python3
# -*- coding: utf-8 -*-

r"""
练习
请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
ax2 + bx + c = 0
的两个解
"""

import math


def check_number(num):
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')


def quadratic(a, b, c):
    for param in [a, b, c]:
        check_number(param)

    if a == 0:
        raise ValueError('a can not be zero')
    else:
        delta = b * b - 4 * a * c
        if delta >= 0:
            return (-b + math.sqrt(delta)) / (2 * a), (-b - math.sqrt(delta)) / (2 * a)
        else:
            return


print(quadratic(2, 3, 1))
print(quadratic(1, 3, -4))
print(quadratic(5, 4, 1))
print(quadratic(0, 4, 1))
