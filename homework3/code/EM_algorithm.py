#!/usr/bin/python3
# coding: utf-8

# import initialProbability
import numpy as np, numpy.random
import math
# import datetime
from datetime import datetime

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

    for k in range(topicNum):
        temp_P_T_d = []
        for j in range(dNumber):
            temp_P_T_d.append(np.random.dirichlet(np.ones(wNumber),size=1).tolist()[0])
        P_T_wd.append(temp_P_T_d)

    # for i in range(wNumber):
    #     wd = []
    #     for j in range(dNumber):
    #         d = []
    #         for k in range(topicNum):
    #             floatPro = np.random.dirichlet(np.ones(topicNum),size=1)
    #             d.append(floatPro.tolist()[0])
    #         wd.append(d)
    #     P_T_wd.append(wd)
# -------------------- EM algorithm -----------------------------
def e_step():

    for k in range(topicNum):
        for j in range(dNumber):
            for i in range(wNumber):
                sum_w_t_d = 0
                for _k in range(topicNum):
                    sum_w_t_d += P_w_T[i][_k] * P_T_d[j][_k]
                if sum_w_t_d <= 0:
                    sum_w_t_d = 1e-6
                # print(k,i,j)
                P_T_wd[k][j][i] = P_w_T[i][k] * P_T_d[j][k] / sum_w_t_d

def m_step():
    # compute P_w_T
    for k in range(topicNum):
        for i in range(wNumber):
            sum_cw_d_P_T_wd = 0
            for j in range(dNumber):
                count_w_d_i_j = 0
                if count_w_d[j][i][0] == wordList[i]:
                    count_w_d_i_j = count_w_d[j][i][1]
                sum_cw_d_P_T_wd += count_w_d_i_j  * P_T_wd[k][j][i]

            sum_Allcw_d_P_T_wd = 0
            for _i in range(wNumber):
                for j in range(dNumber):
                    count_w_d_i_j = 0
                    if count_w_d[j][_i][0] == wordList[_i]:
                        count_w_d_i_j = count_w_d[j][_i][1]
                    sum_Allcw_d_P_T_wd += count_w_d_i_j  * P_T_wd[k][j][_i]
            if sum_Allcw_d_P_T_wd <= 0:
                sum_Allcw_d_P_T_wd = 1e-6
            P_w_T[i][k] = sum_cw_d_P_T_wd / sum_Allcw_d_P_T_wd

    # compute P_T_d
    for k in range(topicNum):
        for j in range(dNumber):
            sum_cw_d_P_T_wd = 0
            for i in range(wNumber):
                count_w_d_i_j = 0
                if count_w_d[j][i][0] == wordList[i]:
                    count_w_d_i_j = count_w_d[j][i][1]
                sum_cw_d_P_T_wd += count_w_d_i_j  * P_T_wd[k][j][i]

            sum_Allcw_d = 0
            for _i in range(wNumber):
                for j in range(dNumber):
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
        e_step()
        m_step()
        compute_max_likehood()

        nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
        f.write("%s  iteration %d, max-likelihood = %.6f\n"%(nowTime, i, max_likelihood))
        print("%s  iteration %d, max-likelihood = %.6f"%(nowTime, i, max_likelihood))
    f.close()
    print(str(i) + " train excution time is ", datetime.now()-start)

start = datetime.now()
print("\ninitialProbability start")
initialProbability()
print("initialProbability stop\n" , datetime.now()-start)


print("\ntrain start")
train()
print("train stop\n")