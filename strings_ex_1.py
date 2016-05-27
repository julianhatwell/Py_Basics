text = "X-DSPAM-Confidence:    0.8475";
opos = text.find("0")
epos = len(text)
flo = float(text[opos:epos+1])
print(flo)