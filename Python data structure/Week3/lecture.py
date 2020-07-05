#read files in python

#open funcion  open(filename, mode)

fname = input('Enter the file name here:    ')

#xfile = open('xxx.txt')
for cheese in xfile:
    print(cheese)


try:
    fhand = open(fname)
except:
    print('File can not be opened:', fname)  #bad name, alert
    quit()

#line counter
count = 0
for line in fhand:
    count =count+1
print(count)

# reading the whold file

inp = fhand.read()
print(len(inp))
94626
print(inp[:20])

#search
for line in fhand:
    line = line.rstrip()  # use rstrip to remove the /n at the end of each line of the txt
    if line.startswith('From:')
        print(line)

