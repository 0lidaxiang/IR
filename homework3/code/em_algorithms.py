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
def e_step0():
    for k in range(topicNum):
        for d in range(dNumber):
            now_doc_WordIndex = noCount_w_d[d]
            d_noCount_w_dNum = len(now_doc_WordIndex)
            for ni in range(d_noCount_w_dNum):
                i = int(now_doc_WordIndex[ni][1])
                sum_w_t_d = 0
                logY = 0
                logX = 0
                for kk in range(topicNum):
                    if kk % 2 == 0:
                        logBigEle =  math.log(P_w_T[i][kk]) +  math.log(P_T_d[kk][d])
                        logSmallEle =  math.log(P_w_T[i][kk+1]) +  math.log(P_T_d[kk+1][d])
                        # bigEle = P_w_T[i][kk] * P_T_d[kk][d]
                        # smallEle = P_w_T[i][kk+1] * P_T_d[kk+1][d]
                        temp = 0
                        if logBigEle < logSmallEle:
                            temp = logBigEle
                            logBigEle = logSmallEle
                            logSmallEle = temp
                        # logBigEle = math.log(bigEle)
                        # logSmallEle = math.log(smallEle)
                        # P_w_T_i_kk = logBigEle + math.log(1 + math.exp(logSmallEle - logBigEle))
                        P_w_T_i_kk = logBigEle + math.log(1 + math.exp(logSmallEle - logBigEle))
                        sum_w_t_d += P_w_T_i_kk

                P_w_T_i_k = math.log(P_w_T[i][k])
                P_T_d_k_d = math.log(P_T_d[k][d])
                index = index = d * (k+1)

                P_T_wd[index][i] = (P_w_T_i_k + P_T_d_k_d) - sum_w_t_d
def m_step0():
    for k in range(topicNum):
        # w_T_denominator
        w_T_denominator = 0
        for i in range(wNumber):
            for j in range(len(dict_DocCountWord[i])):
                para1 =  math.log(int(dict_DocCountWord[i][j][1]))
                d =  dict_DocCountWord[i][j][0]
                index = d * (k+1)
                para2 = P_T_wd[index][i]
                w_T_denominator += para1 + para2

        # compute P_w_T , all words
        for i in range(wNumber):
            molecular = 0
            # all documents
            for j in range(len(dict_DocCountWord[i])):
                if j % 2 == 0:
                    d = dict_DocCountWord[i][j][0]
                    index = d * (k+1)
                    logBigEle =  math.log(int(dict_DocCountWord[i][j][1]))
                    logSmallEle =  P_T_wd[index][i]

                    temp = 0
                    if logBigEle < logSmallEle:
                        temp = logBigEle
                        logBigEle = logSmallEle
                        logSmallEle = temp
                    # molecular
                    molecular += logBigEle + math.log(1 + math.exp(logSmallEle - logBigEle))

            P_w_T[i][k] = molecular - w_T_denominator

        # compute P_T_d ,  all documents
        for d in range(dNumber):
            molecular = 0
            denominator = 0
            now_doc_WordIndex = noCount_w_d[d]
            wIndex_in_now_doc_WordIndex = -1

            #  all words in a document
            for dd in range(len(now_doc_WordIndex)):
                _i = int(now_doc_WordIndex[dd][1])
                index = d * (k+1)
                mole_para1 =  int(count_w_d[ d ][dd][1])
                # mole_para1 = math.log( int(count_w_d[ d ][dd][1]) )
                mole_para2 = P_T_wd[index][_i]

                molecular += math.log(mole_para1) + mole_para2
                denominator += mole_para1

            # if denominator <= 0:
                # denominator = 1e-6
            # print(molecular , math.log(denominator))
            P_T_d[k][d] = molecular / math.log(denominator)

