students = [100 , 90, 80, 70, 60,50,40,30,0]
pass_students = [i if i>60 else 'Failed' for i in students] 
print(pass_students)