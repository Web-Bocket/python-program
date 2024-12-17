# info = {
#     "name" : "rahul",
#     "learning": "coding",
#     "age" : 23,
#     "carrier" : "good"
# }

# print(info)
# print(type(info))
# print(info["name"])
# print(info["age"])

# nested dictionary example ->>>>>>>>>>>>>>>>>>>>>>

# student = {
#     "name": "rahul kumar",
#     "subject": {
#         "java" : {
#             "core-java": 89,
#             "adv-java": 90
#         },
#         "c++": 67,
#         "python": 99
#     }
# }
# print(student)
# print(student["name"])
# print(student["subject"]["java"]["core-java"])
# print(student["subject"]["python"])

# dictionary methods example. 

student = {
    "name": "rahul kumar",
    "subject": {
        "java" : 78,
        "c++": 67,
        "python": 99
    }
}

# print(student)
# print(student.keys()) 
# print(student["subject"].keys()) #['java', 'c++', 'python']
# print(student.values())
# print(student["subject"].values()) #[78, 67, 99]
# print(student.items()) # it can return a tuple of key:value pair
# print(student.get("subject"))
# print(student["subject"].get("python"))
student.update({"name": "ritesh"})
print(student)