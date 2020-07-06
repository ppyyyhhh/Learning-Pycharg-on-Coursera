import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts=dict()
sum = 0
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] =counts.get(word,0)+1
        sum += 1
    print(line.decode().strip())
print('\n', counts)
print(sum)