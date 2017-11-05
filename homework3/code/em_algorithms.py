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
topicNum = 10
P_d = np.random.dirichlet(np.ones(dNumber),size=1).tolist()[0]
P_w_T = np.random.dirichlet(np.ones(topicNum),size= wNumber)
P_T_d = np.random.dirichlet(np.ones(dNumber),size= topicNum)
P_T_wd = np.zeros(shape=(topicNum * dNumber,wNumber))
count_w_d = wordDocsCount.getWordDocCount()
noCount_w_d = wordDocsNoCount.getWordDocNoCount()
dict_DocCountWord = wordDocsCount.getDict_DocCountWord()

print("initial time: " ,  str(datetime.now()-startInitial).split(':', 3)[2], "(sec)")

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
        # denominator
        w_T_denominator = 0
        for i in range(wNumber):
            for j in range(len(dict_DocCountWord[i])):
                w_T_denominator += dict_DocCountWord[i][j][1]

        # compute P_w_T , all words
        for i in range(wNumber):
            molecular = 0
            # all documents
            for j in range(len(dict_DocCountWord[i])):
                d = dict_DocCountWord[i][j][0]

                index = d * (k+1)
                para1 = int(dict_DocCountWord[i][j][1])
                para2 = P_T_wd[index][i]
                # molecular
                molecular += para1 * para2

            if w_T_denominator <= 0:
                w_T_denominator = 1e-6
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
    for i in range(1, 50):
        startOneTrain = datetime.now()

        e_step()
        m_step()
        log_likelihood = compute_log_likelihood()

        nowTime = datetime.now()
        f.write('{:<4d} {:20s}   log_likelihood = {:9f}\n'.format(i, nowTime.strftime('%Y-%m-%d %H:%M:%S'), log_likelihood))
        print('{:<4d} excuteTime: {:9s}(sec) , log_likelihood = {:9f}'.format(i, str(nowTime - startOneTrain).split(':', 3)[2],  log_likelihood))
    f.close()


print("\n -------------------- train start -------------------- \n")
startTrain = datetime.now()
train()
print("\n -------------------- train finished -------------------- \n")
print("train excution time is ", str(datetime.now()-startTrain).split('.', 3)[0])
