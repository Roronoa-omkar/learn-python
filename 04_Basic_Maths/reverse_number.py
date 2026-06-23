def reverse_digit(n):
    rev_no = 0
    while(n>0):
        last_digit = n % 10
        n //= 10
        rev_no = (rev_no * 10) + last_digit
    return rev_no

print(reverse_digit(7789))
