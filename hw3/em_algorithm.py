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
    return c_w_d

startInitial = datetime.now()
# docList = document.getFilesName()
# wordList = dictionary.getDictionary()
topicNum = 5
P_d = np.random.dirichlet(np.ones(dNumber),size=1).tolist()[0]
P_w_T = np.random.dirichlet(np.ones(wNumber),size=  topicNum)

P_T_d = np.random.dirichlet(np.ones(dNumber),size= topicNum)
c_w_d = count_w_d( )
# print(type(c_w_d))
# print(type(P_w_T))
# print(type(P_T_d))

# print(len(P_w_T))
# print(len(P_T_d))

print("initial time: " ,  str(datetime.now()-startInitial).split(':', 3)[2], "(sec)")

# -------------------- EM algorithm -----------------------------
def e_step_wT(k, i):
    # return j  P_T_d[][]s
    log_X = list(np.asarray(P_T_d[k]) + P_w_T[k][i])
    molecular = np.logaddexp.reduce(log_X)
    deno = P_w_T[k][i] + P_T_d[k:]
    denominator = np.logaddexp.reduce(deno)
    return molecular - denominator

def e_step_Td(k, d):
    log_X = list(np.asarray(P_w_T[k]) + P_T_d[k][d])
    molecular = np.logaddexp.reduce(log_X)
    deno = P_w_T[k:] + P_T_d[k][d]
    denominator = np.logaddexp.reduce(deno)
    return molecular - denominator

def m_step():
    for k in range(topicNum):
        # T_d_List[i*k] = e_step(k)
        denominator = 0
        for i in range(wNumber):
            log_X =  c_w_d[i:] + e_step_wT(k, i)
            denominator += np.logaddexp.reduce(log_X)

        for i in range(wNumber):
            log_X =  c_w_d[i:] + e_step_wT(k, i)
            molecular = np.logaddexp.reduce(log_X)
            P_w_T[k][i] = molecular - denominator


        for d in range(dNumber):
            # for i in range(wNumber):
            log_X =  c_w_d[:d] + e_step_Td(k, d)
            molecular = np.logaddexp.reduce(log_X)
            T_d_denominator = np.logaddexp.reduce(c_w_d[:d])
            P_T_d[k][d] = molecular - T_d_denominator

def compute_log_likelihood():
    log_likelihood = 0

    for i in range(wNumber):
        for j in range(len(dict_DocCountWord[i])):
            d = dict_DocCountWord[i][j][0]
            nowDoc = dict_DocCountWord[i][j]

            sum_w_t_d = 0
            for kk in range(topicNum):
                if kk % 2 == 0:
                    logBigEle =  P_w_T[i][kk] + P_T_d[kk][d]
                    logSmallEle =  P_w_T[i][kk+1] +  P_T_d[kk+1][d]
                    temp = 0
                    if logBigEle < logSmallEle:
                        temp = logBigEle
                        logBigEle = logSmallEle
                        logSmallEle = temp
                    P_w_T_i_kk = logBigEle + math.log(1 + math.exp(logSmallEle - logBigEle))
                    sum_w_t_d += P_w_T_i_kk

            log_likelihood += int(nowDoc[1]) * ( math.log(P_d[nowDoc[0]]) + sum_w_t_d )
    return log_likelihood

def train():
    fname = "../log_likelihood_" + str(datetime.now().strftime('%Y-%m-%d')) + ".log"
    f = open(fname, 'w')

    for i in range(10):
        startOneTrain = datetime.now()
        # if i == 0:
        #     e_step0()
        # else:
        #     e_step()
        m_step()
        log_likelihood = compute_log_likelihood()

        nowTime = datetime.now()
        f.write('{:<4d} {:20s}   log_likelihood = {:9f}\n'.format(i, nowTime.strftime('%Y-%m-%d %H:%M:%S'), log_likelihood))
        print('{:<4d} excuteTime: {:9s}(sec) , log_likelihood = {:9f}'.format(i, str(nowTime - startOneTrain).split(':', 3)[2],  log_likelihood))
    f.close()

def write_P_T_d():
    fname = "../P_w_K.txt"
    f = open(fname, 'w')
    for p_w_T in P_w_T:
        strWrite = ""
        for value in p_w_T:
            strWrite += str(value) + " "
        f.write(strWrite + "\n")
    f.close()

print("\n -------------------- train start -------------------- \n")
startTrain = datetime.now()
train()
print("\n -------------------- train finished -------------------- \n")
print("train excution time is ", str(datetime.now()-startTrain).split('.', 3)[0])

# write_P_T_d()
