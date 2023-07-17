# def chet(func):
#     def wrapper(n):
#         number = func(n)
#         if number % 2 == 0:
#             return number
#         return number + 1
#     return wrapper


# @chet
# def main(n):
#     return n


# print(main(7))
# import time


# def timer(func):
#     def wrapper(*args):
#         start = time.time()
#         result = func(*args)
#         print(time.time() - start)
#         return result
#     return wrapper

# @timer
# def gen_num(n):
#     return [i for i in range(n)]




# print(gen_num(10))



# def decorator(func):
#     def wrapper():
#         print('Start')
#         func()
#         print('End')
#         return 
#     return wrapper


# @decorator
# def mainer():
#     print('Hello')


# print(mainer())


# >>>>>>1
# def double(x,y,z):
#     f = (lambda x,y,z: x*y*z)(x,y,z)
#     return (f"Объем бассейна {f}")

# print(double(2,5,7))

# >>>>>>>>2
# import datetime

# countdown = lambda days_passed: f"До Нового года осталось {365 - days_passed} дней."

# days_passed = 200
# result = countdown(days_passed)
# print(result)

# >>>>>3
# def print_odd_numbers(n):
#     if n <= 0:
#         return
#     if n % 2 != 0:
#         print(n)
#     print_odd_numbers(n - 1)


# n = 20
# print("Нечетные числа от 1 до", n, ":")
# print_odd_numbers(n)

# >>>>>4
# def dim(x):
#     print(x)
#     if len(x) == 0:
#         return x
#     else:
#         x.pop()
#         return dim(x)
    
# print(dim(set("Dimash")))

# >>>>>>>5
# from random import randrange

# def decor(fun):
#     def wrap():
#         a = fun()
#         b = list(set(a))
#         return b
#     return wrap

# def sort_decor(fun):
#     def wrap():
#         a = fun()
#         a.sort()
#         return a 
#     return wrap

# @sort_decor
# @decor
# def decor2():
#     return [randrange(10,1500) for i in range(100)]

# print(decor2())

# def decor(fun):
#     def wrap():
#         print(123)
#         fun()
#         print(45)
#     return wrap

# @decor
# def name():
#     print(1)
# name()
# a = [1,2,3]
# b = [*a,4,5,6]

# print(b)
# a.extend(b)
# print(a)

# name()




# def name(**a):
#     return a

# print(name(name=213, age=123))



# def a(n):
#     if n < 11:
#         print(n)
#         return a(n+1)

# a(1)


# def dim_dekor(func):
#     def wrap():
#         login , password = func()
#         login = [ord(i) for i in login]
#         password = [ord(i) for i in password]
#         print(login,password)
#         return  login, password 
#     return wrap

# def dim2(func2):
#     def uncode():
#         login , password = func2()
#         login = ''.join(chr(i) for i in login)
#         password = [chr(i) for i in password]
#         return login, ''.join(password)
#     return uncode

# @dim2
# @dim_dekor
# def dim():
#     login = input("Введите логин:")
#     password = input("Введите пароль:")
#     return login , password

# print(dim())


# >>>>>>last
# n = int(input("Введите число:"))
# a = [1,185,1745345,98726,439872634,7312,64872,123687126,9312,4124,231,3123,34,3453] 
# new_list = list(map(lambda x :x*n  , a))
# print(new_list)

tables = [lambda x = x: x*10 for x in range(1, 11)]
for table in tables:
    print(table())