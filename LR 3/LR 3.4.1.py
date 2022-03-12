from random import randint
c=""
n=10
a=[0]*n #Создаёт массив размерности n
for i in range (len(a)-1):
 a[i]=randint(-10, 10) #Заполняет массив рандомными числами
print("Исходный массив", a)

for i in range (len(a)-1):
 if a[i-1]<0 and a[i]<0:
  c=print("\nПара отрицательных чисел, стоящих рядом:", a[i-1], ",", a[i])

if c=="":
 print("Пар c отрицательными числами, стоящими рядом нет")
