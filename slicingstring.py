myString = "abcdef ghijkl"
sub1 = myString[0:6]# slicing the first 7 elements
sub2 = myString[7:]#from the 7th element till end
sub3 = myString[:5]# first 6 elements
sun4 = myString[10]#the 10th element  - index from 0
sub5 = myString[-5]# last 5 elements

if "a " in myString:
    print("a is there ")

word=myString.split(" ")
print(word)
