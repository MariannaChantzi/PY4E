total = 0
count = 0

while True:
    num_str = input("Enter a number: ")
    if num_str == "done":
        break
    try:
        num = int(num_str)
    except:
        print("Invalid input")
        continue
    total = total + num
    count = count  + 1

print("Total:",total)
print("Count:",count)
print("Average:",total/count)
