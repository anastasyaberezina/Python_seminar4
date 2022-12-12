# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst=['1', '10', '7', '28', '500']
lst2=['1', '28']
list_res=lst+lst2
list_result=''
for i in range(len(list_res)):
    if list_res[i] not in lst2:
        list_result=list_res[i]
        print(list_result, end = ' ')

    