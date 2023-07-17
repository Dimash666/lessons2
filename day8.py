# Не Изменяемые
# int 
# float
# str
# bool
# tuple

# Изменяемые
# list
# set 
# dict

# a = [3,4,5,3,3,4,4,5,6,7,7,8,8,9,1,1,1,1,1,6]
# a = list(set(a))
# print(a)



# a = {3,4,5,3,3,4,4,5,6,7,7,8,8,9,6, 0, (2131, ), 123.123, 'asdasdsd' }
# a.add('wqeqwe')
# print(a)


# a = {3,4,5,3,3,4,4,5,6,7,7,8,8,9,6, 0, (2131, ), 123.123, 'asdasdsd' }
# a.remove(3)
# print(a)

# a = {3,4,5, 123.123, 'asdasdsd'}

# a.clear()
# print(a)

# a = set()

# a = {3,4,5, 123.123, 'asdasdsd'}

# a.remove(7)
# a.discard(7)
# print(a)
# print(a.p


# a = {1, 2, 4, 5}
# b = {4, 5, 6, 7, 8}

# print(a.intersection(b))
# print(a.intersection(b))
# print(b.difference_update(a))

# print(b)
# print(b)
#########################################

# a = {1, 2, 4, 5}
# b = {4, 5, 6, 7, 8}
# a.update(b)
# print(a)



# foods = ["Coca-Cola", ['Potato', 'Cheeps']]
# foods = {
#     "drinks": "Coca-Cola",
#     "drinks": "Pepsi",
#     "snacks": ['Potato', 'Cheeps']
# }

# print(foods['drinks'])
# print(foods['snacks'][1])




# foods = {
#     "drinks": "Pepsi",
#     "snacks": ['Potato', 'Cheeps']
# }

# foods.update({'colas': 'Coca-Cola'})
# print(foods)
# foods['eda'] = 'Plov'

# print(foods)
# foods['snacks'].append('Burger')
# print(foods)





# foods = {
#     "drinks": "Pepsi",
#     "snacks": ['Potato', 'Cheeps']
# }

# foods.pop('snacks')
# print(foods)

# print(foods.get("drin"))
# print(foods["drin"])


# print(foods.keys(), foods.values(), foods.items())

# for key, value in foods.items():
#     print(f"{key=}, {value=}")

# 4!
# a = {"FedEx","Tokaev","Lego","NavData","Elephant"}
# a.add("Kia")
# a.pop()
# print(a)


# 1 ONE -->
# menu = {
#     "Besh_barmak": "130 som",
#     "borsh" : "100 som"
# }
# menu.update({"Lagman": "130 som"})
# menu.pop("borsh")
# print(menu)

# 2 two =
# menu = {"lagman": "120", 
#          "plov" : "120 ",
#          "borsh": "100"
#          }
# menu.update({"drinks" : ["Coca-Cola","Sprite","Fanta"]})
# print(menu)

# 020
# methods = {"add","remove","clear","update","difference","dsicard","intersection","intersection_update","pop"}
# methods2 = {"clear","get","keys","value","items","update"}


# print(methods.intersection(methods2))
# print((methods).difference_update(methods2))


# 31 

# a = {}
# for i in range(0,3):
#     loggin = input("Введите логин:")
#     password = input("Введите пароль:")
#     a.update({loggin: password})

# print(a)


# 27
# a = {"Tokaev":"AGENT","Kairat":"singer","Dimash":"banan","Bektur":"Teacher","leg":"floor"}
# for key,value in a.items():
#     print(f"Здравствуйте {key}, Прекрасная профессия {value}")

# a = set()
# for i in range(0,10):
#     number = int(input("Введите число:"))
#     a.add(number)
# a = tuple(a)
# print(a)

# #11
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
# 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']

# a = list(set(south_american_countries))
# print(a)

# #101
# suitcase = []
# count = 0
# while count < 5:
#         suit = input("Введите вещь: ")
#         suitcase.append(suit)
#         count += 1
# print(suitcase) 


#001

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

# print(farm_2.intersection(farm_2))
# print(farm_1.difference(farm_2))

# >>>>>>>>>>>>>>>>>>>>>
# for i in range(60):
#     for j in range(60):
#         # os.system('clear')
#         # print(f'{i}:{j}')
#         # time.sleep(0.3)





# a = {
#     'kuhnya1': {
#         'stol': 10,
#         'stul': 2
#     },
#     'kuhnya2': {
#         'stol': 10,
#         'stul': 2
#     }
# }

