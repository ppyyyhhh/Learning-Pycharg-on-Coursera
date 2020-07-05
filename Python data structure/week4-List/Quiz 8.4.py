fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = list(line.split())
    for word in words:
        if word in lst:     #check if the word exist in the list
            continue
        else:
            lst.append(word)
print(sorted(lst))