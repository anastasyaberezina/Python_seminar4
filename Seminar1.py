# Задайте строку из набора чисел. 
# Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

number = '3 9 15 4 67'
number=number.split()

for i in range(len(number)):
    number[i]=int(number[i])
print(min(number), max(number))   
