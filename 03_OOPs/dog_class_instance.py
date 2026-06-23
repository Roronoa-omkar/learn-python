class Dog:
    #Creating valuable data with python class
    def __init__(self,name,breed,owner):
        self.name = name #this name can be anything upto you
        self.breed = breed
        self.owner = owner
    #manual method
    def bark(self):
        print("Whoof Whoof")

class Owner:
    def __init__(self,name,address,contact_no):
        self.name = name
        self.address = address
        self.phone_number = contact_no


#manual object
owner1 = Owner("Omkar","Bokaro","999-998-23")

#Basically linked dog1 object data to the owner1 object data
dog1 = Dog("shiro","pug",owner1)

"""Reading the data(basically we create data attributes that our objects knows and stores) ->simple"""
# dog1.bark()
# print(dog1.name)
# print(dog1.breed)

#Now dog1 will have its own attribute(owner1) ot data field to access anytime
print(dog1.owner.address)


