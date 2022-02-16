import csv
import random
import names
import datetime


'''Вариант 1: Генерировать данные на лету, не создавая предварительных списков.
Вариант 2: Генерировать предварительные списки с данными, итерируя которые 
вы будите записывать данные в создаваемый файл.'''


'''Создать пустой empty.csv файл.'''
file = 'empty.csv'
with open(file, 'w', newline='') as f:
    writer = csv.writer(f)


'''Вариант 1. Создать digits.csv файл с 1-м полем, в котором будут 150 строк с числами от 0 до 150'''
file_2 = 'HW_6_digits.csv'
with open(file_2, 'w', newline='') as f:
    writer = csv.writer(f)
    row = range(0, 150)
    for i in row:
        writer.writerow([i])


'''Вариант 1. Создать names.csv файл с 1-м полем, в котором будут 100 строк с разными именами'''
file_3 = 'HW_6_names.csv'
with open(file_3, 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(100):
        writer.writerow([names.get_first_name()])


'''Вариант 1. Создать emals.csv файл с 1-м полем, в котором будут 100 строк с разными имейлами что-то@gmail.com'''
file_4 = 'HW_6_emails.csv'
with open(file_4, 'w', newline='') as f:
    writer = csv.writer(f)
    for i in range(100):
        name = (names.get_last_name()).lower()
        email = [name + '@gmail.com']
        writer.writerow(email)


'''Вариант 1. Создать nne.csv файл с 3-мя полями(Number, Name, Email ), в котором будут 100 строк. 
Имя и часть email до @ должны совпадать.'''
file_5 = 'HW_6_nne.csv'
with open(file_5, 'w', newline='') as f:
    writer = csv.writer(f)
    count = 0
    for i in range(100):
        count += 1
        name = names.get_first_name()
        email = count, name, (name+"@gmail.com").lower()
        writer.writerow(email)


'''Вариант 2. Создать digits_2.csv файл с 1-м полем которое называется number, 
в котором будут 300 строк с числами от 10 до 310'''
digits_ll = []
for i in range(0, 500):
    digits_ll.append([i])


def digits_2(file_name, digits):
    with open(file_name, 'w', newline='') as f:
        header = ["number"]
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(digits)


digits_2(file_name='HW_6_digits_2.csv', digits=digits_ll[10:350])


'''Вариант 2. Создать names_2.csv файл с 1-м полем которое называется name, 
в котором будут 400 строк с разными именами'''
names_ll = []
for i in range(500):
    names_ll.append([names.get_first_name()])


def names_2(file_name, names):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(names)


names_2(file_name='HW_6_names_2.csv', names=names_ll[:400])


'''Вариант 2. Создать emals_2.csv файл с 1-м полем которое называется email, 
в котором будут 400 строк с разными имейлами что-то@gmail.com'''
email_ll = []
for i in range(500):
    name = names.get_last_name()
    email = (name + '@.gmail.com').lower()
    email_ll.append([email])


def emails_2(file_name, emails):
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(emails)


emails_2(file_name='HW_6_emails_2.csv', emails=email_ll[:400])


'''Вариант 2. Создать nne_2.csv файл с 3-мя полями(Number, Name, Email ), 
в котором будут 450 строк. Имя и часть email до @ должны совпадать.'''
nne_ll = []
count = 0
for i in range(500):
    count += 1
    rand_name = names.get_full_name()
    email = (rand_name.replace(" ", "_")).lower() + "@gmail.com"
    nne_ll.append({"Number": count, "Name": rand_name, "Email": email})


def nne_2(file_name, nne_dict):
    with open(file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Number', 'Name', 'Email'])
        writer.writeheader()
        writer.writerows(nne_dict)


nne_2(file_name='HW_6_nne_2.csv', nne_dict=nne_ll[:450])


# file_9 = 'HW_6_nne_2.csv'
# with open(file_9, 'w', newline='') as f:
#     header = ["Number", "Name", "Email"]
#     writer = csv.writer(f)
#     writer.writerow(header)
#     count = 0
#     for i in range(100):
#         count += 1
#         name = names.get_first_name()
#         email = count, name, (name+"@gmail.com").lower()
#         writer.writerow(email)


''' Добавить в файл nne_2.csv столбец Date и заполнить каждую строку текущей датой и временем. 
Поле даты заполнить следующим образом:
a) Первые 50 строк даты по годам от 1980 - 1990 (распределить рандомно)
b) Следующие 100 строк даты по годам от 1991 - 2000 (распределить рандомно)
с) Следующие 150 строк даты по годам от 2001 - 2010 (распределить рандомно)
в) Следующие 150 строк даты по годам от 2011 - 2021 (распределить рандомно)'''


def update_nne(file_name):
    with open(file_name, 'r', newline='') as f:
        ff = []
        reader = csv.DictReader(f, fieldnames=['Number', 'Name', 'Email'])
        for i in reader:
            ff.append(i)
        print(*ff[0])

    with open (file_name, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[*ff[0], "Date"])
        writer.writeheader()
        offset = 1
        for k in range(offset, len(ff)):
            d = datetime.datetime.now()
            date = d - datetime.timedelta(microseconds=d.microsecond)
            if k < 50 + offset:
                ff[k]["Date"] = date.replace(year=random.randint(1980, 1990))
            elif k < 150 + offset:
                ff[k]["Date"] = date.replace(year=random.randint(1991, 2000))
            elif k < 300 + offset:
                ff[k]["Date"] = date.replace(year=random.randint(2001, 2010))
            else:
                ff[k]["Date"] = date.replace(year=random.randint(2011, 2021))
            writer.writerow(ff[k])


update_nne(file_name='HW_6_nne_2.csv')


'''Создать файл combo.csv с полями Name, Emaill, Date. 1000 строк.
a) Соберите имена из файла nne_2.csv.
b) недостающие 550 строк имён сгенерируйте.
с) Имена расположите в алфавитном порядке.
d) Для имён из файла nne_2.csv забрать даты из nne_2.csv которые были с этими именами в nne_2.csv.
e) Остальные даты генерировать рандомно.
f) Добавить и заполнить (можно рандомно) столбы Email, Phone, Gender, Salary.'''

names_lll = []
for i in range(1000):
    names_lll.append([names.get_first_name()])
# print(names_lll[450:])


def create_combo(nne_file_name, combo_file_name, names_list):
    with open(nne_file_name, "r", newline='') as f:
        ff = []
        reader = csv.DictReader(f, fieldnames=["Number", "Name", "Email", "Date"])
        for i in reader:
            ff.append([i["Name"], i["Date"]])
        ff = ff + names_list
        sorted_data = sorted(ff[1:])
    #print(len(sorted_data)[1])
    with open(combo_file_name, "w", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Email", "Date", "Phone", "Gender", "Salary"])
        writer.writeheader()
        gender_list = ["Male", "Female"]
        new_raw = {}
        phone_gen = lambda dig_str: "+" + dig_str[12:][::-1] + "(" + dig_str[9:12][::-1] + ")" \
                                    + "-" + dig_str[6:9][::-1] + '-' + dig_str[3:6][::-1] + \
                                    '-' + dig_str[0:3][::-1]
        for k in range(1000):
            if len(sorted_data[k]) == 1:
                new_raw["Name"] = sorted_data[k][0]
                new_raw["Date"] = datetime.datetime.now()
                new_raw["Email"] = (new_raw["Name"].replace(" ", "_") + "@gmail.com").lower()
                new_raw["Phone"] = phone_gen(str(random.randint(111110000000, 999999999999999))[::-1])
                new_raw["Gender"] = gender_list[random.randint(0, 1)]
                new_raw["Salary"] = random.randint(1000, 99999)
            else:
                new_raw["Name"] = sorted_data[k][0]
                new_raw["Date"] = sorted_data[k][1]
                new_raw["Email"] = (new_raw["Name"].replace(" ", "_") + "@gmail.com").lower()
                new_raw["Phone"] = phone_gen(str(random.randint(1111100000000, 99999999999999))[::-1])
                new_raw["Gender"] = gender_list[random.randint(0, 1)]
                new_raw["Salary"] = random.randint(1000, 99999)
            writer.writerow(new_raw)


create_combo('HW_6_nne_2.csv', "HW_6_combo.csv", names_lll[450:])
