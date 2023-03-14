# Хакер Василий получил доступ к классному журналу и хочет заменить все 
# свои минимальные оценки на максимальные. Напишите программу, 
# которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

# Input: 5 -> 1 3 3 3 4

# Output: 1 3 3 3 1


import random

n = int(input('Введите длину массива от 1 до .... \n'))
rand_lst = [random.randint(1, n) for _ in range(n)]
print(rand_lst)

a = min(rand_lst)
b = max(rand_lst)
rand_lst.insert(b,a) for i in rand_lst
     
print(rand_lst)

import random
n = int(input())
grades = [random.randint(1, 5)for _ in range(n)]
print(grades)

minimum = min(grades)
maximum = max(grades)
print(list(enumerate(grades)))
for i, value in enumerate(grades):
    if value == maximum:
        grades[i] = minimum

print(*grades)