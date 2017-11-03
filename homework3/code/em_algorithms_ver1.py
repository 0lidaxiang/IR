#!/usr/bin/python3
# coding: utf-8

# import initialProbability
import numpy as np, numpy.random
import math
from operator import mul

# import datetime
from datetime import datetime

import dictionary
import document
import wordDocsCount

Tnumber = 5
docList = document.getFilesName()
wordList = dictionary.getDictionary()
# wordDocCount = getWordDocCount
# wNumber = 122
wNumber = len(wordList)
# dNumber = 22 # 2265
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

    start = datetime.now()
    print("\n -------------------- P_T_wd start -------------------- ")
    # np.ones(wNumber) is rows , size=dNumber is cols
    # P_T_wd = np.random.dirichlet(np.ones(wNumber),size=dNumber)
    for k in range(topicNum):
            temp_P_T_d = np.random.dirichlet(np.ones(wNumber),size=dNumber).tolist()
            P_T_wd.append(temp_P_T_d)

    print("P_T_wd size : ", len(P_T_wd))
    print("P_T_wd[0] size : ", len(P_T_wd[0]))
    print("P_T_wd[0][0] size : ", len(P_T_wd[0][0]))
    print("P_T_wd[0][0] type : ", type(P_T_wd[0][0]))
    print("P_T_wd[0][0][0] type : ", type(P_T_wd[0][0][0]))
    # print("topicNum : ", int(int(len(P_T_wd)) / dNumber))

    print(" -------------------- P_T_wd stop" , datetime.now()-start, " -------------------- \n")
# -------------------- EM algorithm -----------------------------
def e_step():
    for k in range(topicNum):
        for j in range(dNumber):
            for i in range(wNumber):
                # print(type(P_w_T[i]))
                sum_w_t_d = sum(list(map(mul, P_w_T[i], P_T_d[j])))
                # for _k in range(topicNum):
                    # sum_w_t_d += P_w_T[i][_k] * P_T_d[j][_k]
                if sum_w_t_d <= 0:
                    sum_w_t_d = 1e-6
                # print(k,i,j)
                # print(type( P_w_T[i][k]))
                # print(P_T_wd[k][j][i])
                P_T_wd[k][j][i] = P_w_T[i][k] * P_T_d[j][k] / sum_w_t_d
                # print(P_T_wd[k][j][i])

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
            for j in range(dNumber):
                for _i in range(wNumber):
                    count_w_d_i_j = 0
                    for value in count_w_d[j]:
                        if value[0] == wordList[_i]:
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
            for j in range(dNumber):
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
    for i in range(1, 3):
        start = datetime.now()
        e_step()
        print("iteration %d, E-step excution time = %.10s"%(i,  datetime.now()-start))

        start = datetime.now()
        m_step()
        print("iteration %d, M-step excution time = %.10s"%(i,  datetime.now()-start))
        compute_max_likehood()

        nowTime = datetime.now().strftime('%Y-%m-%d %H:%M:%S');
        f.write("%s  iteration %d, max-likelihood = %.10f\n"%(nowTime, i, max_likelihood))
        # print("%s  iteration %d, max-likelihood = %.6f"%(nowTime, i, max_likelihood))
    f.close()
    print(str(i) + " train excution time is ", datetime.now()-start)

start = datetime.now()
print("\ninitialProbability start")
initialProbability()
print("initialProbability stop\n" , datetime.now()-start)


print("\ntrain start")
train()
print("train stop\n")
