#prompt for a file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print("File can not be opened:",fname)
    quit()

#search for X-DSPAM-Confidence: line by line
tot = 0
count = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        pos = line.find('0')
        num = line[pos:]
        tot += float(num)
        count += 1
print("Average spam confidence:", tot/count)