#tuples are immutable, can not be altered once created.
#Lists are mutable, but strings and tuples cant
x = [9,8,7] # create a tuples by []


#tuple assignment
(x,y) = (4,'fred')
print(y)
(a,b) =(99,98)
print(a)

#comparing tuples
(0,1,2) < (5,1,2) #comparing one by one, the former pair is more significant

#sorting
d = {'a':10, 'b':1, 'c':22}
t = sorted(d.items())
for k,v in sorted(d.items()):
    print(k,v)
c = list()
for k,v in sorted(d.items()):
    c.append((v,k))#v is ahead, for the sorting by values later. also(v,k)is a tuple, nesting with in ()
print(sorted(c,reverse=True))

#shorter verison of the sorting by value, and top x
print(sorted([(v,k) for k,v in d.items()],reverse=True))

x , y = 3, 4
print(y)