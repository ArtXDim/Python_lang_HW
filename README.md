# Python_lang_HW
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


# dct = {
#     'en':{
#         'A':1, 'E':1, 'I':1, 'O':1, 'U':1, 'L':1, 'N':1, 'S':1, 'T':1, 'R':1,
#         'D':2, 'G':2,
#         'B':3, 'C':3, 'M':3, 'P':3,
#         'F':4, 'H':4, 'V':4, 'W':4, 'Y':4,
#         'K':5,
#         'J':8, 'X':8, 
#         'Q':10, 'Z':10
#     },
#     'ru':
#         {'А':1, 'В':1, 'Е':1, 'И':1, 'Н':1, 'О':1, 'Р':1, 'С':1, 'Т':1,
#         'Д':2, 'К':2, 'Л':2, 'М':2, 'П':2, 'У':2,
#         'Б':3, 'Г':3, 'Ё':3, 'Ь':3, 'Я':3,
#         'Й':4, 'Ы':4,
#         'Ж':5, 'З':5, 'Х':5, 'Ц':5, 'Ч':5,
#         'Ш':8, 'Э':8, 'Ю':8,
#         'Ф':10, 'Щ':10, 'Ъ':10
#     }    
# }
# word = input('Input word\n').upper()
# value = 0
# lang = 'en' if word[0] in dct['en'] else 'ru'

# for letter in word:
#     if letter in dct[lang]:
#         value += dct[lang][letter]
#     else:
#         break
# else:
#     print(f'Sum of symbol: {value}')