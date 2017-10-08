import os

def getFilesList():
    path = "./data/Document"
    files= os.listdir(path)
    fileList = []
    fileNameList = []

    for fileName in files:
        f = open(path+"/"+fileName);
        iter_f = iter(f);
        strtemp = ""
        lineNumber = 1

        fileNameList.append(fileName)

        for line in iter_f:
            if lineNumber > 3:
                strtemp = strtemp + line.rstrip("-1\r\n")
            else:
              lineNumber = lineNumber + 1
        fileList.append(strtemp)



    return fileList

def getFileNameList():

    fname = "./initialResult/fileNameList.txt"
    res1 =  os.path.isfile(fname)
    if res1:
        # print fname + 'file has exists.'
        pass
    else:
        path = "./data/Document"
        files= os.listdir(path)
        fileList = []

        f = open(fname, 'w')
        for fileName in files:
            f.write(fileName + "\r\n")
        f.close()

    res = []
    with open('./initialResult/fileNameList.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        res.append(strTemp)
    return res

def createFilesListFile():
    fname = "./initialResult/filesList.txt"
    res =  os.path.isfile(fname)
    if res:
        # print 'file has exists.'
        pass
    else:
        f = open(fname, 'w')
        fileList = getFilesList()
        for fileStr in fileList:
            f.write(fileStr + "\r\n")
        f.close()
        # print "Write to file over."

def getFilesListFromFile():
    createFilesListFile()
    new = []
    with open('./initialResult/filesList.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        new.append(strTemp)

    return new

# res = getFilesListFromFile()
# print "len(res): " , len(res)
#
# k =0
# for v in res:
#     if k < 10:
#         print v
#         k  = k + 1
