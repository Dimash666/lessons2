# # users = {
# #     'name': 'Anton'
# # }

# # try:
# #     print(a['age'])
# # except  KeyErrore  as e:
# #     print('Mi ilovili KeyError',e)
# # except NameError as e:
# #     print('Vi ne sozdali peremenny!',e)

# # else:
# #     print('Vse ok! 200')
# # finally:
# #     print('Obrabotka zaverwena!')
# zero_except = 0

# while True: 
#     try:
#         print(eval(input('>>>>')))
#     except ZeroDivisionError as e:
#         zero_except += 1
#         print('Vi pitaetes delit na nol!')
#         print('Bolwe ne pitaites')
    
#     except TypeError as e:
#         print('Vi pitaetets rabott s raznimy dannimi')

#     except KeyboardInterrupt as e:
#         print('\nViostanovili!')
#         break

#     except SyntaxError as e:
#         print("Simvol oshibka")

#     except NameError as e:
#         print('Vi ne sozdali peremennoe')
#     if zero_except == 3:
#         print("BAN ZA ZeroDivisionError")
#         print("Podelili na 3")
#         break

# import random
# from random import randint, randrange, choice, shuffle
# users = ['Edils','Bekarys','Beka']

# shuffle(users)
# print(choice(users))
# print(random.randrange(0,10,2))
# print(randint(0,10))
# print(random.randint(0,10))


# import os 
# os.system("ls / > commannd.txt")


# >>>>>1
# import random
# n = random.randrange(1,10) 
# try:
#     user = int(input("Ugadaite chislo:"))
#     if user == n:
#         print("Perfect")
#     else:
#         print("bad")
# except ValueError as n:
#     print("Функция не поддерживает данный тип днных")


# >>>>>2
# import random
# from random import choice
# a = ["Dimash","Tokaev","MAMAGUEVA","TEACHER","LOL"]
# print(choice(a))

# >>>>>>3
# import random
# n = random.randrange(1,1000)

# count = 0
# while True:
#     try:
#         user = int(input("Ugadaite chislo:"))
#         if user == n:
#             print("Молодец")
#             print(f"Вы угадали {count} попыток")
#             break
#         else:
#             print("Собака умнее тебя")
#         if user > n:
#             print("Слишком много")
#         else:
#             print("Слишком мало")
#         count += 1
#     except ValueError as n:
#         print("Функция не поддерживает данный тип днных")


# >>>>>>4


# import random
# from random import choice


# try:
#     a = []
#     print(choice(a))
# except IndexError as a:
#     print("Zapolnite spisok")

    


# >>>>>>>5
# import random
# x = random.random()
# y = random.random()
# print(x,y)

# >>>>>>6
# import random

# # Создаем список с различными типами данных
# my_list = [1, "hello", [2, 3, 4], {"name": "John"}, 3.14]

# try:
#     # Выбираем случайный элемент из списка
#     random_element = random.choice(my_list)

#     # Выводим выбранный элемент на экран
#     print("Случайный элемент из списка:", random_element)

#     # Пытаемся выполнить операцию, зависящую от типа элемента
#     if isinstance(random_element, int):
#         result = random_element + 10
#         print("Результат операции:", result)
#     elif isinstance(random_element, str):
#         result = random_element.upper()
#         print("Результат операции:", result)
#     elif isinstance(random_element, list):
#         result = len(random_element)
#         print("Результат операции:", result)
#     elif isinstance(random_element, dict):
#         result = random_element.keys()
#         print("Результат операции:", result)
#     elif isinstance(random_element, float):
#         result = random_element * 2
#         print("Результат операции:", result)

# except IndexError:
#     print("Список пустой. Нет элементов для выбора.")
# except TypeError:
#     print("Выбранный элемент имеет несовместимый тип данных.")



# # >>>>>>7

# from random import choice

# letters = "1234567890qwertyuiopsdfghjklzxcvbnm"

# password = ''

# for i in range (9):
#     a = choice(letters)
#     password += a
    
# print(password)


# >>>>>8
# from random import randrange




# try:
#     n = int(input("Введите число:"))
#     a = randrange(1,n)
#     print(a)
# except ValueError as n:
#     print("Не являться целым положительным числом")



# >>>>>9

# from random import choice

# symbols = "@#$%^&)(**$#%$#)"

# password = ''
# n = int(input("Dlinna:"))

# for i in range (n):

#     a = choice(symbols)
#     password += a
    
# print(password)



# >>>>>10

from random import choice

a = ["a","2","4","D"]

try:
    
    element = choice(a)

    element = int(element)
    print(element)
except ValueError:
    print("vALEU")

