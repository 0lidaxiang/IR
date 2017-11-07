#!/usr/bin/python3
# coding: utf-8

import numpy as np
import math
from datetime import datetime
import collections

# import dictionary
# import document
# import wordDocsCount
# import wordDocsNoCount
wNumber = 51253
dNumber = 18461
def getTestFileContent(fname):
    with open(fname) as f:
        lines = f.read().splitlines()
    res = []
    for line in lines:
        res.append( list(map(int, line.split())))
    return res

def count_w_d( ):
    c_w_d = np.zeros(shape=(wNumber, dNumber))
    testFileContent = getTestFileContent("./source/Collection.txt")
    for d in range(dNumber):
        res = collections.Counter(testFileContent[d]).most_common()
        for value in res:
            i = value[0]
            c_w_d[i][d] = value[1]

startInitial = datetime.now()
# count_w_d()
# docList = document.getFilesName()
# wordList = dictionary.getDictionary()
topicNum = 5
P_d = np.random.dirichlet(np.ones(dNumber),size=1).tolist()[0]
P_w_T = np.random.dirichlet(np.ones(wNumber),size=  topicNum)

P_T_d = np.random.dirichlet(np.ones(dNumber),size= topicNum)
print(len(P_w_T))
print(len(P_T_d))
# count_w_d = wordDocsCount.getWordDocCount()
# noCount_w_d = wordDocsNoCount.getWordDocNoCount()
# dict_DocCountWord = wordDocsCount.getDict_DocCountWord()

print("initial time: " ,  str(datetime.now()-startInitial).split(':', 3)[2], "(sec)")

# -------------------- EM algorithm -----------------------------
def e_step_wT(k, i):
    # return j  P_T_d[][]s
    log_X =  P_w_T[k][i] + P_T_d[k]
    molecular = np.logaddexp.reduce(log_X)
    for kk in range(topicNum):
        deno += P_w_T[kk][i] + P_T_d[k]
    denominator = np.logaddexp.reduce(deno)
    return molecular - denominator

def e_step_Td(k, d):
    # return j  P_T_d[][]s
    log_X =  P_w_T[k][i] + P_T_d[k]
    molecular = np.logaddexp.reduce(log_X)
    for kk in range(topicNum):
        deno += P_w_T[kk][i] + P_T_d[k]
    denominator = np.logaddexp.reduce(deno)
    return molecular - denominator

def m_step(c_w_d_Arg, T_w_d_Arg):
    for k in range(topicNum):
        # T_d_List[i*k] = e_step(k)
        denominator = 0
        for i in range(wNumber):
            log_X =  c_w_d_Arg[i] + e_step_wT(k, i)
            denominator += np.logaddexp.reduce(log_X)

        for i in range(wNumber):
            log_X =  c_w_d_Arg[i] + e_step_wT(k, i)
            molecular = np.logaddexp.reduce(log_X)
            P_w_T[k][i] = molecular - denominator


        for d in range(dNumber):
            # for i in range(wNumber):
            log_X =  c_d_w[d] + e_step_Td(k, d)
            molecular = np.logaddexp.reduce(log_X)
            T_d_denominator = np.logaddexp.reduce(c_d_w[d])
            P_T_d[k][d] = molecular - T_d_denominator
