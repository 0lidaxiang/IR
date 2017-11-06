#!/usr/bin/python3
# coding: utf-8

import numpy as np
import math
from datetime import datetime

import dictionary
import document
import wordDocsCount
import wordDocsNoCount

startInitial = datetime.now()

docList = document.getFilesName()
wordList = dictionary.getDictionary()
wNumber = len(wordList)
dNumber = len(docList) # 2265
topicNum = 6
P_d = np.random.dirichlet(np.ones(dNumber),size=1).tolist()[0]
P_w_T = np.random.dirichlet(np.ones(topicNum),size= wNumber)
P_T_d = np.random.dirichlet(np.ones(dNumber),size= topicNum)
P_T_wd = np.zeros(shape=(topicNum * dNumber,wNumber))
count_w_d = wordDocsCount.getWordDocCount()
noCount_w_d = wordDocsNoCount.getWordDocNoCount()
dict_DocCountWord = wordDocsCount.getDict_DocCountWord()

print("initial time: " ,  str(datetime.now()-startInitial).split(':', 3)[2], "(sec)")

# -------------------- EM algorithm -----------------------------
def logAdd(xList):
    lenXList = len(xList)
    if lenXList > 1:
        bigEleIndex = xList.index(max(xList))
        tempPara2 = 0
        for i in range(lenXList - 1):
            x = xList[i+1]
            y = xList[i]
            logSmallEle = math.log(xList[i+1])
            logBigEle = math.log(xList[i])
            if x < y:
                temp = y
                y = x
                x = temp
            diff = y - x # diff < 0
            if diff < -23:
                if x < -0.5E10:
                    tempPara2 = -1.0E10
                else:
                    tempPara2 = x
            else:
                tempPara2 += math.log(1 + math.exp(diff))
            # print(logSmallEle, logBigEle, math.exp( logSmallEle - logBigEle))

        # diff1 = 0
        # if bigEleIndex != (lenXList -1):
        #     diff1 = xList[bigEleIndex+1] - xList[bigEleIndex]
        # diff2 = xList[bigEleIndex] - xList[bigEleIndex-1]
        # para2 = tempPara2 -  math.log(1 + math.exp(diff1)) -  math.log(1 + math.exp(diff2))
        para2 = tempPara2
        para1 = xList[bigEleIndex]
        return para1 + para2
    else:
        return xList[0]

# import sys
# sys.setrecursionlimit(230000)

# def logAdd(xList, y, isFirst):
#     # print(len(xList), y)
#
#     if len(xList) > 1:
#         if isFirst:
#             del(xList[-1])
#         LZERO = -1.0E10
#         LSMALL = -0.5E10
#         minLogExp = -23
#         para2 = LZERO
#         x = xList[0]
#         if x < y:
#             temp = x
#             x = y
#             y = temp
#         diff = y - x
#         if(diff < minLogExp):
#             if x < LSMALL:
#                 para2 = LZERO
#             else:
#                 para2 = x
#         else:
#             z = math.exp(diff)
#             para2 = x + math.log(1.0+z)
#         newY = xList.pop()
#         return logAdd(xList, newY, False) + para2
#     else:
#         LZERO = -1.0E10
#         LSMALL = -0.5E10
#         minLogExp = -23
#         # minLogExp = -log(-LZERO)
#
#         x = xList[0]
#         if x < y:
#             temp = x
#             x = y
#             y = temp
#         diff = y - x
#         if(diff < minLogExp):
#             if x < LSMALL:
#                 return  LZERO
#             else:
#                 return x
#         else:
#             z = math.exp(diff)
#             return x + math.log(1.0+z)

# def logAdd(xList):
#     if len(xList) > 2:
#         logSmallEle = math.log(xList[-1])
#         del(xList[-1])
#         logBigEle = logAdd(xList)
#         return logBigEle + math.log(1 + math.exp(logSmallEle - logBigEle))
#     else:
#         Px = xList[0]
#         y = xList[1]
#         temp = 0
#         if Px < y:
#             temp = Px
#             Px = y
#             y = temp
#         logBigEle = math.log(Px)
#         logSmallEle = math.log(y)
#         return logBigEle + math.log(1 + math.exp(logSmallEle - logBigEle))

