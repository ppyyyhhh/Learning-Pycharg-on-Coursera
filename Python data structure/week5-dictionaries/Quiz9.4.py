name = input("Enter file:")
handle = open(name)
counts = dict()
#countig addressm
for line in handle:
    if line.startswith("From "):
        words = line.split()
        counts[words[1]] = counts.get(words[1],0)+1
#sorting the counts
Maxv = None
Maxk = None
for k,v in counts.items():
    if Maxv is None or v > Maxv:
        Maxv = v
        Maxk = k
print(Maxk,Maxv)