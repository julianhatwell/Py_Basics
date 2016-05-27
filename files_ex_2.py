# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
nlines = 0
runtot = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    nlines += 1
    colpos = line.find(":")
    rawval = line[colpos+1:len(line)+1]
    val = float(rawval.strip())
    runtot += val

print("Average spam confidence: " + str(runtot/nlines))