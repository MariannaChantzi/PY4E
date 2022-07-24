fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'

try:
    fhand = open(fname)
except:
    print('Invalid file name')
    quit()

count = dict()

for line in fhand:
    if not line.startswith('From '):
        continue
    words = line.split()
    time = words[5]
    time = time.split(':')
    hour = time[0]
    count[hour] = count.get(hour,0) + 1

for k,v in sorted(count.items()):
    print(k,v)
