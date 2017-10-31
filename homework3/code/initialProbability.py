#!/usr/bin/python3
# coding: utf-8

import numpy as np, numpy.random

# get the
Tnumber = 5
wNumber = 0?
dNumber = 2265

wT = np.random.dirichlet(np.ones(1000),size=1)
Td = np.random.dirichlet(np.ones(1000),size=1)

print(wT[0][0])
print(wT[0][1])
print(wT[0][2])
print(wT[0][3])
print("--------------")
print(type(wT[0]))
print("--------------")
print(len(wT[0]))
# for value in wT[0]:
#     sumT += value

# print(sumT)
print(sum(wT[0]))
