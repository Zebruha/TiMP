print("Найти косинус минимального из 4 заданных чисел")
from math import cos
a=int(input("Введите первое число: "))
b=int(input("Введите второе число: "))
c=int(input("Введите третье число: "))
d=int(input("Введите четвертое число: "))
minimum = min(a, b, c, d) #Функция поиска минимального значения
print("\n" + "Минимальное число из введенных:", minimum)
print("Косинус минимального числа равен равен:", cos(minimum)) #Аргумент задается в радианах