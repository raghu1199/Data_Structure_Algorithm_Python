def reverse_int(num):
    rem=0
    rev=0
    while num > 0:
        rem = num%10
        rev=rev*10+rem
        num=num//10

    return rev

print(reverse_int(4321))