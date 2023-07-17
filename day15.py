# def get_5(item: int, massiv: list) -> bool:
#     if type(massiv) not in [list, tuple]:
#         raise TypeError('Массив должен быть списком или картежом')
    
#     if item in massiv:
#         return True
#     return False

# print(get_5(2, 6))




# def fibonachi(n: int) -> list:
#     x1, x2 = 1, 1
#     lst = []
#     for _ in range(n):
#         lst.append(x1)
#         x1, x2 = x2, x1 + x2
#     return lst
# print(fibonachi(100))




# def main(n: int) -> int:
#     if n % 2 == 0:
#         return n
#     return n + 1

# a = main(4)
# print(a)







# def main(n: int = 10000) -> int:
#     if n % 2 == 0:
#         return n
#     return n + 1

# print(main(213213))



# def main(*args):
#     return sum(args)

# print(main(2, 3, 4, 5, 6, 7, 8, 9, 10))


# def main(**kwargs):
#     return list(kwargs.items())

# print(main(name='Ivan', age=23, city='Moscow', country='Russia'))




# def main(a, b=None, *args, **kwargs):
#     return f"{a=}, {b=}, {args=}, {kwargs=}"
# print(main(1, name='Ivan', age=23))


# def digital_root(n):
#     if n > 9:
#         return digital_root(eval('+'.join(str(n))))
#     return n

# print(digital_root(132189))



# >>>>>>>1
# def add(x,y) :
#     return (x+y)

# print(add(3,2))

# def substract(x,y):
#     return(x-y)

# print(substract(4,1))

# def multiply(x,y):
#     return(x*y)

# print(multiply(5,4))


# def divide(x,y):
#     return x // y

# print(divide(25,5))


# >>>>>>>>2

# def get_len(text):
#     count = 0
#     for _ in text:
#         count += 1
#     return(count)

# print(get_len("dsadaskd"))


# >>>>>>3
# def DICT(a,b):
#     a = {1:"Dimash"}
#     b = {2:"Meru"}
#     c = a|b
#     return c
# print(DICT("a","b"))
# # >>>>>>4
# import os

# def заказать_еду():
#     еда = input("Что бы вы хотели заказать? ")
#     напиток = input("Что бы вы хотели выпить? ")

    
#     with open("menu.txt", "w") as f:
#         f.write(f"Заказ: {еда}, {напиток}")

#     print("Ваш заказ был записан в файл menu.txt на рабочем столе.")

# заказать_еду()

# >>>>>>5
# def создать_файл():
#     file = input("Введите название файла:")

#     with open(file,"w") as f:
#          print("Файл создан")


# создать_файл()


# >>>>>>6

def function1():
    def function():
        return

# >>>>>>7
# def dim(x):


def convert(users: dict) -> dict:
    keys_tuple = tuple(users.keys())
    values_tuple = tuple(users.values())
    return keys_tuple, values_tuple
    
users = {'a': 1, 'b': 2, 'c': 3} 
keys, values = convert(users)
print(keys, values)
    
    





