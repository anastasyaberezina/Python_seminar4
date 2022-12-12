# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) 
# многочлена и записать в файл многочлен степени k(до 6 степени).

from random import randint
 
k = int(input('Введите натуральную степень k: '))
 
def work_file(st):
    with open('fileforHW3.txt', 'w') as data:
        data.write(st)
 
def rund_lst(k):
    lst = []
    for i in range(k):
        lst.append(randint(-100, 101))    
    print(lst)
    return lst
    
def res(sp):
    lst2 = sp[::]
    str = ''
    if len(lst2) < 1:
        str = 'x = 0'
    else:
        for i in range(len(lst2)):
            if i != len(lst2) - 1 and lst2[i] != 0 and i != len(lst2) - 2:
                str += f'{lst2[i]}x^{len(lst2) - i - 1}'
                if lst2 [i + 1] != 0:
                    str += ' + '
            elif i == len(lst2) - 2 and lst2[i] != 0:
                str += f'{lst2[i]}x'
                if lst2[i + 1] != 0:
                    str += ' + '
            elif i == len(lst2) - 1 and lst2[i] != 0:
                str += f'{lst2[i]} = 0'
            elif i == len(lst2) - 1 and lst2[i] == 0:
                str += ' = 0'
    return str
 
numb = rund_lst(k)
work_file(res(numb))
