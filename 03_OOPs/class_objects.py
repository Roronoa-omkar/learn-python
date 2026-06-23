#Everything You create in Python is an object
#These are examples of buil-in classes in python using that we are able to use different 
#data structures like str,int etc
name = "omkar"
age = 23
#str obj , and obj are made from classes
(type(name.upper())) 
#different obj has different functions/methods to modify the data
(name.upper()) 


#Now will learn to create our own classes and our own objects called as instances
#method is basically a function contained withing a CLASS
class Dog:
    #method
    def bark(self):
        print("Whoof Whoof")

#created a dog object and assigning to a dog variable(anything you want) and calling it anytime
dog1 =  Dog()

#Now we can access the method created in the class similar to str,int method we use in python but manually
#Problem with this is it is not very helpful
dog1.bark()