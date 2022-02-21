"""Sum all the numbers of a given array ( cq. list ),
except the highest and the lowest element ( by value, not by index! ).
The highest or lowest element respectively is a single element at each edge,
even if there are more than one with the same value.
Mind the input validation."""


def sum_array(arr):
    return sum(sorted(arr)[1:-1]) if arr else 0


print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([6, 2]))
print(sum_array([6]))
