# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)


# witn int
a = int(input("Input three-digit number:\n"))
print(f"{a} -> {a // 100 + a % 100 // 10 + a % 10}"
      f" ({a // 100} + {a % 100 // 10} + {a % 10})")


# with string
b = input("Input three-digit number:\n")
print(f"{b} -> {int(b[0])+int(b[1])+ int(b[2])} "
      f"({int(b[0])} + {int(b[1])} + {int(b[2])})")
