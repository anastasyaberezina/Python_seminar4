# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open('file1.txt', "r") as file_one:
    lst1=file_one.readline()
    lst1=lst1.split('=')[0]
    print(lst1)
with open('file2.txt', "r") as file_second:
    lst2=file_second.readline()
    lst2=lst2.split('=')[0]
    print(lst2)

a, b, c    = lst1.split('+')
a = int(a[:a.index('*x')])
b=int(b[:b.index('*x')])
c=int(c)

i, j, k = lst2.split('+')
i = int(i[:i.index('*x')])
j=int(j[:j.index('*x')])
k=int(k)

with open('file3.txt', 'w') as file_tree:
    file_tree.write(f'{(a+i)}*x^2+{b+j}*x+{c+k}') # Не знаю, нужно ли степени складывать у многочлена. 
    
