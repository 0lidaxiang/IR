import os
import dictionary
import getFileList
import jieba
import re

def createIDFFile():
    fname = "./initialResult/idfResult.txt"
    res =  os.path.isfile(fname)
    if res:
        pass
    else:
        f = open(fname, 'w')
        dIDFs = []
        allDictionary = dictionary.getDictionary()
        jieba.load_userdict("./data/dictionary_utf8.txt")
        fileList = getFileList.getFilesListFromFile()
        inde = 1
        for sub in allDictionary:
            dIDF = {}
            dIDFsub = 0
            # print(sub, seg_list, "\n")
            pattern = re.compile(sub)
            for fv in fileList:
                result1 = pattern.findall(fv)
                if len(result1) > 0:
                    dIDFsub += 1
            idfNum = dIDFsub
            strWrite = str(idfNum)
            # strWrite = sub + " "  + str(idfNum)
            f.write(strWrite + "\n")
            print(inde)
            inde += 1
        f.close()

def getIDF():
    createIDFFile()
    res = []
    with open('./initialResult/idfResult.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

# def utf8_Dic():
#     fw = open("./data/dictionary_utf8.txt", 'w')
#     with open('./data/dictionary.txt', encoding="gbk", errors='ignore') as f:
#         lines = f.read().splitlines()
#     for line in lines:
#         strTemp = ''.join(line.split("\r\n"))
#         fw.write(strTemp + "\n")
#     fw.close()
#
# utf8_Dic()
# res =  getIDF()
# print( "len(res): " , len(res))
#
# k =0
# for v in res:
#     if k < 10:
#         print (v)
#         k  = k + 1
