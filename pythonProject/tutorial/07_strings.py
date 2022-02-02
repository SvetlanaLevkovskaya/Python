# разбиваем список на строчку
list = ["a", "b", "c"]
print(",".join(list))
print("".join(list))

# метод strip удаление пробелов в начале и в конце
text = "    sjdhg lxkdjglk lskdjglk djgkjdf     "
print(text.strip())
print('split = ', text.split(" "))
text0 = "    sjdhg-lxkdjglk-lskdjglk-djgkjdf     "
print('split0 = ', text.split("_"))

# метод lstrip удаление пробелов в начале строки
print(text.lstrip())

# метод rstrip удаление пробелов в конце строки
print(text.rstrip())

# метод replace
text1 = "olololololololo"
print(text1.replace("l", "o")) # заменяет букву l на букву o

# тройные ковычки
print("""xlkjvk
xlkjlxk
xlkjlxk
xlkjk
""")


# новая строка с использование управляющего символа
print("Hello\nHello\nHello")

# применение табуляции (4 отступа)
print("Hello\tHello\tHello")

#
print('"Hello\tHello\tHello"')
print("'Hello\tHello\tHello'")
print("'Hello \"Hello\" Hello'")

# конкотинация
a = "hello"
b = "Hello_1"
print(a + ' ' + b)
print(a*5)

# списки - итерируемые объекты
print(a[0])
print(a[0:3])
print(a[-1])
print(a.upper())
print(a.lower())
print(a.capitalize())



