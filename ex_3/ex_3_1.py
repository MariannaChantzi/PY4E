hours = input("Enter Hours: ")
rate = input("Enter Hourly Rate: ")

h = float(hours)
r = float(rate)

if h <= 40:
    print("Regular")
    pay = h * r
else:
    print("Overtime")
    pay = h * r + (h-40) * 0.5 * r

print("Pay:",pay)
