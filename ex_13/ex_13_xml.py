import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read().decode()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

comments = tree.findall('comments/comment')

sum = 0
count = 0

for comment in comments:
    str_num = comment.find('count').text
    sum = sum + int(str_num)
    count = count + 1

print("Count:",count)
print('Sum:',sum)
