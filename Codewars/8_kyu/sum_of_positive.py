def positive_sum(arr):
    return sum(a for a in arr if a > 0)


print(positive_sum([1,2,3,4,-5]))