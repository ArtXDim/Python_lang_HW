# Задача 18: Требуется найти в массиве A[1..N] самый близкий по 
# величине элемент к заданному числу X. Пользователь в первой 
# строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

# import random #import module

# n = int(input('Введите длину массива от 1 до .... \n')) # input number n
# rand_lst = [random.randint(0, 10) for _ in range(n)] # array creation
# print(rand_lst) 
# x = int(input("Введите заначение x ..... \n")) # input number x

# near = abs(x-rand_lst[0]) #  near number
# num = rand_lst[0]  

# for i in rand_lst: # 
#     if near > abs(x - i): # condition
#         num = i
#         near = abs(x - i)
#         if near == 0:
#             break

# print(f"Близкое значение к {x} это {num}")



# N = int(input('Input len massiv\n'))
# lst = map(int, (input().split()))
# print(lst)
# x = int(input())
# print(min(lst, key=lambda a:abs(a-x)))

import random #import module

n = int(input('Введите длину массива: \n'))
rand_lst = [random.randint(0, 10) for _ in range(n)] # array creation
print(rand_lst)
x = int(input("Введите значение x: \n")) # input number x

res = rand_lst[0]
for i in rand_lst:
    if abs(i - x) < abs(res - x):
        res = i

print(res)