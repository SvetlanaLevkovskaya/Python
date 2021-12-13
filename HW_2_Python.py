# Arithmetic
#
#  1. Создать переменную item_1 типа integer.
#  2. Создать переменную item_2 типа integer.
#  3. Создать переменную result_sum в которой вы суммируете item_1 и item_2.
#  4. Вывести result_sum в консоль.
import math
import random

item_1 = 55
item_2 = 45
result_sum = item_1 + item_2
print(result_sum)

#  5. Создать переменную result_subtr в которой вы вычитаете большую по значению переменную из меньшей по значению.
#  6. Вывести result_subtr в консоль.
result_subtr = item_2 - item_1
print(result_subtr)

#  7. Создать переменную result_multi в которой вы умножаете item_1 на item_2.
#  8. Вывести result_multi в консоль.
result_multi = item_1 * item_2
print('result_multi = ', result_multi)

#  9. Создать переменную result_exp в которой вы item_1 возводите в степень item_2.
#  10. Вывести result_exp в консоль.
result_exp = item_1 ** item_2
print('result_exp = ', result_exp)

#  11. Создать переменную result_m_exp в которой вы item_1 возводите в степень item_2 используя библиотеку math.
#  12. Вывести result_m_exp в консоль.
result_m_exp = pow(item_1, item_2)
print('result_m_exp = ', result_exp)

#  13. Создать переменную result_s_root в которой вы найдёте квадратный корень любой из переменной item
#  14. Вывести result_s_root в консоль.
result_s_root = item_1 ** 0.5
print('result_s_root = ', result_s_root)

#  15. Создать переменную result_m_s_root в которой вы найдёте квадратный корень любой из переменной item
#  используя библиотеку math.
#  16. Вывести result_m_s_root в консоль.
result_m_s_root = math.sqrt(item_1)
print('result_m_s_root = ', result_m_s_root)

#  17. Создать переменную result_mp_s_root в которой вы найдёте квадратный корень любой из переменной item
#  используя библиотеку math используя метод pow.
#  18. Вывести result_mp_s_root в консоль.
result_mp_s_root = math.isqrt(item_1)
print('result_mp_s_root = ', result_mp_s_root)


#  19. Присвоить переменной item_1 odd значение
#  20. Присвоить переменной item_2 even значение
#  21. Создать переменную result_division в которой вы разделите item_1 на item_2.
#  22. Вывести result_division в консоль.
# Even number examples: 2, 4, 6, 8, 10, etc.
# Odd number examples:1, 3, 5, 7, 9 etc.
item_1 = 55
item_2 = 44
result_division = item_1 / item_2
print('result_division = ', result_division)


#  23. Создать переменную result_m_floor и result_division округлить до ближайшего целого меньшего чем result_division.
#  24. Вывести result_m_floor в консоль.
result_m_floor = math.floor(10.8)
result_division = item_1 / item_2
print('result_m_floor = ', result_m_floor)


#  25. Создать переменную result_m_ceil и result_division округлить до ближайшего целого большего чем result_division.
#  26. Вывести result_m_ceil в консоль.
result_m_ceil = math.ceil(10.8)
print('result_m_ceil = ', result_m_ceil)


#  27. Создать переменную result_int и result_division округлить до ближайшего целого через явное приведение.
#  28. Вывести result_int в консоль.
result_int = round(10.91)
result_int_1 = round(10.11)
print('result_int = ', result_int)
print('result_int_1 = ', result_int_1)

#  29. Создать переменную result_no_division_loss в которой вы разделите item_1 на item_2 без остатка.
#  30. Вывести result_no_division_loss в консоль.
item_3 = 11
item_4 = 5
result_no_division_loss = math.floor(item_3 / item_4)
print('result_no_division_loss = ', result_no_division_loss)


#  31. Создать переменную result_division_loss в которой вы найдёте остаток от деления item_1 на item_2.
#  32. Вывести result_division_loss в консоль.
item_5 = 11
item_6 = 5
result_division_loss = item_3 % item_4
print('result_division_loss = ', result_division_loss)


# Дальше будет реализация через арифметические действия с присваиванием.
#  33. Создать переменную item_3 и присвоить ей целое число
item3 = int(3)

#  34. Прибавить 10 к item_3 с присвоением.
item3 += 10

#  35. Вывести item_3 в консоль.
print('item3 - 3+10 =', item3)

#  36. Отнять 5 от item_3 с присвоением.
#  37. Вывести item_3 в консоль.
item3 -= 5
print('item3 - 3+10 - 5 =', item3)

#  38. Умножить item_3 на 3 с присвоением.
#  39. Вывести item_3 в консоль.
item3 *= 3
print('item3 - (3+10-5) * 3 =', item3)

#  40. Разделить item_3 на 2 с присвоением.
#  41. Вывести item_3 в консоль.
item3 /= 2
print('item3 - (3+10-5)*3 / 2 =', item3)

#  42. Возвести в степень 2 item_3 с присвоением.
#  43. Вывести item_3 в консоль.
item3 **= 2
print('item3 - ((3+10-5)*3/2)**2 =', item3)

