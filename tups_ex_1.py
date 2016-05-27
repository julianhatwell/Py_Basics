fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)

hrs = dict()

for line in fh:
    if line.startswith("From "):
        lineList = line.split()
        tim = lineList[5]
        timList = tim.split(':')
        hrs[timList[0]] = hrs.get(timList[0], 0) + 1

hist = sorted([(k,v) for k, v in hrs.items()])
for k, v in hist:
    print(str(k) + " " + str(v))