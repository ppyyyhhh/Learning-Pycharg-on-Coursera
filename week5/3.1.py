hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rates:")
r = float(rate)
if h > 40:
    h1 = h -40
    pay = 40 * r + h1 * 1.5 * r
else:
    pay = h * r
print(pay)