#  44. Найти квадратный корень item_3 с присвоением.
#  45. Вывести item_3 в консоль.
item3 **= 0.5
print('item3 - (((3+10-5)*3/2)**2) **(0.5) =', item3)

#  46. Присвоить остаток от деления item_3
#  47. Вывести item_3 в консоль.
item3 %= item3
print('item3 - 3 % 3 =', item3)

# Boolean
#  48. Создать переменную b_item_t и присвоить True
b_item_t = True

#  49. Создать переменную b_item_f и присвоить False
b_item_f = False

#  50. Создать переменную b_item_relult_sum и присвоить сумму b_item_t и b_item_f
b_item_relult_sum = b_item_t + b_item_f

#  51. Вывести b_item_relult_sum в консоль.
print('b_item_relult_sum =', b_item_relult_sum)

#  52. Создать переменную b_item_relult_subtr и присвоить разницу b_item_t и b_item_f
#  53. Вывести b_item_relult_subtr в консоль.
b_item_relult_subtr = b_item_t - b_item_f
print('b_item_relult_subtr =', b_item_relult_subtr)

#  54. Создать переменную b_item_relult_multi и присвоить умножение b_item_t и b_item_f
#  55. Вывести b_item_relult_multi в консоль.
b_item_relult_multi = b_item_t * b_item_f
print('b_item_relult_multi  =', b_item_relult_multi)

#  56. Создать переменную b_item_relult_division и присвоить деление b_item_t и b_item_f
#  57. Вывести b_item_relult_division в консоль. (Получить ошибку)
# b_item_relult_division  = b_item_t / b_item_f
# print('b_item_relult_division  =', b_item_relult_division)

#  58. Создать переменную b_item_1_int и присвоить явное приведение b_item_t к int
#  59. Вывести b_item_1_int в консоль.
b_item_1_int = int(b_item_t)
print('b_item_1_int  =', b_item_1_int, type(b_item_1_int))

#  60. Создать переменную b_item_2_int и присвоить явное приведение b_item_f к int
#  61. Вывести b_item_2_int в консоль.
b_item_2_int = int(b_item_f)
print('b_item_2_int  =', b_item_2_int, type(b_item_2_int))

# 7) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) 30"
# digit = input()
# int_digit = int(digit)
# if int_digit == 30:
#     print('Вы вели число = ', int_digit, 'которое равно 30')
# elif int_digit > 30:
#     print('Вы вели число = ', int_digit, 'которое больше 30')
# else:
#     print('Вы вели число = ', int_digit, 'которое меньше 30')

# 8) Сделать скрипт используя функцию input().
#     1. Функция должна на вход принимать целое число.
#     2. Внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100))
#     3. Выводить должна "Вы вели число = (введённое число) которое (меньше/больше/равно) сгенерированному числу"

# num = int(input('Введи число: '))
# i = random.randint(1, 100)
# print(i, type(i))
# if num < i:
#     print('Вы вели число = ', num, 'которое меньше сгенерированному числу')
# elif num > i:
#     print('Вы вели число = ', num, 'которое больше сгенерированному числу')
# else:
#     print('Вы вели число = ', num, 'которое равно сгенерированному числу')

# 9) Сделать скрипт используя функцию input().
# 1. Функция должна на вход принимать целое число.
# 2. Внутри функции должно сгенерироваться рандомное 2 целых числа( import random)...(random.randint(1, 100))
# 3. Выводить должна
# "Вы вели число = (введённое число) которое (меньше/больше/равно и меньше/больше/равно) сгенерированному числу"

num_1 = int(input('Введи число: '))
i_1 = random.randint(1, 100)
i_2 = random.randint(1, 100)
print(i_1, i_2)
if num_1 < i_1 and num_1 > i_2:
    print('Вы ввели число = ', num_1, 'которое меньше сгенерированного числа', i_1, 'и больше сгенерированного числа', i_2)
elif num_1 > i_1 and num_1 < i_2:
    print('Вы ввели число = ', num_1, 'которое больше сгенерированного числа', i_1, 'и меньше сгенерированного числа', i_2)
elif num_1 > i_1 and num_1 > i_2:
    print('Вы ввели число = ', num_1, 'которое больше сгенерированного числа', i_1, 'и больше сгенерированного числа', i_2)
elif num_1 < i_1 and num_1 < i_2:
    print('Вы ввели число = ', num_1, 'которое меньше сгенерированного числа', i_1, 'и меньше сгенерированного числа', i_2)
elif num_1 == i_1 and num_1 < i_2:
    print('Вы ввели число = ', num_1, 'которое равно сгенерированного числа', i_1, 'и меньше сгенерированного числа', i_2)
elif num_1 > i_1 and num_1 == i_2:
    print('Вы ввели число = ', num_1, 'которое больше сгенерированного числа', i_1, 'и равно сгенерированного числа', i_2)
else:
    print('Вы ввели число = ', num_1, 'которое не удовлетворяет условиям')


