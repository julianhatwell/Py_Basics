fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

ems = dict()

for line in fh:
    if line.startswith("From "):
        lineList = line.split()
        ems[lineList[1]] = ems.get(lineList[1], 0) + 1
mx = 0
addr = None
for em in ems:
    if ems[em] > mx:
        mx = ems[em]
        addr = em
print(addr, mx)