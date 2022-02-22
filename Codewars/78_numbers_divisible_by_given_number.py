"""Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor.
First argument is an array of numbers and the second is the divisor."""


def divisible_by(numbers, divisor):
    return [x for x in numbers if x % divisor == 0]


print(divisible_by([0,1,2,3,4,5,6,7,8,9,10], 2))
