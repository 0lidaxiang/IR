import os

def getQueryFilesString():
    dTFs = []
    path = "./Query"
    files= os.listdir(path)
    queryFiles = []
    for file in files:
        f = open(path+"/"+file);
        iter_f = iter(f);
        strtemp = ""
        lineNumber = 1

        for line in iter_f:
            strtemp = strtemp + line.rstrip("-1\r\n")
            lineNumber = lineNumber + 1
        queryFiles.append(strtemp)

    return queryFiles
def getQueryFilesList():
    queryFiles = getQueryFilesString()
    queryFilesList = []
    for value in queryFiles:
        queryFilesList.append(value.split())
    return queryFilesList
