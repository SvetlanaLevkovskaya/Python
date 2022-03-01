"""Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially
applying the operator to the values in the array.

True AND True -> True
True AND False -> False

True OR True -> True
True OR False -> True

True XOR True -> False
False XOR False -> False
"""


def logical_calc(array, op):
    true_count = 0
    if op == "AND":
        if False in array:
            return False
        return True
    if op == "OR":
        if True in array:
            return True
        return False
    # Basically if there is an odd number of True's (1's) the output will always be True
    if op == "XOR":
        for bol in array:
            if bol == True:
                true_count += 1
        if true_count % 2 != 0:
            return True
        return False


print(logical_calc([True, True, False], "AND"))
print(logical_calc([True, True, False], "OR"))
print(logical_calc([True, True, False], "XOR"))

print(logical_calc([True, False], "AND"))
print(logical_calc([True, False], "OR"))
print(logical_calc([True, False], "XOR"))
