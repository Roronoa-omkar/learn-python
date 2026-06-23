# Python gives you 4 main ways to store multiple things:

# List → like a shopping list
# Tuple → like a fixed list (cannot change)
# Set → like a bag with no duplicates
# Dictionary → like a real dictionary (word → meaning)

# print("##List##")
# state = ["mumbai" , "delhi" , "bihar"]

"""
# print(state) #Printing entire list obj

#List are mutable --> we can change the list
# state[0] = "Raipur"
# print(state)

#List Slicing Possible --> lsit_name[starting_idx:ending_idx]
# print(state[:2])

#Methods are available in List
# list = [24,6,7,1]
# list.append(88)
# print(list)

Examples --> sort(), list.index(idx,el) - insert element at idx
"""

# for i in range(len(state)):  #Each element one by one
#     print(state[i]) 

# state = ["mumbai" , "delhi" , "bihar"]
# for i,v in enumerate(state):
#     print("Index:" , i , "value:" , v)

# state = ["mumbai" , "delhi" , "bihar"]
# for i in range(len(state)):
#     print("Index:", i, "Value:", state[i])



# print("##Tuple##")

# cars = ("merc","bmw","nissan")
# for car in cars:
#     print(car)

# fruits = ("apple","orange","strawberry")
# for i in range(len(fruits)):
#     print(i, fruits[i])

# for index, value in enumerate(fruits):
#     print(index,value)




# print("##Sets##")

# colors = {"red","green","yellow"} ## no fixed indexing
# for i in range(len(colors)):
#     print(colors)

# for index, value in  enumerate(colors):
#     print(index,value)

#sets are mutable but set's elements are immutable 
#hashing is a specific algo were orginal value ko change kr k kisi aur cheej mai kr dete hai

 # methods in sets
# collection = {"hello","omkar","shruti","cricket","market"}
# print(collection.pop())


#Dictionary

#nested dictionary 
# info = {
#     "name":"omkar",
#     "subjects": 
#         {
#             "phy" : 45,
#             "chem" : 56,
#             "maths" : 44
#         }
#     }

# print(len(info))

# #methods of dict similarly there are other methods like 
# print(len(list(info.keys()))) 
# #values(),items(),get(),update()

