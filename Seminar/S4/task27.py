# txt = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells".lower().split()
# # print(txt)
# print(len(set(txt.replace(';', '').replace('.', '').replace(',', '').lower().split())))
# # for i in txt():
# #     if txt(i) = 

# n = int(input())
# s = ''
 
# for i in range(n):
#     s += input() + ' '
    
# print(len(set(s.split())))

text = input("Input: ")
words = text.lower().split()
unique_words = set(words)
print("Output:", len(unique_words))