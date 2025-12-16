print("Get max , min, swap value of varibales")
print("\n 1. Max \n 2. Min \n 3.Swap")
a, b = map(int,input("Enter two numbers").split(","))

choice = int(input("enter your choice"))
if choice == 1:
    print(max(a,b))
elif choice == 2:
    print(min(a,b))
elif choice == 3:
    a,b=b,a
    print("after swapping %d %d"%(a,b))
else:
    print("invalid choice")