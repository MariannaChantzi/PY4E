fname = input("Enter file name: ")

if len(fname) < 1:
    fname = "mbox-short.txt"

fhand = open(fname)

count = 0

for l in fhand:
    if not l.startswith("From "):
        continue
    line = l.rstrip()
    words = line.split()
    print(words[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")
