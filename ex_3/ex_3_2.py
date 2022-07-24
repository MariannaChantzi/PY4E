hours = input("Enter Hours: ")
rate = input("Enter Hourly Rate: ")

try:
    h = float(hours)
    r = float(rate)
except:
    print("Please enter numeric input.")
    quit()

if h <= 40:
    pay = h * r
else:
    pay = h * r + (h-40) * 0.5 * r

print("Pay:",pay)
