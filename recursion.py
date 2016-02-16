#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


def tail_fact(n):
    return fact_iter(n, 1)


def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)


# the solution of tower of hanoi
def move(origin, destination):
    print(origin, "-->", destination)


def hanoi(number, origin, assist, destination):
    if number == 1:
        move(origin, destination)
    else:
        hanoi(number - 1, origin, destination, assist)
        move(origin, destination)
        hanoi(number - 1, assist, origin, destination)


n = int(input('请输入汉诺塔的层数：'))
hanoi(n, 'A', 'B', 'C')
