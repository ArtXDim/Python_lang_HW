# Задача 22: Даны два неупорядоченных набора целых чисел (может быть,
# с повторениями). Выдать без повторений в порядке возрастания все те числа,
# которые встречаются в обоих наборах. Пользователь вводит 2 числа. n - кол-во
# элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random as ran

n = int(input('Введите количество элементов первого массива от 1 до .... \n'))
m = int(input('Введите количество элементов второго массива от 1 до .... \n'))
rand_lst_1 = set([int(ran.randint(1, 10)) for _ in range(n)])
rand_lst_2 = set([int(ran.randint(1, 10)) for _ in range(m)])
print(*rand_lst_1)
print(*rand_lst_2)
rand_lst_1_set = set(rand_lst_1)
rand_lst_2_set = set(rand_lst_2)
lst_set = rand_lst_1.intersection(rand_lst_2)
if len(lst_set) == 0: 
    print ("Нет повторений чисел")
else: 
    print(*sorted(lst_set))
    
# # print(f'Числа встречающиеся в двух списках:\n {sorted.set(res)}')

# # print(sorted(rand_lst_1 & rand_lst_2, key=int))

# print(*sorted((rand_lst_1.split()) & (rand_lst_2.split()), int))
