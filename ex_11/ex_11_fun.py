import re
print( sum([ int(num) for num in re.findall('[0-9]+', open('regex_sum_1545365.txt').read() ) ] ) )
