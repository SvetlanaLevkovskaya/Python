# 1 - вызывам функцию open() которая возвращает объект file
# 2 - вызываем метод read() или write() для объекта file
# 3 - закрываем файл методом close()
# R - режим чтения
# W - режим перезаписи
# A - режим добавления


# f = open("1.txt", "w")
# f.write("Hello file!!!")
# f = open("1.txt", "r")
# print(f.read())
# f.close()

# with open("1.txt", "w") as f:
#     f.write("sd,jg,sg,sdmg!!!")

# f = open("2.txt", "w")
# f.write("Hello file!!!")
# f.close()

# обработка исключений
try:
    a = int(input("a"))
    b = int(input("b"))
    print(a / b)
except ZeroDivisionError:
    print("It is not correct")
