# coding: utf-8
import os
import numpy as np

import computeAqueryForADoc as compute

# stpe 0 : get the query list

# step1 : get the dictionary and document tf,idf and query tf

# step2 : document term weight，先取得一個 document 作爲豎着向量
# step3 : query term weight， 作爲橫着向量

# step4 :compute the 向量點乘
#   document term weight 向量
#   query term weight 向量

# step5 : compute the 向量長度

# step6 : 計算 cos

# step7 : 排序比較對於這個 query ，最接近的結果，也就是找到的 document 相似度

# step8: 找到所有的 query 的 排序結果
print "------------------------------ Main Program Start ----------------"
# queryFilesList = queryList.getQueryFilesList()
# resultIndex = 1
# for query in queryFilesList:
#     compute.computeAquery(resultIndex - 1)
#     print str(resultIndex).ljust(2) , " compute  " + query["fileName"] + " over. "
#     resultIndex += 1

res = compute.computeAquery(14)
print "len(res): " , len(res)
k = 0
for v in res:
    # if v < 0.3:
        if k < 10:
            k+=1
            print v
print "------------------------------ Main Program  Over ----------------"
