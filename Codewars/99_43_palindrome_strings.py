def is_palindrome(string):
    return str(string) == str(string)[::-1]


print(is_palindrome('anna'))
print(is_palindrome(123321))
