import json
import urllib.request, urllib.parse, urllib.error
import ssl


url = input("Enter location: ")
print("Retrieving ", url)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

try:
    js = json.loads(data)
except:
    js = None
    quit()
comments = list(js["comments"])
print("Count: ", len(comments))
tot = 0
for item in comments:
    num = item["count"]
    tot = tot + int(num)
print("Sum: ", tot)