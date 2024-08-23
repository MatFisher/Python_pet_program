#Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X

import random
from random import randint

my_list = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    my_list.append(random.randint(0,10))
print(my_list)

k = int(input("Введите число: "))
min = k
result = 0
for item in my_list:
    if min > abs(k - item):
        min = abs(k - item)
        result = item
print(result)