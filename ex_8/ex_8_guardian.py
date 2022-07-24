han = open('mbox-short.txt')

for line in han:
    line = line.rstrip()
    wds = line.split()
    # guardian pattern in a compound statement. 3 is for more safety
    if len(wds) < 3 or wds[0] != 'From' : # short circuit guarantee
        continue
    print(wds[1])
