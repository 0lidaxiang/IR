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
topicNum = 5
P_d = np.random.dirichlet(np.ones(dNumber),size=1).tolist()[0]
# P_w_T = np.random.dirichlet(np.ones(topicNum),size= wNumber)
P_w_T = get_P_w_T()
P_T_d = np.random.dirichlet(np.ones(dNumber),size= topicNum)
P_T_wd = np.zeros(shape=(topicNum * dNumber,wNumber))
count_w_d = wordDocsCount.getWordDocCount()
noCount_w_d = wordDocsNoCount.getWordDocNoCount()
dict_DocCountWord = wordDocsCount.getDict_DocCountWord()

# get the P_w_T
def get_P_w_T():
    fname = '../P_w_K.txt'
    # fname = '../initial18000Result/P_w_T_' + str(datetime.now().strftime('%Y-%m-%d')) + '.txt'
    res = []
    with open(fname) as f:
        lines = f.read().splitlines()
    for line in lines:
        lineList = line.split(" ")
        res.append(lineList)
    return res

# -------------------- EM algorithm -----------------------------
def e_step():
    for k in range(topicNum):
        for d in range(dNumber):
            now_doc_WordIndex = noCount_w_d[d]
            d_noCount_w_dNum = len(now_doc_WordIndex)
            for ni in range(d_noCount_w_dNum):
                i = int(now_doc_WordIndex[ni][1])
                sum_w_t_d = 0
                for kk in range(topicNum):
                    sum_w_t_d +=  P_w_T[i][kk] * P_T_d[kk][d]
                if sum_w_t_d <= 0:
                    sum_w_t_d = 1e-6

                P_w_T_i_k = P_w_T[i][k]
                P_T_d_k_d =  P_T_d[k][d]
                index = index = d * (k+1)
                P_T_wd[index][i] = (P_w_T_i_k * P_T_d_k_d) / sum_w_t_d
def m_step():
    for k in range(topicNum):
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

                molecular += mole_para1 * mole_para2
                denominator += mole_para1

            if denominator <= 0:
                denominator = 1e-6
            P_T_d[k][d] = molecular / denominator

log_likelihood = 0
def compute_log_likelihood():
    log_likelihood = 0

    for i in range(wNumber):
        for j in range(len(dict_DocCountWord[i])):
            P_wT_Td = 0
            for k in range(topicNum):
                P_wT_Td += P_w_T[i][k] * P_T_d[k][dict_DocCountWord[i][j][0]]
            log_likelihood += int(dict_DocCountWord[i][j][1]) * math.log10(P_d[j] * P_wT_Td)
    return log_likelihood

def train():
    fname = "../log_likelihood_" + str(datetime.now().strftime('%Y-%m-%d')) + ".log"
    f = open(fname, 'w')
    for i in range(10):
        startOneTrain = datetime.now()

        e_step()
        m_step()
        log_likelihood = compute_log_likelihood()

        nowTime = datetime.now()
        f.write('{:<4d} {:20s}   log_likelihood = {:9f}\n'.format(i, nowTime.strftime('%Y-%m-%d %H:%M:%S'), log_likelihood))
        print('{:<4d} excuteTime: {:9s}(sec) , log_likelihood = {:9f}'.format(i, str(nowTime - startOneTrain).split(':', 3)[2],  log_likelihood))
    f.close()

def write_P_T_d():
    fname = "../2265P_T_d.txt"
    f = open(fname, 'w')
    for p_w_T in P_w_T:
        strWrite = ""
        for value in p_w_T:
            strWrite += str(value) + " "
        f.write(strWrite + "\n")
    f.close()

get_P_w_T()
print("\n -------------------- train start -------------------- \n")
startTrain = datetime.now()
train()
print("\n -------------------- train finished -------------------- \n")
print("train excution time is ", str(datetime.now()-startTrain).split('.', 3)[0])

write_P_T_d()
