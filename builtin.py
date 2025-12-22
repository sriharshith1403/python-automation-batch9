"""""
def buitin(x):
x=range(5)
for n in x:
    print(n)
#range starts from 0 to n-1


myList= ["a","b","c"]
x=len(myList) #length of the List
y=type(myList)#type of the list

#strp()  remove whitespaces from start and end of the string
txt="     banana     "
x=txt.strip() #returns "banana"
print(x)

#str 
y=str(3.5)
print(y)


#builtin module ---> math, random
import random
print(random.randint(1,10)) #random number between 1 to 10

#3rd party module --> requests, numpy, pandas, matplotlib
import requests
requests.get("http://www.google.com")
r.status_code
"""
