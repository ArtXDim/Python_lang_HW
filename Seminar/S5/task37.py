# Дано натуральное число N и последовательность из N элементов. 
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы 
# и использовать циклы (даже для ввода и вывода).

# Input:    2 -> 3 4
# Output:   4 3

# def reversed(variab): 
#     if len(variab) == 1:
#         return varib
#     return variab[-1] + reversed(variab[:-1])

# #print(reversed(input()))

def reverseString(any_string):
    if any_string == "":
        return any_string
    else:
        return reverseString(any_string[1:]) + any_string[:1]