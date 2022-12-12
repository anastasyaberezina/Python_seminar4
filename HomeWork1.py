# Вычислить число ПИ c заданной точностью d.  - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10

import math

number_pi = float(math.pi)
d=int(input('Введите нужное кол-во цифр: '))
d=d+2
print(str(number_pi)[:d])









