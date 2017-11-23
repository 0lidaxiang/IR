import os

def getFileNameList():
    fname = "./data/doc_list.txt"
    res = []
    with open(fname) as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

def getFilesList():
    path = "./data/Document"
    files= getFileNameList()
    fileList = []

    for fileName in files:
        f = open(path+"/"+fileName);
        iter_f = iter(f);
        strtemp = ""
        lineNumber = 1

        for line in iter_f:
            if lineNumber > 3:
                strtemp = strtemp + line.rstrip("-1\r\n")
            else:
              lineNumber = lineNumber + 1
        fileList.append(strtemp)
    return fileList

def getDocsList():
    initialResultDir = "./initialResult/"
    fname = initialResultDir + "allDocsLength.txt"
    res =  os.path.isfile(fname)
    docsLength = []
    if res:
        pass
    else:
        fileList = getFilesList()
        for fileStr in fileList:
            docsLength.append(len(fileStr.split()))
    return docsLength

# res = createFilesListFile()
# print( "len(res): " , len(res))

# k =0
# for v in res:
#     if k < 10:
#         print (v)
#         k  = k + 1
