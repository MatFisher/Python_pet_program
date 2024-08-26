# Напишите функцию, которая принимает одно число и проверяет, 
# является ли оно простым. 

def prime(n):
    i = 2
    flag = True
    while i < n and flag:
        if n % i == 0:
            flag = False
        i += 1
    if flag:
        return 'yes'
    return 'no'

n = int(input())
print(prime(n))