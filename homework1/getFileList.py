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

def createFilesListFile():
    fname = "filesList.txt"
    res =  os.path.isfile(fname)
    if res:
        print 'file has exists.'
    else:
        f = open(fname, 'w')
        fileList = getFilesList()
        for fileStr in fileList:
            f.write(fileStr + "\r\n")
        f.close()
        print "Write to file over."

def getFilesListFromFile():
    createFilesListFile()
    new = []
    with open('./filesList.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        new.append(strTemp)

    return new


# res1 = getFilesListFromFile()
# res2 = getFilesList()
# print res1==res2
res = getFilesListFromFile()
print "len(res): " , len(res)

k =0
for v in res:
    if k < 10:
        print v
        k  = k + 1
