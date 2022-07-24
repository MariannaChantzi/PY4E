import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

#Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
scount = input('Enter count: ')
sposition = input('Enter position: ')

try:
    count = int(scount)
    position = int(sposition)
except:
    print('Invalid input')
    quit()

i = 0

while i <= count:
    print('Retrieving: ', url)
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    tag = tags[position - 1]
    url = tag.get('href', None)
    i = i + 1
