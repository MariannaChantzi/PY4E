import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter url: ')

if len(url) < 1:
    url = 'https://py4e-data.dr-chuck.net/comments_42.html'

html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

spans = soup('span')
sum = 0
count = 0

for span in spans:
    str_num = span.contents[0].strip()
    num = int(str_num)
    sum = sum + num
    count = count + 1

print('Sum:',sum)
print('Count:', count)
