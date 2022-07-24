largest = None
smallest = None

while True:
    num_str = input("Enter a number: ")
    if num_str == "done":
        break
    try:
        num = int(num_str)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = num
    elif num > largest:
        largest = num

    if smallest is None:
        smallest = num
    elif num < smallest:
        smallest = num

print("Maximum is",largest)
print("Minimum is",smallest)
