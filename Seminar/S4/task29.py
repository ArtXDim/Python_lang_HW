# Ваня и Петя поспорили, кто быстрее решит следующую задачу: 
# “Задана последовательность неотрицательных целых чисел. 
# Требуется определить значение наибольшего элемента последовательности, 
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2  друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. 
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор. 
# За помощью товарищи обратились к Вам, студентам.

# Примечание: Программные коды на следующих слайдах

import random
n= 20

a = [random.randint(1, 10) for _ in range(n)]
print(a)
b = []

idx = random.randrange(len(a))

a.insert(idx, 0)

for i in range(len(a)):
    if a[i] != 0:
        b.append(a[i]) 
    else:
        break
print(b)
print(max(b))

