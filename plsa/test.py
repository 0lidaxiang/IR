fname = "./Collection.txt"
with open(fname) as f:
    lines = f.read().splitlines()
res = []
for line in lines:
    res.append( list(map(int, line.split())))
print(len(res))

fname = "./allFilesContent.txt"
with open(fname) as f:
    lines = f.read().splitlines()
res2 = []
for line in lines:
    res2.append( list(map(int, line.split())))
print(len(res2))

for i in range(60000):
    print("----" , i)
    for value1 in res:
        if i in value1:
            for value in res2:
                if i in value:
                    print(i)
