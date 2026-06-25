#variable - usable container for any value (string,integer,float,boolean)
#           the variable behaves as if it the values that it contains 
full_name = "youtube"
age = 32
height = 4.5
is_student = False


print(full_name)
print(f"Hello {full_name}")
print(f"Your age is {age}")
print(f"Your height is {height}")


if is_student:
    print("You are a student")
else:
    print("You are not a student")


"""
#concept of Variables
a = 10 
b = a 

a = 20 
# print(a) 
# print(b) #cause int are immutable int, float,string,tuple 

#2 Swapping is possible 
a , b = b , a

"""
##Cocepts of ternary used in python 
"""
#instead of using if and else condition again n again 
#we can use ternary to make that in one line (shortcut of a small decision)

age = 45
if age>18 :
    {
        print("he is a senior")
    }
else:
    print("not senior")

result = "senior" if age >18 else not "senior" #Ternary
print(result) 

num = 5 
value = "Even" if num %2 == 0 else "odd"
print(value)

"""

# arithmetic = [+,-,*,/,//(returns integer) , % - remainder(remaining)]
friend = 5
friend %= 4 #Augmented assignment operator
#friend++ ( Error ❌)
print(friend)

#typecasting - the process converting a variable from one data type to another 
#               str(), int(), float(), bool() --> Functions
name  = ""
age = 24
gpa = 3.07
is_student = True
print(type(is_student)) #Type of data type

age = str(age) #type cast
age += "2"
print(age)

name = bool(name)
print(name)

"""
#input() 
name = input("Enter your name: ") #str data type
print(name)


age = int(input("Enter your age "))
age += 1 
print(f"Your are {age} old!")

"""

# if - else statement (Decision making statements) - agar/magar

# Logical operators - Evaluate multiple conditions 
# Or , and , not(inverts the condition not true , not False)

temp = 55
is_raining = False
if temp > 35 or temp < 0 or is_raining:
    print("No Outdoor")
else:
    print("Outdoor")

"""
#While Loop - used to repeat the condition as long as the condition is true
#             we recheck the condition at the end of the loop 

if 1 == 1:
    print("I am stuck in a loop")

name = input("Enter your name")

while name == "":
    name = input("Enter your name")

age = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be less than zero")
    age = int(input("Enter your age: "))

print(f"hello {name}") 
print(f"Your age is {age}")
#While loop is really good for input that is not valid and reprompt it 
"""

#For loop 

# for i in range(10):
#     print(i)

# for i in range(1,11):
#     print(i)

# for i in range(1,20,3):
#     print(i)

# name = "omkar kumar"
# for letter in name:
#     print(letter,end = " ")

# import time
# for i in range(10,0,-1):
#     print(i)
#     time.sleep(1)

# print("happy new year")

# list - mutable - change the elemennts 
# tuple - immutable 
# set{} - mutable , unordered , No duplicates , best for membership testing 

#Functions - Block of reusable code () - parenthesis after the fuction name 

def display_invoice(username, amount, due_date):
   print(f"Hello {username}")
   print(f"Your bill of ${amount:.2f} is due: {due_date}")

# display_invoice("BroCode", 42.50, "01/01")
# display_invoice("JoeSchmo", 100.01, "01/02")

#return is a statement that is used to end a function 
# and send a result back to the caller 

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

# full_name = create_name("spongebob", "squarepants")
# print(full_name)

##Dictionaries 

# dictionary =  a collection of {key:value} pairs
#                        ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
                    "India": "New Delhi",
                    "China": "Beijing",
                    "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("Japan"))

# if capitals.get("Russia"):
#    print("That capital exists")
# else:
#    print("That capital doesn't exist")

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detroit"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# keys = capitals.keys()
# for key in capitals.keys():
#   print(key)

# values = capitals.values()
# for value in capitals.values():
#     print(value)

# items = capitals.items()
# for key, value in capitals.items():
#    print(f"{key}: {value}")


"""
#Recursion - call itself again n again 
#Recursion is when a function calls itself again and again to solve a problem.

def countdown(n):
    if n == 0:          # base condition
        return
    print(n)
    countdown(n - 1)    # recursive call

countdown(5)
print()

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n-1)
    factorial(n-1)


print(factorial(5))

"""
