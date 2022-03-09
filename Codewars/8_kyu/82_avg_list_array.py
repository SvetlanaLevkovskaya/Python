"""Return the average of the given array rounded down to its nearest integer."""

def get_average(marks):
    return int(sum(marks) / len(marks))


print(get_average([1, 5, 87, 45, 8, 8]))


def get_average(marks):
    return sum(marks) // len(marks)


print(get_average([1, 5, 87, 45, 8, 8]))
