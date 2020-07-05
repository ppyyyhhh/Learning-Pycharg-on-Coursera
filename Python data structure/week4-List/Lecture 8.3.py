#split
abc = 'with three words'
stuff = abc.split()
print(stuff)
print(len(stuff))
for w in stuff:
    print(w)

#Double split patter
line = "from stephenaoejggj@uct.ac.za Sat Jan 5 08:14:19 2020"
words = line.split()
email = words[1]
print(email)
pieces = email.split('@')
print(pieces)
host = pieces[1]
print('host=',host)

