# coding: utf-8

import os
import collections

path = "./data/Document"
files= os.listdir(path)
s = []
for file in files:
    f = open(path+"/"+file);
    iter_f = iter(f);
    strtemp = ""
    lineNumber = 1
    for line in iter_f:
        if lineNumber > 3:
            strtemp = strtemp + line
        else:
          lineNumber = lineNumber + 1
    s.append(strtemp)

def getDictionary():
    all_the_text = "".join(str(x) for x in s)

    result = []

    for word in all_the_text.split():
        if word not in result:
            result.append(word)

    return result


# f = open('IR-Homework1-Result.txt', 'w')
# for key,value in dword.items():
# #      print key.rjust(8) + " : "  + repr(value).rjust(6)
# #      f.write( key.rjust(8) + " : "  + repr(value).rjust(6) + "\n")  # python will convert \n to os.linesep
#       f.write("%-*s%-*s%-*s"%(8,key, 4,":", 8,value) + "\n")  # python will convert \n to os.linesep
# f.close()
# print "Write to file over."
