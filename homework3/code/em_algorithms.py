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
noCount_w_dNum = len(noCount_w_d)
print("initialProbability stop " , datetime.now()-start, "\n")

max_likehood = 0

# -------------------- EM algorithm -----------------------------
def e_step():

    for d in range(dNumber):
        d_noCount_w_d = noCount_w_d[d]
        d_noCount_w_dNum = len(d_noCount_w_d)
        for ni in range(d_noCount_w_dNum):
            i = int(d_noCount_w_d[ni][1])
            sum_w_t_d = 0
            for kk in range(topicNum):
                sum_w_t_d += math.log10( P_w_T[i][kk]) + math.log10(P_T_d[kk][d])
            if sum_w_t_d <= 0:
                sum_w_t_d = 1e-6

            for k in range(topicNum):
                P_w_T_i_k = math.log10(P_w_T[i][k])
                P_T_d_k_d = math.log10( P_T_d[k][d])
                index = d * k
                P_T_wd[index][i] = (P_w_T_i_k + P_T_d_k_d) / sum_w_t_d

    # for i in range(wNumber):
    #     for d in range(dNumber):
    #         if ("".join([wordList[i], " "])) in noCount_w_d[d]:
    #             # print( wordList[i]+ " ",  noCount_w_d[d], "\n")
    #             sum_w_t_d = 0
    #             for kk in range(topicNum):
    #                 sum_w_t_d += math.log10( P_w_T[i][kk]) + math.log10(P_T_d[kk][d])
    #             if sum_w_t_d <= 0:
    #                 sum_w_t_d = 1e-6
    #
    #             for k in range(topicNum):
    #                 P_w_T_i_k = math.log10(P_w_T[i][k])
    #                 P_T_d_k_d = math.log10( P_T_d[k][d])
    #                 index = d * k
    #                 P_T_wd[index][i] = (P_w_T_i_k + P_T_d_k_d) / sum_w_t_d
def m_step():
    # compute P_w_T
    for k in range(topicNum):
        for i in range(wNumber):
            sum_cw_d_P_T_wd = 0
            sum_Allcw_d_P_T_wd = 0
            for j in range(dNumber):
                count_w_d_i_j = 0
                if count_w_d[j][i][0] == wordList[i]:
                    count_w_d_i_j = count_w_d[j][i][1]

                index = j * k
                sum_cw_d_P_T_wd += count_w_d_i_j  * P_T_wd[index][i]

                for _i in range(wNumber):
                    count_w_d_i_j = 0
                    for value in count_w_d[j]:
                        if value[0] == wordList[_i]:
                            count_w_d_i_j = count_w_d[j][_i][1]
                    sum_Allcw_d_P_T_wd += count_w_d_i_j  * P_T_wd[index][_i]
            if sum_Allcw_d_P_T_wd <= 0:
                sum_Allcw_d_P_T_wd = 1e-6
            P_w_T[i][k] = sum_cw_d_P_T_wd / sum_Allcw_d_P_T_wd

        # compute P_T_d
        for j in range(dNumber):
            sum_cw_d_P_T_wd = 0
            sum_Allcw_d = 0
            for i in range(wNumber):
                count_w_d_i_j = 0
                if count_w_d[j][i][0] == wordList[i]:
                    count_w_d_i_j = count_w_d[j][i][1]

                index = j * k
                sum_cw_d_P_T_wd += count_w_d_i_j  * P_T_wd[index][i]

                for _i in range(wNumber):
                    count_w_d_i_j = 0
                    if count_w_d[j][_i][0] == wordList[_i]:
                        count_w_d_i_j = count_w_d[j][_i][1]
                    sum_Allcw_d += count_w_d_i_j

            if sum_Allcw_d <= 0:
                sum_Allcw_d = 1e-6
            P_w_T[i][k] = sum_cw_d_P_T_wd / sum_Allcw_d

def compute_max_likehood():
    temp_max_likehood = 0
    for i in range(wNumber):
        for j in range(dNumber):
            P_wT_Td = 0
            for k in range(topicNum):
                P_wT_Td += P_w_T[i][k] * P_T_d[k][j]
            temp_max_likehood += count_w_d[i][j] * math.log(P_d[j] * P_wT_Td)
    max_likelihood = temp_max_likehood

def train():
    start = datetime.now()
    fname = "../maxLikehood_" + str(datetime.now().strftime('%Y-%m-%d')) + ".log"
    f = open(fname, 'w')
    for i in range(1, 51):
        start = datetime.now()
        e_step()
        print("iteration %d, E-step excution time = %.10s"%(i,  datetime.now()-start))

        # start = datetime.now()
        # m_step()
        # print("iteration %d, M-step excution time = %.10s"%(i,  datetime.now()-start))
        # compute_max_likehood()
        #
        # nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
        # f.write("%s  iteration %d, max-likelihood = %.10f\n"%(nowTime, i, max_likelihood))
        # print("%s  iteration %d, max-likelihood = %.6f"%(nowTime, i, max_likelihood))
    f.close()
    print(str(i) + " train excution time is ", datetime.now()-start)



print("\ntrain start")
train()
print("train stop\n")
