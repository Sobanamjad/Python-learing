# info = {
#     "name": "Soban",
#     "subjects": ["Python","Java","NextJS"],
#     "topics": ("Dictionary","Set"),
#     "age": 23,
#     "is_adult": True,
#     "marks": 87
# }
# info["name"] = "Ahmad"
# # Add new key value in Dictionary
# info["surname"] = "Anwar"
# print(info)
# print(type(info))

# Nested Dictionary 
student = {
    "name" : "Zaman",
    "subjects" : {
        "phy" : 97,
        "math" : 89,
        "chem" : 91,
    }
}
print(student["subjects"]["chem"])
# .keys() function just print keys 
print(student.keys())
#  print list values in dictionary
print(list(student.keys()))
# lenght of dictionary
print(len(student))
# .values funtion print all values of dictionary
print(student.values())
# .items() function print tuples
print(student.items())
# Pairs 
pairs = list(student.items()) 
print (pairs[0])

# Two methods to get value of key
print(student["name"]) #if key wrong  like name2 then its print error 
print(student.get("name")) #if key wrong  like name2 then its print null value 

# Update method 
new_dict = {"city" : "Karachi", "name" : "Soban"}
student.update(new_dict)
print(student)
