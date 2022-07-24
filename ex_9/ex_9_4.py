fname = input('Enter file name: ')

try:
    fhandle = open(fname)
except:
    print('Invalid file name')
    quit()

address = list()
counts = dict()

for line in fhandle:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    address = words[1]
    counts[address] = counts.get(address, 0) + 1

bigsender = None
bigcount = None

for sender,count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigsender = sender

print(bigsender, bigcount)
