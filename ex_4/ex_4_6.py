def computepay(hours,rate):
    # print("In function computepay()",hours,rate)
    if hours > 40:
        # print("Overtime")
        reg = hours * rate
        ovt = (hours - 40) * rate * 0.5
        pay = reg + ovt
    else:
        # print("Regular")
        pay = hours * rate
    # print("Returning", pay)
    return pay

hours = input("Enter Hours: ")
rate = input("Enter Hourly Rate: ")

try:
    h = float(hours)
    r = float(rate)
except:
    print("Please enter numeric input.")
    quit()

p = computepay(h,r)

print("Pay:",p)
