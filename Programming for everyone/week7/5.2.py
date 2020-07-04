largest = None
smallest = None
while True:
    num = input("Enter a number:")
    if num == "done":
        break
    try:
        flvt = int(num)
    except:
        print("Invalid input")
        continue
    if largest is None:
        largest = flvt
    if smallest is None:
        smallest = flvt
    if largest < flvt:
        largest = flvt
    if smallest > flvt:
        smallest = flvt
print("Maximum is", largest)
print("Minimum is", smallest)