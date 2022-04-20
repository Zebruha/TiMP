import math

class Calculator:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.action()
        self.again()

    def action(self):
        # Выводим сообщение какие действия есть
        print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"  
              "Квадратный корень: sq\n"
              "Возведение в степень: ^\n"
              "Синус: sin\n"
              "Синус: cos\n"
              )
        # Переменная для хранения действия
        action = self.check_action()
        # Если action равен +, -, *, /, то
        if action in ('+', '-', '*', '/'):
            self.a = self.check_value()
            self.b = self.check_value()
            # Если action равен + то
            if action == '+':
                self.addition()
            # Если action равен - то
            elif action == '-':
                self.subtraction()
            # Если action равен * то
            elif action == '*':
                self.multiplication()
            # Если action равен / то
            elif action == '/':
                self.division()

        if action in ('sq', '^', 'sin', 'cos'):
            self.a = self.check_value()
            if action == 'sq':
                self.square_root()
            if action == '^':
                self.n = self.check_value()
                self.exponentiation()
            if action == 'sin':
                self.sin()
            if action == 'cos':
                self.cos()

    def check_action(self):  # Проверка на корректность ввода действия
        while True:
            try:
                self.act = input("Действие: ")
                if self.act in ('+', '-', '*', '/', 'sq', '^', 'sin', 'cos'):
                    return self.act
                raise ValueError
            except ValueError:
                print("Вы должны ввести действие из предложенного списка")

    def check_value(self):  # Проверка на корректность ввода значения
        while True:
            try:
                if self.act in ('+', '-', '*', '/'):
                    if self.a == 0:
                        self.a = float(input("\nВведите первое число: "))
                        return self.a
                    else:
                        self.b = float(input("Введите второе число: "))
                        if self.b == 0:
                            raise ValueError
                        return self.b
                if self.act in ('sq', '^', 'sin', 'cos'):
                    if self.act == '^':
                        if self.a == 0:
                            self.a = float(input("\nВведите число: "))
                            return self.a
                        else:
                            self.n = float(input("Введите степень: "))
                            return self.n
                    self.a = float(input("\nВведите число: "))
                    if self.act == 'sq':
                        if self.a <= 0:
                            raise ValueError
                        return self.a
                    return self.a
            except ValueError:
                print("Некорректный ввод")

    def again(self):
        calc_again = input("\nВы хотите снова произвести вычисления? Пожалуйста, введите Y для ответа ДА или N для ответа НЕТ: \n")
        # Если пользователь вводит Y, программа запускает функцию Calculator()
        if calc_again == 'Y':
            Calculator()
        # Если пользователь вводит N, программа попрощается и завершит работу
        elif calc_again == 'N' or calc_again == 'n':
            print('Выход из программы.')
    # Если пользователь вводит другой символ, программа снова запускает функцию again()
        else:
            Calculator()

    def addition(self):
        add = self.a + self.b
        print("Результат: ", add)

    def subtraction(self):
        subst = self.a - self.b
        print("Результат: ", subst)

    def multiplication(self):
        mult = self.a * self.b
        print("Результат: ", mult)

    def division(self):
        div = self.a / self.b
        print("Результат: ", div)

    def square_root(self):
        sqrt = math.sqrt(self.a)
        print("Результат: ", sqrt)

    def exponentiation(self):
        b = math.pow(self.a, self.n)
        print("Результат: ", b)

    def sin(self):
        b = math.sin(self.a)
        print("Результат: ", b)

    def cos(self):
        b = math.cos(self.a)
        print("Результат: ", b)

pr = Calculator()

