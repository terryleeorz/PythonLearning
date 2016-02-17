#!/usr/bin/env python3
# -*- coding: utf-8 -*-


L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print('L[0:3] =', L[0:3])
print('L[:3] =', L[:3])
print('L[1:3] =', L[1:3])
print('L[-2:] =', L[-2:])

R = list(range(100))
print('R[:10] =', R[:10])
print('R[-10:] =', R[-10:])
print('R[10:20] =', R[10:20])
print('R[:10:2] =', R[:10:2])
print('R[::5] =', R[::5])

# use L[:] to clone a list
L2 = L
L3 = L[:]
print(L2 == L)
print(L3 == L)
print(L2 == L3)
L3[0] = 'Terry'
L2[1] = 'Lee'
print(L)
print(L2)
print(L3)

# slice a tuple
print((0, 1, 2, 3, 4, 5)[:3])

# slice a string
print('ABCDEFG'[::2])
