fhand = open('mbox-short.txt')

for l in fhand:
    line = l.rstrip()
    print(line.upper())
