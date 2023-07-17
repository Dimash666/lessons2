# Created on Tue July 11 10:32:32 2023

# def hello():
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')
#     print('Hello World')


# # for i in range(10):
# #     print(i)
# #     hello()


# def get_len(text: str) -> int:
#     count = 0
#     for _ in text:
#         count += 1
#     return count


# s = 'kashdkjgashjdjhashdcjhgcagjcasxghashkxcakshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'
# b = 'kashdkjgashjdjha(shdcjhgcagjcasxghaskshx'
# d = 'kashdkjgashjdjhashdcjhgcagjcasxghaskshx'


# count = 0
# for i in s:
#     count += 1

# count_b = 0
# for i in b:
#     count_b += 1

# s_len = get_len(s)
# b_len = get_len(b)
# d_len = get_len(d)

# print(s_len == s_len == d_len)

# import string
# import random


# def generate_password(length: int) -> str:
#     symbols = string.ascii_letters + string.digits
#     password = ''
#     for _ in range(length):
#         password += random.choice(symbols)
#     return password


# p1 = generate_password(10) 
# p2 = generate_password(10) 
# p3 = generate_password(10) 
# p4 = generate_password(10) 
# print(p1,p2,p3,p4)







# def get_5(item: int, massiv: list) -> bool:
#     if type(massiv) not in [list, tuple]:
#         raise TypeError('Массив должен быть списком или картежом')
    
#     if item in massiv:
#         return True
#     return False

# print(get_5(2, 6))



# >>>>>1

# def sqwr(x):
#     x = x **2
#     return x

# n = int(input("NN"))
# print(sqwr(n))


# >>>>>>2
# def mas(x):
#     from random import randint
#     a = []
#     for i in range(x):
#         a.append(randint(0,100))

#     return a

# print(mas(10))

# >>>>>>3

# def dim(x):
#     return x[::-1]

# print(dim("Dimash"))   


# >>>>>>4

# def dim(text:str) -> int:
#     count = 0
#     for _ in text:
#         count += 1
#     return count

# print(dim('wertyuiop'))


# >>>>>>>5
# def dim(text:str):
#     if text == text[::-1]:
#         return "Palindrome"
#     else:
#         return "NOT"
    

# print(dim("MAM"))

# >>>>>>6

# def dim(x):
#     b = ""
#     while x > 0:
#         b = str(x % 2) + b
#         x = x // 2
#     return b

# print(dim(55))

# >>>>>>7
# def dim(x,y):
#     if x == y:
#         return 0
#     elif x > y :
#         return 1
#     else:
#         return -1

# print(dim(1,2))

# >>>>>>>8

# def get_len(text: str) -> int:
#     count = 0
#     for _ in text.split( ):
#         count += 1

#     return count

# s = "Dimsh shamid"


# count = 0
# for i in s:
#     count += 1

# print(get_len(s))

# >>>>9

# def dim(text:str)->list:
#     a = []
    
#     word = ""
#     for i in text:
#         if i != " ": 
#             word += i
#         else:
#             a.append(word)
#             word = ""
#     a.append(word)
#     return a

# print(dim("Dimash Shamid sadjhasj sjd ajh asudh asjh as"))



# def dim(x):
#     if x == 1:
#         return x
#     return dim(x-1)*x 

# print(dim(6))

# def dim(x):
#     d = 2
#     while x % d != 0:
#         d += 1
#     return d == x
    
# print(dim(6))


# def fibonachi(n:list):
#     x1, x2 = 1, 1
#     lst = []
#     for i in range(10):
#         lst.append(x1)
#         x1, x2 = x2, x1 + x2
#     return lst

# print(fibonachi(15))







   
