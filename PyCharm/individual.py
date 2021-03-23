from math import sqrt

a = int(input('Enter first number: '))
b = int(input('Enter second number: '))
c1 = (abs(a) + abs(b)) / 2
c2 = sqrt(a*b)

print('Результат арифмитеческой прогрессии: ', c1)
print('Результат геометрической прогрессии', c2)

