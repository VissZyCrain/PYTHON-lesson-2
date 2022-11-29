# Задайте список из (2*N+1) элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных ИНДЕКСАХ. 
# Пять ИНДЕКСОВ хранятся в списке, который вы сами заполняете.
# Пример списка ИНДЕКСОВ [2, 2, 3, 1, 8]
# Ввод: 4
# [-4, -3, -2, -1, 0, 1, 2, 3,4]


import os
os.system('cls')

print('Задача № 3')

from random import randint

def list(n):
    list = []
    for i in range(n):
        list.append(randint(-n, n))
    return list

n = int(input('Введите число N: '))
numbers = list(n)
print(numbers)
b = open('file.txt','r')
result = numbers[int(b.readline())] * numbers[int(b.readline(2))]
print(result)