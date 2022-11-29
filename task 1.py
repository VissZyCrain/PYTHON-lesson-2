# Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

import os
os.system('cls')

print('Задача № 1')

# Решение с помощью факториала
# def factorial (number, count = 1):
#     for i in range(1, number + 1):
#         count *= i
#     return count

# n = int(input('Введите число N: '))
# print(f'Набор произведений чисел от 1 до N равен числам: ', end = '')
# for i in range(1, n + 1):
#     if i == n: 
#         print(f'{factorial(i)}')
#     else:
#         print(f'{factorial(i)}', end = ', ')

N = int(input('Введите число N: '))

f = 1
for i in range(N):
    i = i + 1
    f = i * f
    
    print(f, end=" ")