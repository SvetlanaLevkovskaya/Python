# errors and exceptions (SyntaxError, TypeError, ModuleNotFoundError, NameError, FileNotFoundError, ValueError,
#                        IndexError, KeyError)

x = 5
if x < 0:
    raise Exception('x should be positive')

x = 5
assert x >= 0, 'x is not positive'

print('-' * 80)
try:
    a = 5 / 0
except:
    print('an error happened')

print('-' * 80)
try:
    a = 5 / 0
except Exception as e:
    print(e)

print('-' * 80)
try:
    a = 5 / 1
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

print('-' * 80)
try:
    a = 5 / 0
    b = a + '10'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

print('-' * 80)
try:
    a = 5 / 1
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')

print('-' * 80)
try:
    a = 5 / 0
    b = a + 10
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print('everything is fine')
finally:
    print('cleaning up...')

print('-' * 80)


# class ValueTooHighError(Exception):
#     pass
#
# def test_value(x):
#     if x > 100:
#         raise ValueTooHighError('value is too high')
#
# test_value(200)





