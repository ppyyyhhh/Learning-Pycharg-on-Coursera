# add list
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print('c=', c)
print('a=', a)

# slicing a list
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
print(t[1:3])
print(t[:5])
print(t[3:])
print(t[:])

# add things by append

stuff = list()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')
print(stuff)
# sorting
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
# enter number and output average

print("enter numbers to get the mean, type done after finished")
numlist = list()
while True:
    inp = input("Enter a number: ")#igjkojiugiojkhgyuyoupikjiuogtyu90-piuoiuiouhuilhp[
    if inp == 'done' : break
    try:
        value = float(inp)
    except:
        print("invalid number")
        continue
    numlist.append(value)

print(numlist)
mean = sum(numlist) / len(numlist)
print('The average is :', mean)
