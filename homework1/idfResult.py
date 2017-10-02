import os
import dictionary
import getFileList

def createIDFFile():
    fname = "idfResult.txt"
    res =  os.path.isfile(fname)
    if res:
        print fname + ' file has exists.'
    else:
        f = open(fname, 'w')
        dIDFs = []
        allDictionary = dictionary.getDictionary()
        fileList = getFileList.getFilesList()

        for sub in allDictionary:
            dIDF = {}
            dIDFsub = 0

            for fv in fileList:
                if sub in fv:
                    dIDFsub = dIDFsub + 1

            strWrite = sub + " "  + str(dIDFsub)

            f.write(strWrite + "\n")
        f.close()
        print "Write to file over."

def getIDF():
    createIDFFile()

    res = []
    with open('./idfResult.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

res =  getIDF()
print "len(res): " , len(res)

k =0
for v in res:
    if k < 10:
        print v
        k  = k + 1
