# Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def Mult(num):       # Раскладываем числа на простые множители
    multipliers = []
    d = 2            # Делитель
    while num>1:
        while num%d == 0:
            multipliers.append(d)
            num//=d
        d+=1  
    return multipliers

a, b = 18, 48
mult_a = Mult(a)
mult_b = Mult(b)

print(mult_a)    
print(mult_b)   

res=1 # Перемножаем множители
for i in set(mult_a).intersection(set(mult_a)):
    res*=i
print(res) 