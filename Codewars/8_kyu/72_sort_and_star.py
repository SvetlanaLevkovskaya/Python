"""You will be given a vector of strings. You must sort it alphabetically (case-sensitive,
and based on the ASCII values of the chars) and then return the first value.
The returned value must be a string, and have "***" between each of its letters.
You should not remove or add elements from/to the array."""


def two_sort(array):
    return "***".join(sorted(array)[0])


print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
print(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]))


def two_sort(lst):
    return '***'.join(min(lst))


print(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]))
print(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]))
