import os
import dictionary
import getFileList

def createDocumentTF():
    allDictionary = dictionary.getDictionary()
    fileList = getFileList.getIntsFromFile()

    fname = './initialResult/documentTFResult.txt'
    res =  os.path.isfile(fname)
    if res:
        pass
    else:
        f = open(fname, 'w')
        for sub in allDictionary:
            strWrite = ""
            docIndex = 0
            for fv in fileList:
                c_wd = fv.count(sub)
                # if c_wd > 0:
                strWrite += " " + str(c_wd)
                # strWrite += " " + str(docIndex) + ":" + str(c_wd)
                docIndex+=1
            f.write(strWrite + "\n")
        f.close()

def getDocumentTF():
    createDocumentTF()

    res = []
    with open('./initialResult/documentTFResult.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(list(map(int, strTemp.split() )) )
    return res

res = getDocumentTF()
print("len(res): " , len(res))

k =0
for v in res:
    if k < 3:
        print(v)
        k  = k + 1
