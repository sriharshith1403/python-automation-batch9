import json

a={"name": "harshith", "age": 22}

#key <> value
#json -> java Script object notation
#test.docx
#data.json

b=json.dumps(a)

# {"age": 32, "name": "jhon"}

with open('data.json', 'r') as file:
    data=json.load(file)
print(json.dumps(data,indent=2)) #space between the object is 4
#it should in same file location