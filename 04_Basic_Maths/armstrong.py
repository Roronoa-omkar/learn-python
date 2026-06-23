#armstrong number 
def armstrong(n):
    sum = 0 
    dup = n
    while(n>0):
        last_digit = n % 10
        sum = sum + (last_digit * last_digit * last_digit)
        print(sum)
        n //= 10
    return sum == dup


print(armstrong(153))


        
