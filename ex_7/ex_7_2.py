fname = input('Enter file name: ')

try:
    fhand = open(fname)
except:
    print("Invalid file name")
    quit()

count = 0
total = 0

for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    print(line)
    count = count + 1
    spc_pos = line.find(' ')
    num_str = line[spc_pos+1:]
    num_flt = float(num_str)
    total = total + num_flt

print("Done")
print("Average spam confidence:", total/count)
