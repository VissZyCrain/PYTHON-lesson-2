# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]

import os
os.system('cls')

print('Задача № 3')

n = int(input('Введите число N: '))
list1 = [i for i in range(-n, n+1)]
print(list1)
list2 = [2, 2, 3, 1, 8]
proiz = 1
for index in list2:
    proiz *= (list1[index])
    print(list1[index])
print(proiz)


# Решение через .txt

# from random import randint

# def list(n):
#     list = []
#     for i in range(2*n+1):
#         list.append(randint(-n, n))
#     return list

# n = int(input('Введите число N: '))
# numbers = list(n)
# print(numbers)
# # x = open('file.txt','r')
# # result = numbers[int(x.readline())] * numbers[int(x.readline(2))]
# # print(result)