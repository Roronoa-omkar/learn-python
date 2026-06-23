#A number exactly two facts 1 and itself
def prime(n):
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            count = count + 1
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")

prime(2)

#other is the sqrt method 


            
