def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[0:2])


print(sum_two_smallest_numbers([7, 15, 12, 18, 22]))

a = [7, 15, 12, 18, 22]
print(sorted(a))
print(sum(sorted(a)[0:2]))
