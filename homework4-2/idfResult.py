import os
import dictionary
import getFileList

def createIDFFile():
    allDocumentNumber = 2265.0
    fname = "./initialResult/idfResult.txt"
    res =  os.path.isfile(fname)
    if res:
        # print fname + ' file has exists.'
        pass
    else:
        f = open(fname, 'w')
        dIDFs = []
        allDictionary = dictionary.getDictionary()
        fileList = getFileList.getFilesListFromFile()
        for sub in allDictionary:
            dIDF = {}
            dIDFsub = 0

            for fv in fileList:
                if sub in fv.split():
                    dIDFsub = dIDFsub + 1
            idfNum = allDocumentNumber / dIDFsub
            strWrite = sub + " "  + str(idfNum)

            f.write(strWrite + "\n")
        f.close()

        # print "Write to " + fname + "file over."

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
# print "len(res): " , len(res)
#
# k =0
# for v in res:
#     if k < 10:
#         print v
#         k  = k + 1
