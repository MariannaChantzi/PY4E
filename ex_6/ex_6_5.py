text = "X-DSPAM-Confidence:    0.8475"
space_pos = text.find(' ')
num_str = text[space_pos+1:]
num = float(num_str)
print(num)
