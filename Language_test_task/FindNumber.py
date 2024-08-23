s = int(input('Введите сумму чисел: '))
p = int(input('Введите произведение чисел: '))

for x in range(1, 1001):
    y = s -x
    if x <= y and x * y == p:
        print(x, y)

