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