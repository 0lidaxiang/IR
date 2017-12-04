import os

# def getFilesList():
#     path = "./data/Document/"
#     files= getFileNameList()
#     fileList = []
#
#     for fileName in files:
#         with open(path + fileName, encoding="gbk", errors='ignore') as f:
#             # lines = f.read().splitlines()
#             lines = ''.join(f.read().splitlines())
#             fileList.append(lines)
#     return fileList

def getFileNameList():
    fname = "./initialResult/fileNameList.txt"
    res1 =  os.path.isfile(fname)
    if res1:
        pass
    else:
        subPathL = ["C000008", "C000010", "C000013", "C000014", "C000016", "C000020", "C000022", "C000023", "C000024"]
        path = "./data/Document"
        f = open(fname, 'w')
        for subPath in subPathL:
            files= os.listdir(path + "/" + subPath)
            # for fileName in files:
                # f.write(subPath + "/" + str(fileName) + "\r\n")
            for fileName in range(11,2000):
                f.write(subPath + "/" + str(fileName) + ".txt\r\n")
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
        pass
    else:
        fw = open(fname, 'w')
        path = "./data/Document/"
        files= getFileNameList()
        for fileName in files:
            with open(path + fileName, encoding="gbk", errors='ignore') as f:
                lines = ''.join(f.read().splitlines())
                fw.write(lines + "\r\n")
        fw.close()
        # print "Write to file over."

def getFilesListFromFile():
    createFilesListFile()
    new = []
    with open('./initialResult/filesList.txt', encoding="utf8", errors='ignore') as f:
        lines = f.read().splitlines()
    for line in lines:
        strTemp = ''.join(line.split("\r\n"))
        new.append(strTemp)
    return new

def getAFile(filePath):
    with open(filePath, encoding="gbk", errors='ignore') as f:
        lines = f.read().splitlines()
        strTemp = ''.join(lines[0].split("\r\n"))
    return strTemp
# res = getFilesListFromFile()
# print ("len(res): " , len(res))
#
# k =0
# for v in res:
#     if k < 10:
#         print (v)
#         k  = k + 1
