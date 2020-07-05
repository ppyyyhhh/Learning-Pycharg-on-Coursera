#prompt for a file name
fname = input('Enter file name: ')
try:
    fh = open(fname)
except:
    print("File can not be opened:",fname)
    quit()
#print line by line
for line in fh:
    line = line.rstrip()
    print(line.upper())