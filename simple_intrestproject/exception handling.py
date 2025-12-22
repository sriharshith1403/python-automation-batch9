try:
    num= int(input("enter a number :"))
    result=10/num

except ZeroDivisionError:
    print("the divisor cannot be zero")

except ValueError:
    print("the divisor is non numeric")

finally:
    print("everything done ")

print("result is :{result}")
    
#where ever we input from the user we have to write the exception handling code