def e_step0():
    for k in range(topicNum):
        for d in range(dNumber):
            now_doc_WordIndex = noCount_w_d[d]
            d_noCount_w_dNum = len(now_doc_WordIndex)
            for ni in range(d_noCount_w_dNum):
                i = int(now_doc_WordIndex[ni][1])
                logBigEleList = []
                for kk in range(topicNum):
                    logBigEleList.append( P_w_T[i][kk] * P_T_d[kk][d] )
                tempY = logBigEleList[-1]
                # del(logBigEleList[-1])
                sum_w_t_d = logAdd(logBigEleList)

                P_w_T_i_k = math.log(P_w_T[i][k])
                P_T_d_k_d = math.log(P_T_d[k][d])
                index = d * (k+1)

                P_T_wd[index][i] = (P_w_T_i_k + P_T_d_k_d) - sum_w_t_d

def e_step():
    for k in range(topicNum):
        for d in range(dNumber):
            now_doc_WordIndex = noCount_w_d[d]
            d_noCount_w_dNum = len(now_doc_WordIndex)
            for ni in range(d_noCount_w_dNum):
                i = int(now_doc_WordIndex[ni][1])
                logBigEleList = []
                for kk in range(topicNum):
                    para1 = -1.0E10
                    if math.exp(P_w_T[i][kk]) <= 0:
                        para1 = 0.5E10
                    else:
                        para1 = math.exp(P_w_T[i][kk])

                    if para1 * math.exp( P_T_d[kk][d]) <= 0:
                        print(para1 ,  math.exp( P_T_d[kk][d]))
                    logBigEleList.append(para1 * math.exp( P_T_d[kk][d]))
                tempY = logBigEleList[-1]
                # del(logBigEleList[-1])
                sum_w_t_d = logAdd(logBigEleList)

                P_w_T_i_k = P_w_T[i][k]
                P_T_d_k_d = P_T_d[k][d]
                index = index = d * (k+1)

                P_T_wd[index][i] = (P_w_T_i_k + P_T_d_k_d) - sum_w_t_d

def m_step():

    for k in range(topicNum):
        # w_T_denominator
        w_T_deno_logBigEleList = []
        for i in range(wNumber):
            for j in range(len(dict_DocCountWord[i])):
                para1 = -1.0E10
                if math.exp(int(dict_DocCountWord[i][j][1])) <= 0:
                    para1 = 0.5E10
                else:
                    para1 = math.exp(int(dict_DocCountWord[i][j][1]))

                if para1 * int(dict_DocCountWord[i][j][1])  <= 0:
                    print(para1 ,  math.exp( P_T_d[kk][d]))

                # para1 = int(dict_DocCountWord[i][j][1])
                d =  dict_DocCountWord[i][j][0]
                index = d * (k+1)
                para2 = P_T_wd[index][i]
                w_T_deno_logBigEleList.append(para1 * math.exp(para2))
        # tempY = w_T_deno_logBigEleList[-1]
        # del(w_T_deno_logBigEleList[-1])
        w_T_denominator = logAdd(w_T_deno_logBigEleList)

        # compute P_w_T , all words
        for i in range(wNumber):
            molecular = 0
            # all documents
            logBigEleList = []
            for j in range(len(dict_DocCountWord[i])):
                d =  dict_DocCountWord[i][j][0]
                index = d * (k+1)
                logBigEleList.append(int(dict_DocCountWord[i][j][1]) * math.exp( P_T_wd[index][i]))
            # tempY = logBigEleList[-1]
            # del(logBigEleList[-1])
            # print(k, i)
            molecular = logAdd(logBigEleList)

            P_w_T[i][k] = molecular - w_T_denominator
            if P_w_T[i][k] == 0:
                print(i, k , molecular , w_T_denominator)

        # compute P_T_d
        # all documents
        for d in range(dNumber):
            T_d_molecular = 0
            now_doc_WordIndex = noCount_w_d[d]
            now_doc_WordCount = count_w_d[d]
            #  all words in this document
            T_d_logBigEleList = []
            for dd in range(len(now_doc_WordIndex)):
                temp_count_w_d = int(now_doc_WordCount[dd][1])

                i = int(now_doc_WordIndex[dd][1])
                index = d * (k+1)
                temp_P_T_w_d = math.exp(P_T_wd[index][i])
                T_d_logBigEleList.append(temp_count_w_d * temp_P_T_w_d)
            # tempY = T_d_logBigEleList[-1]
            # del(T_d_logBigEleList[-1])
            T_d_molecular = logAdd(T_d_logBigEleList)

            # T_d_denominator
            T_d_denominator = 0
            for dd in range(len(now_doc_WordCount)):
                T_d_denominator += int(now_doc_WordCount[dd][1])

            P_T_d[k][d] = T_d_molecular - math.log(T_d_denominator)

log_likelihood = 0

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
        if i == 0:
            e_step0()
        else:
            e_step()
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

write_P_T_d()

# get the result
# for value in dNumber:
#     pass
