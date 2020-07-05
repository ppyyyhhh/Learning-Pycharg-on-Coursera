#Counting with the dictionaries
count = dict()
names = ['csev','cwen','csev','zqian','cwen',]
for name in names:
    if name not in count:
        count[name]=1
    else:
        count[name] += 1
print(count)

#get method for dic
counts = dict()
for name in names:
    counts[name] = counts.get(name,0)+1  #get the name times from counts, if no then defaul is 0.
print(counts)