# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами

lst = '-5x^2 - 7x + 3 = 0'
lst2 = lst.split(' = ')[0] # Разделяем на 2 части
# a, b, c = lst2.split(' + ') # Разделяем на 3 части
a, lit1, b, lit2, c = lst2.split()
b = lit1 + b
c = lit2 + c
a = int(a[:a.index('x')]) # С помощью срезов по индексам вытаскиваем цифры
b = int(b[:b.index('x')])
c = int(c)
D = b*b - 4*a*c # Ищем дискриминант
if D<0:
    print('Корней нет ')
elif D == 0: 
    print(f'x={-b/(2*a)}')
else:
    print(f'x1={round((-b+D**0.5)/(2*a), 2)}, x2={round((-b-D**0.5)/(2*a), 2)}')    