captials =  {"USA": "Washington, D.C.", "France": "Paris", "Japan": "Tokyo"}
print(captials["France"])
print(captials.get("Germany"))
print (captials.keys())
print(captials.values())
print(captials.items())



captials.update({"Germany": "Berlin"})
captials.update({"USA": "Las Vegas"})
captials.pop("Japan")

for key, value in captials.items():
    print(key,value)