def e_step():
    for k in range(topicNum):
        for d in range(dNumber):
            now_doc_WordIndex = noCount_w_d[d]
            d_noCount_w_dNum = len(now_doc_WordIndex)
            for ni in range(d_noCount_w_dNum):
                i = int(now_doc_WordIndex[ni][1])
                sum_w_t_d = 0
                for kk in range(topicNum):
                    sum_w_t_d +=  P_w_T[i][kk] + P_T_d[kk][d]
                # if sum_w_t_d <= 0:
                #     sum_w_t_d = 1e-6

                P_w_T_i_k = P_w_T[i][k]
                P_T_d_k_d =  P_T_d[k][d]
                # P_w_T_i_k = math.log(P_w_T[i][k])
                # P_T_d_k_d = math.log(P_T_d[k][d])
                index = index = d * (k+1)
                P_T_wd[index][i] = (P_w_T_i_k + P_T_d_k_d) / sum_w_t_d
def m_step():
    for k in range(topicNum):
        # denominator
        w_T_denominator = 0
        for i in range(wNumber):
            for j in range(len(dict_DocCountWord[i])):
                para1 =  math.log(int(dict_DocCountWord[i][j][1]))
                d =  dict_DocCountWord[i][j][0]
                index = d * (k+1)
                para2 = P_T_wd[index][i]
                w_T_denominator += para1 + para2
                # w_T_denominator += dict_DocCountWord[i][j][1]

        # compute P_w_T , all words
        for i in range(wNumber):
            molecular = 0
            # all documents
            for j in range(len(dict_DocCountWord[i])):
                d = dict_DocCountWord[i][j][0]

                index = d * (k+1)
                para1 =  math.log(int(dict_DocCountWord[i][j][1]))
                para2 = P_T_wd[index][i]
                # molecular
                molecular += para1 + para2

            # if w_T_denominator <= 0:
                # w_T_denominator = 1e-6
            P_w_T[i][k] = molecular / w_T_denominator

        # compute P_T_d ,  all documents
        for d in range(dNumber):
            molecular = 0
            denominator = 0
            now_doc_WordIndex = noCount_w_d[d]
            wIndex_in_now_doc_WordIndex = -1

            #  all words in a document
            for dd in range(len(now_doc_WordIndex)):
                _i = int(now_doc_WordIndex[dd][1])
                index = d * (k+1)
                mole_para1 = int(count_w_d[ d ][dd][1])
                mole_para2 = P_T_wd[index][_i]

                molecular += math.log(mole_para1) + mole_para2
                denominator += mole_para1

            # if denominator <= 0:
                # denominator = 1e-6
            P_T_d[k][d] = molecular / math.log(denominator)

log_likelihood = 0
def compute_log_likelihood():
    log_likelihood = 0

    for i in range(wNumber):
        for j in range(len(dict_DocCountWord[i])):
            P_wT_Td = 0
            nowDoc = dict_DocCountWord[i][j]
            for k in range(topicNum):
                P_wT_Td += math.exp(P_w_T[i][k]) * math.exp(P_T_d[k][ nowDoc[0]])
                # print(P_w_T[i][k] , P_T_d[k][ nowDoc[0]])
                # print(nowDoc, P_d[nowDoc[0]], P_wT_Td)
            # print(P_d[nowDoc[0]],P_wT_Td, "\n")
            log_likelihood += int(nowDoc[1]) * ((math.log(P_d[nowDoc[0]]) + math.log(P_wT_Td)) )
    return log_likelihood

def train():
    fname = "../log_likelihood_" + str(datetime.now().strftime('%Y-%m-%d')) + ".log"
    f = open(fname, 'w')

    for i in range(10):
        startOneTrain = datetime.now()
        e_step0()
        # m_step0()
        # if i == 0:
        #     e_step0()
        #     m_step0()
        # else:
        #     e_step()
        #     m_step()
        # log_likelihood = compute_log_likelihood()
        #
        nowTime = datetime.now()
        # f.write('{:<4d} {:20s}   log_likelihood = {:9f}\n'.format(i, nowTime.strftime('%Y-%m-%d %H:%M:%S'), log_likelihood))
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
