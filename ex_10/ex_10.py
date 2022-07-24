fname = input('Enter file name: ')
if len(fname) < 1:
    fname = 'clown.txt'

try:
    fhand = open(fname)
except:
    print('Invalid file name')
    quit()

di = { }

for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word,0) + 1

lst = [ ]

for k, v in di.items():
    lst.append((v,k))

lst = sorted(lst, reverse=True)

for v, k in lst[:5]:
    print(k,v)
