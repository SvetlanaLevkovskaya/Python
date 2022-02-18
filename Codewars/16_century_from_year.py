def century(year):
    if year % 100 == 0:
        return year // 100
    return year // 100 + 1


print(century(1705))   # 18, 'Testing for year 1705
print(century(1900))   # 19, 'Testing for year 1900
print(century(1601))   # 17, 'Testing for year 1601
print(century(2000))   # 20, 'Testing for year 2000
print(century(356))    # 4, 'Testing for year 356
print(century(89))     # 1, 'Testing for year 89


def century(year):
    return (year + 99) // 100


import math

def century(year):
    return math.ceil(year / 100)


# print "math.floor(-23.11) : ", math.floor(-23.11)     # 24
# print "math.floor(300.16) : ", math.floor(300.16)     # 300
# print "math.floor(300.72) : ", math.floor(300.72)     # 300
#
# print "math.ceil(-23.11) : ", math.ceil(-23.11)       # 23
# print "math.ceil(300.16) : ", math.ceil(300.16)       # 301
# print "math.ceil(300.72) : ", math.ceil(300.72)       # 301