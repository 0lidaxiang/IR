import os

def getFileNameList():
    fname = "./data/query_list.txt"
    res = []
    with open(fname) as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

def getFilesList():
    path = "./data/Query"
    files= getFileNameList()
    fileList = []

    for fileName in files:
        f = open(path+"/"+fileName);
        iter_f = iter(f);
        strtemp = ""
        lineNumber = 1

        for line in iter_f:
            strtemp = strtemp + line.rstrip("-1\r\n")
            lineNumber = lineNumber + 1
        fileList.append(strtemp)
    return fileList

def createFilesListFile():
    initialResultDir = "./initialResult/"
    fname = initialResultDir + "allQuerys.txt"
    res =  os.path.isfile(fname)
    if res:
        pass
    else:
        if not os.path.isdir(initialResultDir):
            os.mkdir(initialResultDir)
        f = open(fname, 'w')
        fileList = getFilesList()
        for fileStr in fileList:
            f.write(fileStr + "\r\n")
        f.close()

def getFilesListFromFile():
    createFilesListFile()
    new = []
    with open('./initialResult/allQuerys.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        new.append(strTemp)

    return new

def getIntsFromFile():
    createFilesListFile()
    new = []
    with open('./initialResult/allQuerys.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        new.append(list(map(int, strTemp.split())))

    return new

# res = getIntsFromFile()
# print( "len(res): " , len(res))
#
# k =0
# for v in res:
#     if k < 1:
#         print (v)
#         k  = k + 1
