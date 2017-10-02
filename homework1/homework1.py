# coding: utf-8
import os
import queryList

import dictionary
import documentTF
import queryTF
import idfResult

# stpe 0 : get the query list
queryFilesList = queryList.getQueryFilesList()
# print queryFilesList[0]

# step1 : get the dictionary and document tf,idf and query tf
allDictionary = dictionary.getDictionary()
documentTF = documentTF.getDocumentTF()
idf = idfResult.getIDF()
queryTF = queryTF.getQueryTF()


# step2 : document term weight
# TF: 字典裏 的每個單詞在某個文檔裏面出現次數
# [{"word name " :  documentName - list[{documentName : wordOccursTimes}]},
# ]
# IDF： 在所有文檔裏面，包含字典裏 的一個單詞的文檔有多少個，然後每個query的每個單詞
# [{"word in a query" : document number that contains this word},
# ]

# print "----------start print result2 ----------------"
# k =0
# for v in dIDFs:
#     if k < 10:
#         print v
#         k  = k + 1
#
# # print len(dTFs)
# # print "\n"

# step3 : query term weight
# TF: 字典的每個單詞在 query 裏面出現次數


# step4 :
# document term weight 向量
# query term weight 向量


# step5 : 向量點乘

# step6 : 計算 cos

# step7 : 排序比較對於這個 query ，最接近的結果，也就是找到的 document 相似度

# step8: 找到所有的 query 的 排序結果
