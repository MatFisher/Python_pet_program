# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
import random
from random import randint


my_list = []
n = int(input("Введите количество чисел: "))
for i in range(n):
    my_list.append(random.randint(0,10))
print(my_list)

k = int(input("Введите число: "))
result = 0
for item in my_list:
    if k == item:
        result += 1 
if result == 0:
    print("Такого числа нет")
else:
    print(f"Число встречается {result} раз")