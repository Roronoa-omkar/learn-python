#Stack overflow 
# def cause_overflow():
#     print("Calling myself...")
#     cause_overflow()  # The function calls itself over and over

#Trigger the infinite loop of function calls
# cause_overflow()

#Defining a stop condition in recursion 
def overflow(count):
    
    if count == 3:
        return
    print(count)
    overflow(count + 1)

overflow(0)
 