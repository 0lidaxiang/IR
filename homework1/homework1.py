# coding: utf-8
import os
import queryList

import dictionary
import documentTF
import queryTF
import idfResult

import numpy as np

# stpe 0 : get the query list
queryFilesList = queryList.getQueryFilesList()
# print queryFilesList[0]

# step1 : get the dictionary and document tf,idf and query tf
allDictionary = dictionary.getDictionary()
wordNumber = len(allDictionary)
documentTF = documentTF.getDocumentTF()
idfList = idfResult.getIDF()
queryTF = queryTF.getQueryTF()


# step2 : document term weight，先取得一個 document 作爲豎着向量
# TF: 字典裏 的每個單詞在某個文檔裏面出現次數
# [{"word name " :  documentName - list[{documentName : wordOccursTimes}]},
# ]
# IDF： 在所有文檔裏面，包含字典裏 的一個單詞的文檔有多少個，然後每個query的每個單詞
# [{"word in a query" : document number that contains this word},
# ]

print "\n------------ start compute the document weight vector -----------------"
document2WeightVec = []

index = 0
while index < wordNumber:
    tf = float(documentTF[index].split()[2])
    idf = float(idfList[0].split()[1])
    document2Weight = (tf * idf)
    document2WeightVec.append(document2Weight)
    index += 1

print "------------ finish compute the document weight vector -----------------\n"


# step3 : query term weight， 作爲橫着向量
# TF: 字典的每個單詞在 query 裏面出現次數
print "\n------------ start compute the query weight vector -----------------"
query1WeightVec = []

index = 0
while index < wordNumber:
    tf = float(queryTF[index].split()[1])
    idf = float(idfList[0].split()[1])
    query1Weight = (tf * idf)
    query1WeightVec.append(query1Weight)
    index += 1

print "------------ finish compute the query weight vector -----------------\n"

# step4 :compute the 向量點乘
# document term weight 向量
# query term weight 向量

print "\n\n\n------------ compute the cos value -----------------\n"
a = np.array(query1WeightVec)
b = np.array(document2WeightVec)
aL = np.sqrt(a.dot(a))
bL = np.sqrt(b.dot(b))

x = np.dot(a, b)
y = aL * bL
cos_angle = x / y
print "query1 and document2 cos_angle : " + str(cos_angle)

# step5 : compute the 向量長度

# step6 : 計算 cos

# step7 : 排序比較對於這個 query ，最接近的結果，也就是找到的 document 相似度

# step8: 找到所有的 query 的 排序結果
