file = open("owels.py", "w")   
file.write("Hello, this is a sample text.\nWelcome to Python file handling!")
file.close()


file = open("calculator.py", "r")  
content = file.read()
file.close()

print("File content:")
print(content)
