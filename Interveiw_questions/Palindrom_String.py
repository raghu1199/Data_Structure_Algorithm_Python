
def is_palindrom(str):
    original_str=str
    reversed_str=str[::-1]

    if original_str == reversed_str:
        return True
    else:
        return False

print(is_palindrom("radar"))
print(is_palindrom("radart"))
str ="abcdefg"
print(str[::-1])