fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lineList = line.split()
    for word in lineList:
        if word in lst: continue
        lst.append(word)
lst.sort()
print(lst)