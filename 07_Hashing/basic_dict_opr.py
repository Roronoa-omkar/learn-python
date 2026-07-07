user_info = { "name": "Omkar", "age": 25, "logged_in": True}

#or you can also write dict in these ways 
calendar = dict(month= "july", year= 2028)

#or list of tuples
politics = [("bjp", "congress"), ("cockroach", 0)]
data = dict(politics)


#Reading - [], for safe way use .get()
# print(calendar['month'])
# print(user_info["logged_in"])
# print(data.get("aap", "N/A"))


#writing/adding 
user_info["title"] = "kumar"
# print(user_info)


# Updates 'logged_in' and adds 'city'
user_info.update({"city": "Bangalore", "logged_in": False}) 
# print(user_info)


#iterating 
# print(calendar.keys())
# print(calendar.values())
# print(calendar.items())


#To check if a key exist in it or not
# if "day" in calendar:
#     print(calendar["day"])
# else:
#     print("day not found")


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 4}

merged = dict1 | dict2
#dict 2 overrides dict 1
# print(merged)

