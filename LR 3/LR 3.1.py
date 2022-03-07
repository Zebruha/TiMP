fio = input("Ваши фамилия, имя, отчество? ")
mfio = input("Фамилия, имя, отчество Вашей мамы? ")
ofio = input("Фамилия, имя, отчество Вашего отца? ")
def main(): #Проверка на корректность ввода данных
   while True:
        try:
            age = int(input("Ваш возраст? "))
            if age <= 0:
                raise ValueError
            return age
        except ValueError:
            print("Вы должны ввести неторицательное число")
age = main()
place = input("Где вы Живете? ")
print("\n" + "Ваши фамилия, имя, отчество: ", fio)
print("Вашу маму зовут:", mfio)
print("Вашего отца зовут:", ofio)
print("Ваш возраст:", age)
print("Ваше место жительства:", place)
