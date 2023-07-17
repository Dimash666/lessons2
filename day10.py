# f = open('main.txt', 'r')
# text = f.read() # фаил открыт в режимах чтения и запаковки в переменновой text 
# f.close()

# print(text)


# f = open('main.txt', 'a')
# f.write('Hello world!\n')
# f.close()

# a = 'Hello world!\n'

# with open('main.txt', 'a') as file:
#     file.write('Hello world!\n')

# with open('main.txt', 'r') as file:
#     text = file.read()
#     print(len(text.split('\n')))

# with open('main.txt','a') as file:
#     for i in range(1,101):
#         file.write(f"{i}\n")


# >>>>>1
# with open('directories.txt','r') as file:
#     text = file.read()
#     file.close()

# >>>>2

# with open('users.txt','a') as file:
#     log = input("Введте логин:")
#     pas = int(input("Ведите пароль:"))
#     file.write(f"n{log} , {pas}")


# >>>>3
# with open('directories.txt', 'r') as f:
#     if "w" in f.read():
#         print("da")
#     else:
#         print("net")

# >>>>4

# with open('python.txt', 'r') as f:
#     t_words = []
#     for line in f:
#         words = line.split()
#         for a in words:
#             if 't' in a or 'T' in a:
#                 t_words.append(a)
#                 print(a)

# >>>>5

# with open('database.txt', 'a') as f: 
while True:    
    # a = input("Введите 1 что бы ввойти или  2 что бы зарегестироватся: ")
    # if a == "1" :
    #     log = input("Введите логин: ")
    #     pas = input("Пароль:")  
    #     with open('database.txt', 'r') as f:
    #         data = f.read()
    #         if log in data and pas in data:
    #             print("Вы успешно вошли")
    #         else:
    #             print("Зарегайтесь")
    # elif a == "2":
    #     log2 = input("Ввеидте логин:")
    #     pas2 = input("Ввдите парль:")
    #     pas3 = input("Введите еще раз пароль:")
    #     if pas2 == pas3:
    #         with open('database.txt', 'r') as f:
    #             data = f.read()
    #             if log2 in data and pas2 in data:
    #                 print("Вы уже зареганы")
    #             else:
    #                 with open('datase.txt', 'a') as f:
    #                     f.write(f"{log2} {pas2}")
    #                     print("Вы успешно зреганы")

# >>>>6




