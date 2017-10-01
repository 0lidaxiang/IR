# coding: utf-8
import os
import hw1_0
import hw1_1

# stpe -1 : get the query list
queryFilesList = hw1_0.getQueryFilesList()
# print queryFilesList[0]

# step0: get the dictionary
# allDictionary = hw1_1.getDictionary()
# print allDictionary

# for sub in queryFilesList[0]:
#     print sub
# print queryFilesList[0]


# step1: document term weight
# TF: 每個query的每個單詞在某個文檔裏面出現次數
# [{"word in a query" : countInADocument, "document name": documentName},

# {"another word in a query" : countIn Another Document, "document name": documentName},
# ]
# IDF： 在所有文檔裏面，包含一個query的一個單詞的文檔有多少個，然後每個query的每個單詞


dTFs = []
path = "./Document"
files= os.listdir(path)
fileList = []
fileNameList = []
for file in files:
    f = open(path+"/"+file);
    iter_f = iter(f);
    strtemp = ""
    lineNumber = 1

    fileNameList.append(file)
    # print file

    for line in iter_f:
        if lineNumber > 3:
            # print "str.count(sub) : ", str.count(sub)
            strtemp = strtemp + line
        else:
          lineNumber = lineNumber + 1

    fileList.append(strtemp)

print len(fileNameList)
print fileNameList[0]
print len(fileList)

i = 0
for sub in queryFilesList[0]:
    dTF = {}
    # print strtemp.count(sub)
    for fv in fileList:
        dTF["documentName"] = fileNameList[i]
        i = i + 1

        dTF[sub] = fv.count(sub)
        dTFs.append(dTF)
# print fileList
print type(dTFs[1])
print len(dTFs)

# print dTF
# print len(fileList)



#
# print "\n"

# step2: query term weight
# TF: 每個query的每個單詞在 query 裏面出現次數

# step3:
# document term weight 向量
# query term weight 向量

# step4: 向量點乘

# step5: 計算 cos

# step6: 排序比較對於這個 query ，最接近的結果，也就是找到的 document 相似度

# step7: 找到所有的 query 的 排序結果
