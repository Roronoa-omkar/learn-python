def palindrome(n):
    dup = n
    rev_num = 0
    while(n>0):
        last_digit = n % 10
        n //= 10
        rev_num = (rev_num * 10) + last_digit
    if rev_num == dup:
        print("True")
    else:
        print("False")
    
    return rev_num



number = int(input("Enter the value "))
print(palindrome(number))
