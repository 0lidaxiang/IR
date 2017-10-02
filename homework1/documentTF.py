import os
import dictionary
import getFileList

def createDocumentTF():
    allDictionary = dictionary.getDictionary()
    fileList = getFileList.getFilesListFromFile()

    fname = 'documentTFResult.txt'
    res =  os.path.isfile(fname)
    if res:
        print fname + ' file has exists.'
    else:
        f = open(fname, 'w')
        # dIDFs = []
        for sub in allDictionary:
            # dIDF = {}
            # dIDF[sub] = 0

            dTF = {}
            dTFLists = []

            i = 0
            strWrite = sub + " "
            for fv in fileList:
                dTFList = {}
                strWrite = strWrite + " "  + str(fv.count(sub))

                i = i + 1
                dTFLists.append(dTFList)

            #     if sub in fv:
            #         dIDF[sub] = dIDF[sub] + 1
            # dIDFs.append(dIDF)

            f.write(strWrite + "\n")
        f.close()
        print "Write to file over."

def getDocumentTF():
    createDocumentTF()

    res = []
    with open('./documentTFResult.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

res = getDocumentTF()
print "len(res): " , len(res)

k =0
for v in res:
    if k < 10:
        print v
        k  = k + 1
