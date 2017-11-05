#!/usr/bin/python3
# coding: utf-8

# import initialProbability
import numpy as np, numpy.random
import math
from operator import mul
from datetime import datetime

import dictionary
import document
import wordDocsCount
import wordDocsNoCount

Tnumber = 5
docList = document.getFilesName()
wordList = dictionary.getDictionary()
wNumber = len(wordList)
dNumber = len(docList) # 2265
topicNum=5

P_d = np.random.dirichlet(np.ones(dNumber),size=1).tolist()[0]
print("\ninitialProbability start")
start = datetime.now()
# np.ones(wNumber) is rows , size=dNumber is cols
P_w_T = np.random.dirichlet(np.ones(topicNum),size= wNumber)
P_T_d = np.random.dirichlet(np.ones(dNumber),size= topicNum)
P_T_wd = numpy.zeros(shape=(topicNum * dNumber,wNumber))
# P_T_wd = np.random.dirichlet(np.ones(wNumber),size= topicNum * dNumber)
# print(len(P_T_wd))
# print(len(P_T_wd[0]))

count_w_d = wordDocsCount.getWordDocCount()
noCount_w_d = wordDocsNoCount.getWordDocNoCount()
# noCount_w_dNum = len(noCount_w_d)
dict_DocCountWord = wordDocsCount.getDict_DocCountWord()
onlyWordsByDoc = wordDocsNoCount.getOnlyWordDocNoCount()
print("initialProbability stop " , datetime.now()-start, "\n")
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
                    sum_w_t_d += math.log10( P_w_T[i][kk]) + math.log10(P_T_d[kk][d])
                if sum_w_t_d <= 0:
                    sum_w_t_d = 1e-6

                P_w_T_i_k = math.log10(P_w_T[i][k])
                P_T_d_k_d = math.log10( P_T_d[k][d])
                index = index = d * (k+1)
                P_T_wd[index][i] = (P_w_T_i_k * P_T_d_k_d) / sum_w_t_d
def m_step():
    for k in range(topicNum):
        # print (k , "m_step")

        w_T_denominator = 0
        for i in range(wNumber):
            for j in range(len(dict_DocCountWord[i])):
                w_T_denominator += dict_DocCountWord[i][j][1]

        # compute P_w_T , all words
        for i in range(wNumber):
            molecular = 0
            # denominator = 0

            # all documents
            for j in range(len(dict_DocCountWord[i])):
                d = dict_DocCountWord[i][j][0]
                # wIndex_in_now_doc_WordIndex = -1
                # temp_wIndex = 0
                # for value in now_doc_WordIndex:
                    # if int(value[1]) == i:
                    #     wIndex_in_now_doc_WordIndex = temp_wIndex
                    #     break
                    # temp_wIndex += 1
                # words = onlyWordsByDoc[d]
                # word = wordList[i]
                # if word in words:
                # now_doc_WordIndex = noCount_w_d[d]
                # wIndex_in_now_doc_WordIndex = i
                # print(wordList[i], onlyWordsByDoc[d][wIndex_in_now_doc_WordIndex])

            # if wIndex_in_now_doc_WordIndex > -1:
                index = d * (k+1)
                para1 = math.log(int(dict_DocCountWord[i][j][1]))
                para2 = math.log(P_T_wd[index][i])

                # molecular
                molecular += para1 + para2

                # denominator
                # now_doc_WordIndex = noCount_w_d[d]
                # for ni in range(len(now_doc_WordIndex)):
                #     _i = int(now_doc_WordIndex[ni][1])
                #     # index = d * (k+1)
                #     deno_para1 = math.log(int(count_w_d[ d ][ni][1]))
                #     deno_para2 = math.log(P_T_wd[index][_i])
                #     denominator += deno_para1 + deno_para2

            if w_T_denominator <= 0:
                w_T_denominator = 1e-6
            P_w_T[i][k] = molecular / w_T_denominator
        # print("finish P_w_T")

        # compute P_T_d , # all documents
        for d in range(dNumber):
            molecular = 0
            denominator = 0
            now_doc_WordIndex = noCount_w_d[d]
            wIndex_in_now_doc_WordIndex = -1

            #  all words in a document
            for dd in range(len(now_doc_WordIndex)):
                _i = int(now_doc_WordIndex[dd][1])
                index = d * (k+1)
                mole_para1 = math.log(int(count_w_d[ d ][dd][1]))
                mole_para2 = math.log(P_T_wd[index][_i])

                molecular += mole_para1 + mole_para2

                denominator += mole_para1

            if denominator <= 0:
                denominator = 1e-6
            # print(i, molecular, denominator)
            P_T_d[k][d] = molecular / denominator
        # print("finish P_T_d")

max_likehood = 0
def compute_max_likehood():
    max_likehood = 0

    for i in range(wNumber):
        for j in range(len(dict_DocCountWord[i])):
            P_wT_Td = 0
            for k in range(topicNum):
                P_wT_Td += P_w_T[i][k] * P_T_d[k][dict_DocCountWord[i][j][0]]
            max_likehood += int(dict_DocCountWord[i][j][1]) * math.log(P_d[j] * P_wT_Td)
    return max_likehood
def train():
    startTrain = datetime.now()
    fname = "../maxLikehood_" + str(datetime.now().strftime('%Y-%m-%d')) + ".log"
    f = open(fname, 'w')
    for i in range(1, 20):
        startE = datetime.now()
        e_step()
        print("iteration %d, E-step excution time = %.10s"%(i,  datetime.now()-startE))

        startM = datetime.now()
        m_step()
        print("iteration %d, M-step excution time = %.10s"%(i,  datetime.now()-startM))

        max_likehood = compute_max_likehood()

        nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
        f.write("%s  iteration %d, max-likelihood = %.10f\n"%(nowTime, i, max_likehood))
        # print("%s  iteration %d, max-likelihood = %.6f"%(nowTime, i, max_likehood))
    f.close()
    print(str(i) + " train excution time is ", datetime.now()-startTrain)

print("\ntrain start")
train()
print("train stop\n")
