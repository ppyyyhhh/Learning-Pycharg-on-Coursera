fruit = 'banana'
print(len(fruit))

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

for letter in fruit:
    print(letter)

count = 0
for letter in fruit:
    if letter == 'a':
        count = count +1
print(count)

s = 'Monty Python'
print(s[0:4])

stuff = 'Hello world'
type(stuff)

dir(stuff)