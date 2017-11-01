#!/usr/bin/python3
# coding: utf-8

# import initialProbability
import numpy as np, numpy.random
import math
import datetime

import dictionary
import document
import wordDocsCount

Tnumber = 5
docList = document.getFilesName()
wordList = dictionary.getDictionary()

# wordDocCount = getWordDocCount

wNumber = len(wordList)
dNumber = len(docList) # 2265
topicNum=5

P_d = np.random.dirichlet(np.ones(dNumber),size=1).tolist()[0]
P_w_T = []
P_T_d = []
P_T_wd = []
count_w_d = wordDocsCount.getWordDocCount()
max_likehood = 0

def initialProbability():
    index = 0
    for value in wordList:
        wT = np.random.dirichlet(np.ones(topicNum),size=1)
        P_w_T.append(wT.tolist()[0])
        index += 1

    index = 0
    for value in docList:
        Td = np.random.dirichlet(np.ones(topicNum),size=1)
        P_T_d.append(Td.tolist()[0])
        index += 1

    for k in range(0, topicNum):
        temp_P_T_d = []
        for j in range(0, dNumber):
            temp_P_T_d.append(np.random.dirichlet(np.ones(wNumber),size=1).tolist()[0])
        P_T_wd.append(temp_P_T_d)

initialProbability()
print(P_w_T[0][0])
# print(type(P_w_T[0][0]))
print(type(P_w_T[0]))
print(len(P_w_T[0]))
print(len(P_w_T))

print("--------------")
print(type(P_T_d[0][0]))
print(P_T_d[0][0] * P_w_T[0][0])
print("--------------")
# print(type(P_w_T[0][0]))
print(type(P_T_wd[0]))
print(type(P_T_wd[0][0]))
print(type(P_T_wd[0][0][0]))
print(len(P_T_wd[0][0]))
print(len(P_T_wd[0]))
print(len(P_T_wd))

# print(int(sum(P_w_T)))
# print(int(sum(P_w_T[0])))
# print(int(sum(P_T_d[0])))

# P_d = np.random.dirichlet(np.ones(dNumber),size=1)
# P_w_T = []
# P_T_d = []
#
# index = 0
# for value in wordList:
#     wT = np.random.dirichlet(np.ones(topicNum),size=1)
#     P_w_T.append(wT)
#     index += 1
#
# index = 0
# for value in docList:
#     Td = np.random.dirichlet(np.ones(topicNum),size=1)
#     P_T_d.append(Td)
#     index += 1
#
# print(P_w_T[0][0])
# print(P_T_d[0])
# print(P_w_T[0])
# print("--------------")
# print(int(sum(P_d[0])))
# print(len(P_d[0]))
#
# print(int(sum(P_w_T[0][0])))
# print(int(sum(P_T_d[0][0])))
