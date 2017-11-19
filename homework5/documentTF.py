import os
import dictionary
import getFileList

def createDocumentTF():
    allDictionary = dictionary.getDictionary()
    fileList = getFileList.getFilesListFromFile()

    fname = './initialResult/documentTFResult_sim.txt'
    res =  os.path.isfile(fname)
    if res:
        pass
    else:
        f = open(fname, 'w')
        for sub in allDictionary:
            strWrite = sub
            docIndex = 0
            for fv in fileList:
                c_wd = fv.split().count(sub)
                if c_wd > 0:
                    strWrite += " " + str(docIndex) + ":" + str()
                docIndex+=1
            f.write(strWrite + "\n")
        f.close()

def getDocumentTF():
    createDocumentTF()

    res = []
    with open('./initialResult/documentTFResult_sim.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(map(int, strTemp.split()) )
    return res

res = getDocumentTF()
print("len(res): " , len(res))

k =0
for v in res:
    if k < 10:
        print(v)
        k  = k + 1
