"""Write a function that checks if a given string (case insensitive) is a palindrome."""


def is_palindrome(s):
    return s.lower() == s.lower()[::-1]


print(is_palindrome('TZVHdbbatxHDryKKYRDhxTABbDHVzT'))
print(is_palindrome('Abba'))


def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


print(is_palindrome('TZVHdbbatxHDryKKYRDhxTABbDHVzT'))
print(is_palindrome('Abba'))
