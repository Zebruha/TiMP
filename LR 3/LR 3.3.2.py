N = int(input("Введите число N: "))
K = 0
while N > 1:
    N //= 2
    K += 1
print("\n" + "Показатель степени K:", K)