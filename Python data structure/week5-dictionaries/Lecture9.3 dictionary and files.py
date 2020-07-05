# retreiving the key and values

jjj = {'chuck':1, 'fred':42, 'jan': 100}
print(jjj.keys())
print(jjj.values())
print(jjj.items())

# two iteration variables
for aaa,bbb in jjj.items(): # aaa is key here, and bbb is value, this will hit every pair of key and value in the dict
    print(aaa,bbb)

#chapter 1 notebook

stuff = dict()
print(stuff.get('candy',-1))