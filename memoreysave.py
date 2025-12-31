def large_num(n):
    for i in range(n):
        yield i
# this doesnt create a large list in memory
gen = large_num(10)
print(next(gen))
print(next(gen))

#basic list comprehension it will store in them memory
list = [x*x for x in range(5)]
print(list)

#doing comprehension using generators it will not store in memory
gen = (x*x for x in range(5))
print(gen)