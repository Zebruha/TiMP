from random import randint

n=10
a=[0]*n #Создаёт массив размерности n
for i in range (len(a)-1):
 a[i]=randint(1,10) #Заполняет массив рандомными числами
a = sorted(a) #Сортирует элементы массива в порядке возрастания для лучшей наглядности
print("Исходный массив", a)

for i in reversed(range(len(a)-1)):
    if a[i] in a[i+1:]:
        a.pop(i)
a=sorted(a)
print("Новый массив", a)




