import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl

print("*calling Twitter...")
url = augment('http//api.twitter.com/1.1statusesuser_timeline.json',
              {'screen_name':'drchuck','count':'2'})
print(url)

#ignore ssl certificate errors



connection = urllib.request.urlopen(url, context=ctx)
data = connection.read()
print(data)  #dump the json, not decode yet. shoudl be byte content, not unicode

print('================')
headers = dict(connection.getheaders())
print(headers)

