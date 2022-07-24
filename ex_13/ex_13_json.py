import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
if len(url) < 1:
    url = 'http://py4e-data.dr-chuck.net/comments_42.json'

print('Retrieving:',url)
uh = urllib.request.urlopen(url, context = ctx)
data = uh.read().decode()
print('Retrieved',len(data),'characters')

info = json.loads(data)

sum = 0
counts = 0

for item in info['comments']:
    num = item['count']
    sum = sum + int(num)
    counts = counts + 1

print('Count:',counts)
print('Sum:',sum)