# area = 0
# for i in a:
#     area += sum(a[i].values())
# print(area)


# area = 0
# for i in a:
#     for j in a[i]:
#         print(j, a[i][j])
#         area += a[i][j]

# print(area)


# for i in range(1, 20+1):
#     for j in range(1, 20+1):
#         print(f'{i} ** {j} = {j**i}')
#     print()


# a = [1,2,3,4,5, 6, 7, 7,8,8]

# c = [{i:i**2} for i in a if i % 2 == 0]

# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append({i:i**2})

# print(b)
# print(c)

# a = []
# for i in range(100):
#     a.append(i)

# print(a)

# b = [i for i in range(100)]
# print(b)

# c = list(range(100))
# print(c)



# a = []
# for i in range(10):
#     if i % 2 == 0:
#         a.append(0)
#     else:
#         a.append(i)
# print(a)

# b = [0 if i % 2 == 0 else i for i in range(10)]
# print(b)

# c = [i for i in range(10) if i % 2 != 0]
# print(c)


# a = 0 if 5 % 5 != 0 else 5

# print(a)

# s = {i:i*2 for i in range(10)}

# print(s)

# house = {
#     "гостиная": {
#         "диван": 10,
#         "стол": 5,
#         "телевизор": 3,
#         "кресло": 7
#     },
#     "кухня": {
#         "стол": 6,
#         "стул": 3,
#         "холодильник": 4,
#         "плита": 5
#     },
#     "спальня": {
#         "кровать": 12,
#         "шкаф": 8,
#         "тумбочка": 2,
#         "комод": 6
#     },
#     "ванная": {
#         "ванна": 10,
#         "раковина": 4,
#         "туалет": 3,
#         "зеркало": 2
#     }
# }


# area = 0
# for i in house:
#     area += sum(house[i].values())
# print(area)



# area = 0
# for i in house:
#     for j in house[i]:
#         print(j, house[i][j])
#         area += house[i][j]

# print(area)

cities = []
while True:
    action = int(input("Выберите действие: \n"
        " 1. Добавить новый город \n"
        " 2. Отобразить список городов \n"
        " 3. Заменить город \n"
        " 4. Удалить город \n"
        " 5. Посетить следующий город \n"
        " 6. Выход \n"))
    if action == 6:
        print("Программа завершает работу!")
        break
    elif action == 1:
        city = input("Введите название города: ")
        if cities == city:
            print(f"б. Такой город уже есть!, {cities[city]}")
        elif city.isdigit() == True:
            print("в. Некорректное название!")
        else:
            cities.append(city)
            print("a. Город добавлен!")
    elif action == 2:
        if cities == []:
            print("Нет городов для вывода, заполните лист!")
        else:
            print(f"Список городов: \n", cities)
    elif action == 3:
        if cities == []:
            print("Нет городов для изменения, заполните лист!")
        else:
            choice = int(input(f"Выберите город по номеру для замены (счет начинается с 0):{cities}: "))
            city = input("Введите новый город: ")
            print(f"Новый город: {city}")
            if city != cities:
                cities[choice] = city
                print("б. Город заменен")
            elif cities[choice] == city:
                print(f"в. Такой город уже есть! {city} - 3")
            elif city.isdigit() == True:
                print("г. Некорректное название!")
    elif action == 4:
        if cities == []:
            print("Нет городов для удаления, заполните лист!")
        else:
            choice2 = int(input(f"Выберите город по номеру для удаления (счет начинается с 0):{cities}: "))
            city = input("Введите название города, который вы хотите удалить: ")
            if city != cities[choice2]:
                print("а. Текущий город отсутвует")
            elif city.isdigit() == True:
                print("б. Некорректное название!")
            elif city == cities[choice2]:
                cities.pop(choice2)
                print("в. Город удален!") 
    elif action == 5:
        if cities == []:
            print("Нет городов для выбора, заполните лист!")
        else:
            city_choice = int(input(f"В каком городе вы хотите находится в данный момент? (счет начинается с 0) {cities}: "))
            print(f"На данный момент мы находимся в городе: {cities[city_choice]}")
            choice3 = int(input(f"Выберите, какой город вы хотите посетить следующим? (счет начинается с 0):{cities}: "))
            city = input("Введите название города, который вы хотите Посетить: ")
            if city == cities[choice3]:
                print(f"а. Сейчас мы находися в городе: {cities[choice3]}")
            elif city.isdigit() == True:
                print("б. Некорректное название!")
            elif city != cities[choice3]:
                print("в. Вы выбрали разные значения пары значение/название!")


