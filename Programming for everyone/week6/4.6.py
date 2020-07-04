hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rates:")
r = float(rate)
def computepay(a,b):
    if a > 40:
        a1 = a -40
        pay = 40 * b + a1 * 1.5 * b
    else:
        pay = a * b
    return pay
p = computepay(h,r)
print("Pay", p)