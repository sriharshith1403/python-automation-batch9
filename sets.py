myset = {"apple", "banana", "cherry","apple",False,0,2}
mylist = ['a','b']
myset2 = ['c','d']
print(mylist)
empty_set =set()
empty_dict = {}
print(type(myset))
mylist.append(10)
mylist.remove(10)
myset.update(mylist)
count=len(myset)
print(myset|myset2) #union
print(myset&myset2)
for fruit in myset:
    print(fruit)