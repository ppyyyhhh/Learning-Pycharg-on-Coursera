import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
counts = int(input('Enter count :'))
position = input('Enter position :')
position = int(position)

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
i = 0
for tag in tags:
    tempurl = tag.get('href', None)
    i += 1
    if i == position:
        print("Retrieving: ", tempurl)
        break
count = 1
while count < counts:
    count += 1
    urlloop = tempurl
    htmlloop = urllib.request.urlopen(urlloop, context=ctx).read()
    tempsoup = BeautifulSoup(htmlloop, 'html.parser')
    temptags = tempsoup('a')
    i = 0
    for tag in temptags:
        tempurl = tag.get('href', None)
        i += 1
        if i == position:
            print("Retrieving: ", tempurl)
            break
