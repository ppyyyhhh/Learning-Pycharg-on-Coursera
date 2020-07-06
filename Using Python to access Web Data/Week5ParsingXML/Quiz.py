import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
from xml.etree.ElementTree import Element

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter location: ')
print('Retrieving', url)
fh = urllib.request.urlopen(url, context=ctx)

data = fh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)
tot = 0
counts = tree.findall('.//count')
count = len(counts)
print(count)
for item in counts:
    value = item.text   #no need for find() here, because the findall() before.
    num = int(value)
    tot = tot + num

print('Count: ', count)
print('Sum: ', tot)