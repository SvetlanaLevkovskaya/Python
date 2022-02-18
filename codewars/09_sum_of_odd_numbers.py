def sum_odd_numbers(n):
    return n**3

'''
             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29 '''


def row_sum_odd_numbers(n):
    return sum(range(n*(n-1)+1, n*(n+1), 2))