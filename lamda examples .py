from functools import reduce

x=lambda a: a + 10
print(x(5))

y=lambda a,b: a*b
print(y(5,6))

z=lambda a,b,c: a+b+c
print(z(5,6,2))


a=[1,2,3,4,5,6]
b=map(lambda x:x**2,a)
#it will create new list of b with 1,2,3,4,5
print(list(b))

#for reduce we have to use import reduce
#define the lambda it must accept 2 argument
#call reduce

from functools import reduce
 
numbers = [1, 2, 3, 4, 5]
 
# The lambda x, y: x * y multiplies the current accumulator (x) and the next item (y)

product_result = reduce(lambda x, y: x * y, numbers)
 
print(product_result)

# Output: 120 (calculated as ((((1*2)*3)*4)*5))

from functools import reduce
 
words = ["a", "for", "b"]
 
# The lambda x, y: x + " " + y concatenates strings with a space in between
concatenated_string = reduce(lambda x, y: x + " " + y, words)
 
print(concatenated_string)

 