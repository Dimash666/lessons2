# number = input("vvedit:").split()
# number = list(map(int,number))
# print(number)
# pow_number = list(map(pow,number))

# def main_pow(x):
#     return x **2 


# print(main_pow(2))

# numbers = [1,2,6,3,5,9]
# b = []
# for i in numbers:
#     if i > 5:
#         b.append(i)
# print(b)    

# b = [i for i in numbers if i > 5]
# print(b)
# def main_f(x):
#     if x % 3 == 0 or x % 5 == 0:
#         return True
# list_filter = list(filter(lambda x : x > 5 , numbers))

# print(list_filter)


# a = [1,3,4,5]
# b = ['a','b','c','d']
# print(list(zip(a,b)))


# while True: print(eval(input(">>>")))

# sum()
# min()
# max()
# sorted()
# reversed()
# len()
# range()
# print()
# list()
# tuple()
# set(), dict(), int()
# input()
# slice()


# enumerate()
# map()
# filter()
# zip()
# all()
# any()
# eval()
# round()
# abs()
# pow()

# a = ['Asel', 'Mansur', 'Alim', 'Jahongir', 'Abdulloh', 'Alexandr', 'Vlad']

# for i, v in enumerate(a):
#     if i % 2 == 0:
#         print(i, v)

# print(list(enumerate(a)))


# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 1
# c = [str(i) for i in a]

# 2
# b = []
# for i in a:
#     b.append(str(i))

# 3
# b = list(map(str, a))

# print(b)
# c = list(map(int, b))
# print(c)

# print(''.join(b))


# def main_pow(x):
#     return x ** 2

# print(main_pow(2))


# numbers = input("Введите числа через пробел: ").split()
# numbers = list(map(int, numbers))
# print(numbers)
# pow_numbers = list(map(lambda x: x ** 2, numbers))
# print(pow_numbers)



# numbers = [1, 2, 6, 3, 8, 5, 9, 4]

# b = []
# for i in numbers:
#     if i > 5:
#         b.append(i)
# print(b)

# b = [i for i in numbers if i > 5]
# print(b)

# def main_f(x):
#     if x % 3 == 0 or x % 5 ==0:
#         return True
# list_filter = list(filter(main_f, numbers))
# print(list_filter)

# list_filter = list(filter(lambda x: x % 3 == 0 or x % 5 ==0 , numbers))
# print(list_filter)





# a = [1,    3,   4,   5]
# b = ['a', 'b', 'c', 'd']

# print(list(zip(a,b)))




# all()
# any()
# eval()
# round()
# abs()


# a = [True, True, False]

# a = [12,3243,345,456,46,46]
# c = [True if i % 2 == 0 else False for i in a]

# print(c)
# print(all(c))
# print(any(c))

# a = -943
# print(abs(a))
# v = 23
# print(-v)

# s = 54.829234
# print(round(s, 2))

# while True: print(eval(input(">>> ")))
# >>>>>1
# values = ("Razakov 32", 10, 1005, ["tables", "chairs"], 23.00)
# a = []

# for i in values:
#     if i 
    

# >>>>>1

# a = ("Dimash Banana Tokaev Clown")
# letters = "aoie"
# print(len(list(filter(lambda x: x in letters,a))))



# >>>>.2
# def num(x):
#     return x*2

# numbers = [1,2,3,4,5]
# b = list((map(num,numbers)))

# print(b)


# >>>>>>3

# numbers = [-2,-5,0,7,-1,9,4]
# def possitive(numbers):
#     if numbers > 0:
#         return True

# print(list(filter(possitive, numbers)))


# >>>>>4.

# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# print(list(zip(names,ages)))

# >>>>>>5
# numbers = [2, 4, 6, 8, 9]
# def num(x):
#     if x % 2 == 0:
#         return True
#     else:
#         return False
# b = all(map(num,numbers))
# print(b)
   
# >>>>>>6
expression = "2 * (3+4)"
print(eval(expression))

# >>>>>>>7
# number = 3.14159
# print(round(number,2))
