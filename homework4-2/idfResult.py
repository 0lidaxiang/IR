import os
import getFileList

def createIDFFile():
    allDocumentNumber = 2265.0
    fname = "./initialResult/idfResult.txt"
    res =  os.path.isfile(fname)
    if res:
        pass
    else:
        f = open(fname, 'w')
        dIDFs = []
        fileList = getFileList.getFilesListFromFile()
        for sub in range(0, 51253):
            dIDF = {}
            dIDFsub = 0
            for fv in fileList:
                if sub in fv:
                    dIDFsub = dIDFsub + 1
            strWrite = ""
            if dIDFsub > 0:
                idfNum = allDocumentNumber / dIDFsub
                strWrite = str(idfNum) + " "
            f.write(strWrite + "\n")
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

# res =  getIDF()
# print("len(res): " , len(res))
#
# k =0
# for v in res:
#     if k < 10:
#         print(v)
#         k  = k + 1
