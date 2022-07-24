fhand = open('romeo.txt')

words = list()

for ln in fhand:
    line = ln.rstrip()
    for word in line.split():
        if word not in words:
            words.append(word)

words.sort()
print(words)
