# coding: utf-8
import os
import numpy as np

import queryList
import computeAqueryForADoc as compute

resultDic = "./result/"
if not os.path.exists(resultDic):
    os.mkdir(resultDic)

# stpe 0 : get the query list

# step1 : get the dictionary and document tf,idf and query tf

# step2 : document term weight，先取得一個 document 作爲豎着向量
# step3 : query term weight， 作爲橫着向量

# step4 :compute the 向量點乘
#   document term weight 向量
#   query term weight 向量

# step5 : compute the 向量長度

# step6 : 計算 cos

# step7 : 排序比較對於這個 query ，最接近的結果 cosVal 越大

# step8: 找到所有的 query 的 排序結果
print "------------------------------ Main Program Start ----------------"

queryFilesList = queryList.getQueryFilesList()
print len(queryFilesList)
resultIndex = 0
for query in queryFilesList:
    compute.computeAquery(resultIndex+1, resultDic + "res-" + queryFilesList[resultIndex]["fileName"])
    print str(resultIndex+1).ljust(2) , " compute  " + query["fileName"] + " over. "
    resultIndex += 1
print "------------------------------ Main Program  Over ----------------"
