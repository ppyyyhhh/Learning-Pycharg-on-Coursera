import re
handle = open('regex_sum_754797.txt')
numlist = list()
for line in handle:
    line = line.rstrip()
    digits = list()
    digits = re.findall('[0-9]+', line)
    for i in range(len(digits)):
         num = digits[i]
         value = float(num)
         numlist.append(value)
print(sum(numlist))
