person_string = '{"name":"Cansu", "langues": ["python", "C"]}'

person_dictionary ={
    "name" : "Cansu",
    "langues": ["python", "C"]
}
# result = person["name"]
# result = person["langues"]
# result = person["langues"][0]

import json

# person_string = '{"name":"Cansu", "langues": ["python", "C"]}'

# # json string to Dictionary
# person = json.loads(person_string)
# result0 =person["name"]
# result1 = person["langues"]
# result2 = person["langues"][0]

# print(result0)
# print(result1)
# print(result2)


# with open("person.json") as f:
#     data = json.load(f)
#     print(data["name"])

# person_string = json.dumps(person_dictionary)
# print(person_string)
# print(type(person_string))

# with open("person.json","w") as f:
#     json.dump (person_dictionary,f)

person_dictionary = json.loads(person_string)

result = json.dumps(person_dictionary, indent=4 , sort_keys=True )
print(result)