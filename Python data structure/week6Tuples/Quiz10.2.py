name = input("Enter file:")
handle = open(name)
Counts = dict()
for line in handle:
    if line.startswith("From "):
        words = line.split()
        time = words[5]
        hours = time[:2]
        Counts[hours] = Counts.get(hours,0) + 1

print(sorted([(k,v) for k,v in Counts.items()]))

for k,v in sorted(Counts.items()):
    print(k,v)