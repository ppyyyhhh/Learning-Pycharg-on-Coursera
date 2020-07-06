import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

#ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter the url here: ')
html = urllib.request.urlopen(url,context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

#revieve all numbers
count = 0
sum = 0
tags = soup('span')
for tag in tags:
    value = tag.contents[0]
    count += 1
    sum = sum + int(value)
print("Count", count)
print("Sum", sum)