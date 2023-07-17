# import random

# data = {
#     1 : 'Камень',
#     2 : 'Ножницы', 
#     3 : 'Бумага'   
# }


# while True:
#     print('Введите ваш выбор: 1 - Камень, 2 - Ножницы, 3 - Бумага')
#     user_choice = int(input('>>> '))
#     if user_choice not in data:
#         print('Введите одно из допустимых значений')
#         continue
#     computer_choice = random.randint(1,3)
#     print(f'Вы выбрали: {data[user_choice]}')
#     print(f'Компьютер выбрал: {data[computer_choice]}')

#     if user_choice == computer_choice:
#         print('Ничя😐')
#     elif (user_choice == 1 and computer_choice == 2) or (user_choice == 2 and computer_choice == 3) or (user_choice == 3 and computer_choice == 1):
#         print('👄Вы победили😜')
#     else:
#         print('Вы проиграли!💩💩💩')
    


# import datetime


# today = datetime.date.today()

# now = datetime.datetime.now()

# print(now)
# print(today)

# now = datetime.datetime.now()
# formatted_date = now.strftime("Год: %Y месяц: %B день: %d")

# print(formatted_date)


# from datetime import datetime

# date1 = datetime(2000, 1, 28)
# date2 = datetime(2023, 7, 10)
# difference = date2 - date1
# print(difference.days)


# from datetime import datetime

# date_string = input('Введите дату в формате yyyy-mm-dd hh:mm:ss: ') # "2022-10-31 18:30:00"
# parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
# print(type(parsed_date))


# from datetime import date

# try:
#     user_date = input('Введите дату в формате yyyy-mm-dd: ')
#     user_date = date.fromisoformat(user_date)   
#     print(user_date)
# except ValueError:
#     print('Дата введена неверно')


# from datetime import datetime, timedelta
# import pytz

# # Установка часового пояса
# timezone = pytz.timezone("Europe/Moscow")
# localized_time = datetime.now(timezone)
# print(localized_time)

# # Добавление временного интервала
# future_time = localized_time + timedelta(hours=3)
# print(future_time)


# # Добавление временного интервала
# future_time = localized_time + timedelta(hours=6)
# print(future_time)


# from random import choice
# from string import ascii_letters, digits, punctuation

# print(punctuation)
# print(ascii_letters)
# print(digits)

# password = ''

# while len(password) < 10:
#     password += choice(ascii_letters + digits)

# print(password)


# password = '1234'

# count = 0
# while True:
#     zlom = ''.join(choice(digits) for i in range(4))
#     if zlom == password:
#         print('Вы зломали пароль')
#         print(f'Количество попытков: {count}')
#         break
#     count += 1
#     if count == 1000:
#         print('Вы проиграли!')
#         break

# import sys
# print(sys.version)

# import os
# import random
# import sys


# print(os.name) # -> Узнать общее имя операционной системы.

# print(sys.platform) # -> Узнать ДЕТАЛЬНОЕ имя ОС.

# print(random.choice(['name1','name2', 'name3', 'name4'])) 



# import sys 

# print(sys.argv)

# if sys.argv[1] == 'runsrver':
#     print('Запускаем ...')


# >>>>>>>1
# from data import Year
# print(Year)


# >>>>>>>2
# from random import choice

# names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", 
#     "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

# names2 = []

# for i in range (4):
#     a = choice(names)   
#     names2.append(a)
# print(names2)

# >>>>>>>3
# import sys
# print(sys.argv)

# >>>>>>4
# import os 
# for i in range (5):
#     os.system(f"touch Dimash/file{i}.py")

# >>>>>>5

from random import choice
import random

names = ["Aibek", "Joomart", "Adinai", "Ermek", "Atai", "Aslan", 
    "Lyazat", "Salavat", "Daniyar", "Bolotbek", "Alymbek", "Dastan", "Maksat"]

team1 = []
team2 = []
team3 = []
team4 = []



# print([[names.pop(random.randint(0,len(names)-1))for _ in range(3)]for _ in range(4)])




# for i in (team1,team2,team3,team4):
#     for _ in range(3):
#         i.append(names.pop(random.randint(0,len(names)-1)))

# print(team1)
# print(team2)
# print(team3)
# print(team4)
# print(names)

# while True:
#     for i in range (4):
    #     a = choice(names)
    #     team1.append(a)
    # print(team1)
    # for i in range(3):
    #     a = choice(names)
    #     team2.append(a)
    # print(team2)
    # for i in range(3):
    #     a = choice(names)
    #     team3.append(a)
    # print(team3)
    # for i in range(3):
    #     a = choice(names)
    #     team4.append(a)
    # print(team4)    
    
    # break
    
        
        



# >>>>>>1.1

# import sys
# print(sys.argv[1:])

# >>>>>>>>2.1
# import sys
# a = input(">>>>>")
# b = input(">>>>>")
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

# >>>>>>>3.1
# from random import choice
# from string import ascii_letters,digits, punctuation
# a = int(input("Input number:"))
# password = ""
# while len(password) < a:
#      password += choice(ascii_letters + digits + punctuation)

# print(password)


# >>>>>> 3.3.1

# from random import randrange

# a = (randrange(6,13,2))
# b = (randrange(5,101,5))

# print(f"{a}, {b}")


# >>>>>>>date1000

# import datetime

# dt = datetime.datetime.now()
# thdt = datetime.timedelta(days=1000)
# result = dt+thdt

# print(result)


# NNNN1

# numbers = [1, 12, 123, 1234, 12345, 123456, 1234567, 12345678, 123456789]

# for i in range(len(numbers)-1):
#     a = numbers[i] + (numbers[i + 1])
#     print(a)


# nnn2
# import datetime
# print(datetime.datetime.now())

# nnn3

# import time
# for i in range(1,11):
#     print (f"Step {i}")
#     time.sleep(1)


# nnn4

# list1 = [1,3,5,7,9,11,13]

# list2 = [2,4,6,8,10,12,14]

# a = zip(list1,list2)
# b = list(a)

# print(b)


