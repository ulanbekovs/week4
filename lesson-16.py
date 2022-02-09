''' Встроенные функции '''
# abs(-2)
# pow(3, 2)   #вводит в степень
# print()
# input()
# len()
# list()
# s = {"k": 2}
# p = list(s.items())
# print(p)
# tuple()
# int()
# str()
# type()
# dir()

# map(), filter(), reduce(),

''' map '''

# def add(x):
#     return x * 7
# lists = [3, 5, 8, 12]
# add_to = list(map(add, lists))    # map всегда первым аргументом принимает функцию например def add()
# print(add_to)


# def fact(a):
#     if a < 0:
#         a = abs(a)
#     x = 1
#     for i in range(1, a + 1):
#         x *= i
#     return abs(x)
#
#
# lists = [3, -5, 8, -2]
# list_new = list(map(fact, lists))
# print(list_new)

# def fact(a):
#     if a < 0:
#         a = abs(a)
#     x = 1
#     for i in range(1, a + 1):
#         x *= i
#     return abs(x)
#
#
# lists = [-3, 5, -8, 2]
# # q = list(map(abs, lists))
# list_new = list(map(fact, lists))
# print(list_new)

''' filter '''

# def test(number):
#     if number <= 3:
#         return number
#
# numbers = [1, 19, 13, 3,]
# result = filter(test, numbers)
# print(list(result))

# polindrom = ["Анна", "Civic", "китнаморенеромантик", "Almaz", "Ulukbek",]
#
# def is_polindrom(strin):
#     new_str = strin[::-1]
#     if strin.lower() == new_str.lower():
#         return strin
#
# new_polindrom = list(filter(is_polindrom, polindrom))
# print(new_polindrom)

''' reduce '''
# from functools import reduce  #функция reduce принимает только 2 аргумента
#
# def proiz(a, b):
#     return a * b
#
# numbers = [4, 2, 2, 3]
# num = reduce(proiz, numbers)
# print(num)

''' home work '''

# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето или осень).

# year = [1, 2, 3, 4, 5 ,6,7 ,8 ,9 ,10, 11, 12, ]
#
# def season(n):
#     if n == 12 or n < 3:
#         print("Winter")
#         return "Зима"
#     elif n == 3 or n < 6:
#         print("spring")
#         return "Весна"
#     elif n == 6 or n < 9:
#         print("summer")
#         return "Лето"
#     else:
#         print("autumn")
#         return "Осень"
#
# num = int(input("Введите число месяца: "))
# s = map(season, )
# print(s)

test