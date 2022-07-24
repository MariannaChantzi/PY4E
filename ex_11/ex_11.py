fname = input('Enter file name:')

if len(fname) < 1:
    fname = 'regex_sum_1545365.txt'

import re

try:
    fhand = open(fname)
except:
    print('Invalid file name')
    quit()

sum = 0
count = 0

for line in fhand:
    line = line.rstrip()
    lst_num = re.findall('[0-9]+', line)
    for str_num in lst_num:
        sum = sum + int(str_num)
        count = count + 1

print('Total sum:',sum)
print('Total number of values:',count)
