from tkinter import *
import sqlite3
import datetime
from tkinter.ttk import Combobox
from tkinter import messagebox
from tkinter import ttk

class Main:
    def __init__(self):
        self.window = Tk()
        self.window.title("Фитнес")
        screenWidth = self.window.winfo_screenwidth()  # Получить ширину зоны отображения
        screenHeight = self.window.winfo_screenheight()  # Получить высоту области отображения
        width = 370  # Установить ширину окна
        height = 270  # Установить высоту окна
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.window.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.window.configure(bg='#B4CEB3')

        mainmenu = Menu(self.window)
        self.window.config(menu=mainmenu)
        new_item = Menu(mainmenu, tearoff=0)
        new_item.add_command(label='Тарифы', command=Rates)
        new_item.add_command(label='Отчет', command=self.Report)
        mainmenu.add_cascade(label='Информация', menu=new_item)

        # Кнопка "Создать абонемент"
        ButtonCreateCard = Button(self.window, text="Создать абонемент", background="#546A76", foreground="#FFFFFF",
                                  width=20, height=1, font='Verdana 18', command=self.CreateCard)
        ButtonCreateCard.place(x=30, y=30)

        # Кнопка "Найти абонемент"
        ButtonFindCard = Button(self.window, text="Найти абонемент", background="#546A76", foreground="#FFFFFF",
                                width=20, height=1, font="Verdana 18", command=self.Information)
        ButtonFindCard.place(x=30, y=110)
        self.a = ButtonFindCard.cget('text')

        # Кнопка "Заказ тренировки"
        ButtonOrderWorkout = Button(self.window, text="Заказ тренировки", background="#546A76", foreground="#FFFFFF",
                                    width=20, height=1, font="Verdana 18", command=self.OrderWorkout)
        ButtonOrderWorkout.place(x=30, y=190)
        self.b = ButtonOrderWorkout.cget('text')
        self.window.mainloop()

    def CreateCard(self):
        self.window.destroy()
        CreateCard()

    def OrderWorkout(self):
        self.window.destroy()
        SearchCard(self.b)

    def Information(self):
        self.window.destroy()
        SearchCard(self.a)

    def Report(self):
        table = Report(Tk())
        table.pack(expand=1, fill=BOTH)
        table.mainloop()

# Окно "Создание абонемента"
class CreateCard:
    def __init__(self):
        self.window = Tk()
        self.window.title("Создание абонемента")
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()
        width = 700
        height = 500
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.window.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.window.configure(bg='#FFFFFF')

        self.Title = Label(self.window, text="Создать абонемент", background='#FFFFFF', foreground="#000000",
                           font="Verdana 18")
        self.Title.place(x=225, y=20)

        self.Surname = Label(self.window, text="Фамилия", background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Surname.place(x=40, y=70)
        self.Surname = Entry(self.window, width=23, font="Verdana 14")
        self.Surname.place(x=40, y=105)

        self.Name = Label(self.window, text="Имя", background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Name.place(x=40, y=145)
        self.Name = Entry(self.window, width=23, font="Verdana 14")
        self.Name.place(x=40, y=175)

        self.Patronymic = Label(self.window, text="Отчество", background='#FFFFFF', foreground="#000000",
                                font="Verdana 14")
        self.Patronymic.place(x=40, y=215)
        self.Patronymic = Entry(self.window, width=23, font="Verdana 14")
        self.Patronymic.place(x=40, y=245)

        self.Birthdate = Label(self.window, text="Дата рождения", background='#FFFFFF', foreground="#000000",
                               font="Verdana 14")
        self.Birthdate.place(x=40, y=285)
        self.Birthdate = Entry(self.window, width=23, font="Verdana 14")
        self.Birthdate.place(x=40, y=315)

        self.PhoneNumber = Label(self.window, text="Номер телефона", background='#FFFFFF', foreground="#000000",
                                 font="Verdana 14")
        self.PhoneNumber.place(x=40, y=355)
        self.PhoneNumber = Entry(self.window, width=23, font="Verdana 14")
        self.PhoneNumber.place(x=40, y=385)

        self.CardNumber = Label(self.window, text="№ присваиваемой карты", background='#FFFFFF', foreground="#000000",
                                font="Verdana 14")
        self.CardNumber.place(x=375, y=70)
        self.CardNumber = Entry(self.window, width=23, font="Verdana 14")
        self.CardNumber.place(x=375, y=105)

        self.With = Label(self.window, text="Оформить с", background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.With.place(x=375, y=145)
        self.With = Entry(self.window, width=23, font="Verdana 14")
        self.With.place(x=375, y=175)

        self.By = Label(self.window, text="По", background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.By.place(x=375, y=215)
        self.By = Entry(self.window, width=23, font="Verdana 14")
        self.By.place(x=375, y=245)

        self.Workout = Label(self.window, text="Тариф тренировок", background='#FFFFFF', foreground="#000000",
                             font="Verdana 14")
        self.Workout.place(x=375, y=285)
        self.Workout = Combobox(self.window, width=22, font="Verdana 14", state='readonly')
        self.Workout['values'] = ("Нет", "Разовая тренировка", "5 тренировок", "10 тренировок", "20 тренировок",
                                  "30 тренировок", "Составление программы тренировок")
        self.Workout.current(0)
        self.Workout.place(x=375, y=315)

        ButtonPrintReceipt = Button(self.window, text="Печать чека", background="#B4CEB3", foreground="#2A363C",
                                    width=21, height=1, font="Verdana 16", command=self.PrintReceipt)
        ButtonPrintReceipt.place(x=375, y=425)

        ButtonBack = Button(self.window, text="Назад", background="#546A76", foreground="#FFFFFF", width=21, height=1,
                            font="Verdana 16", command=self.Back)
        ButtonBack.place(x=40, y=425)

        self.window.mainloop()

    def Back(self):
        self.window.destroy()
        Main()

    def PrintReceipt(self):
        if self.Surname.get() == '' or self.Name.get() == '' or self.Patronymic.get() == '' or self.Birthdate.get() == '' or \
                self.PhoneNumber.get() == '' or self.CardNumber.get() == '' or self.With.get() == '' or self.By.get() == '':
            messagebox.showerror("Ошибка ввода", "Не заполнено поле")
        else:
            try:
                connenction = sqlite3.connect("CustomerBase.db")
                cursor = connenction.cursor()
                print("Подключен к SQLite")

                Membership = [(self.Surname.get(), self.Name.get(), self.Patronymic.get(), self.Birthdate.get(),
                               self.PhoneNumber.get(), self.CardNumber.get(), self.With.get(), self.By.get(),
                               self.Workout.get())]
                cursor.executemany('''INSERT INTO Membership VALUES (?, ?, ?, ?, ?, ?, ?, ?,?)''', Membership)
                connenction.commit()
                print("Запись успешно обновлена")
                cursor.close()
            except sqlite3.Error as error:
                print("Ошибка при работе с SQLite", error)
            finally:
                if connenction:
                    connenction.close()
                    num = self.CardNumber.get()
                    print("Соединение с SQLite закрыто")
                    self.window.destroy()
                    PrintReceiptCard(num)

# Окно "Поиск абонемента"
class SearchCard:
    def __init__(self, p):
        root = Tk()
        self.window = root
        self.parametr = p
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()
        width = 300
        height = 200
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.window.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.window.configure(bg='#FFFFFF')
        self.window.title("Ввод карты клиента")

        self.CardNumber = Label(self.window, text="№ присваиваемой карты", background='#FFFFFF', foreground="#000000",
                                font="Verdana 14")
        self.CardNumber.place(x=10, y=20)
        self.CardNumber = Entry(self.window, width=23, font="Verdana 14")
        self.CardNumber.place(x=10, y=50)

        self.BtAddLeave = Button(self.window, text="Поиск карты", background="#B4CEB3", foreground="#2A363C", height=1,
                                 width=15, font=" Verdana 14", command=self.Search)
        self.BtAddLeave.place(x=55, y=90)

        self.BtAddLeave = Button(self.window, text="Назад", background="#546A76", foreground="#FFFFFF", height=1,
                                 width=15, font="Verdana 14", command=self.Back)
        self.BtAddLeave.place(x=55, y=140)

    def Search(self):
        try:
            connenction = sqlite3.connect("CustomerBase.db")
            cursor = connenction.cursor()
            self.t = (self.CardNumber.get(),)
            rowsQuery = cursor.execute("SELECT count(CardNumber) FROM Membership WHERE CardNumber=?", self.t)
            numberOfRows = cursor.fetchone()[0]
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

        finally:
            if connenction:
                if self.parametr == 'Заказ тренировки':
                    if numberOfRows == 1:
                        connenction.close()
                        self.window.destroy()
                        OrderWorkout(self.t)
                    else:
                        messagebox.showerror("Ошибка ввода", "Ошибка в номере карты или такой карты не существует")
                        connenction.close()
                if self.parametr == 'Найти абонемент':
                    if numberOfRows == 1:
                        connenction.close()
                        self.window.destroy()
                        InformationCard(self.t)
                    else:
                        messagebox.showerror("Ошибка ввода", "Ошибка в номере карты или такой карты не существует")
                        connenction.close()

    def Back(self):
        self.window.destroy()
        Main()

# Окно "Заказ тренировки"
class OrderWorkout:
    def __init__(self, num):
        self.window = Tk()
        self.window.title("Заказ тренировки")
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()
        width = 470
        height = 300
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.window.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.window.configure(bg='#FFFFFF')
        self.number = num[0]

        self.Title = Label(self.window, text="Заказ тренировки", background='#FFFFFF', foreground="#000000",
                           font="Verdana 18")
        self.Title.place(x=125, y=20)

        self.CardNumber = Label(self.window, text="№ карты клиента", background='#FFFFFF', foreground="#000000",
                                font="Verdana 14")
        self.CardNumber.place(x=40, y=70)
        self.CardNumber = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.CardNumber['text'] = self.number
        self.CardNumber.place(x=40, y=105)

        self.Workout = Label(self.window, text="Тариф тренировок", background='#FFFFFF', foreground="#000000",
                             font="Verdana 14")
        self.Workout.place(x=40, y=145)
        self.Workout = Combobox(self.window, width=31, font="Verdana 14", state='readonly')
        self.Workout['values'] = ("Разовая тренировка", "5 тренировок", "10 тренировок", "20 тренировок",
                                  "30 тренировок", "Составление программы тренировок")
        self.Workout.current(0)
        self.Workout.place(x=40, y=175)

        ButtonPrintReceipt = Button(self.window, text="Печать чека", background="#B4CEB3", foreground="#2A363C",
                                    width=14, height=1, font="Verdana 16", command=self.PrintReceipt)
        ButtonPrintReceipt.place(x=245, y=225)

        ButtonPrintReceipt = Button(self.window, text="Назад", background="#546A76", foreground="#FFFFFF",
                                    width=14, height=1, font="Verdana 16", command=self.Back)
        ButtonPrintReceipt.place(x=39, y=225)
        self.window.mainloop()

    def Back(self):
        self.window.destroy()
        Main()

    def PrintReceipt(self):
        try:
            connection = sqlite3.connect('CustomerBase.db')
            cursor = connection.cursor()
            print("Подключен к SQLite")
            update = """Update Membership set Workout = ? where CardNumber = ?"""
            data = (self.Workout.get(), self.number)
            cursor.execute(update, data)
            connection.commit()
            print("Запись успешно обновлена")
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)
        finally:
            if connection:
                connection.close()
                print("Соединение с SQLite закрыто")
                self.window.destroy()
                PrintReceiptWorkout(self.number)

# Окно "Информация об абонементе"
class InformationCard:
    def __init__(self, num):
        self.window = Tk()
        self.window.title("Информация об абонементе")
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()
        width = 460
        height = 505
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.window.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.window.configure(bg='#FFFFFF')
        self.number = num[0]

        self.Title = Label(self.window, text="Информация об абонементе", background='#FFFFFF', foreground="#000000",
                           font="Verdana 18")
        self.Title.place(x=50, y=20)

        self.FIO = Label(self.window, text="ФИО", background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.FIO.place(x=40, y=70)
        self.FIO = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.FIO.place(x=40, y=105)

        self.BD = Label(self.window, text="Дата рождения:", background='#FFFFFF', foreground="#000000",
                          font="Verdana 14")
        self.BD.place(x=40, y=145)
        self.BD = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.BD.place(x=40, y=175)

        self.Phone = Label(self.window, text="Номер телефона", background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Phone.place(x=250, y=145)
        self.Phone = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Phone.place(x=250, y=175)

        self.CardNumber = Label(self.window, text="№ карты", background='#FFFFFF', foreground="#000000",
                                font="Verdana 14")
        self.CardNumber.place(x=40, y=215)
        self.CardNumber = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.CardNumber.place(x=40, y=245)

        self.Time = Label(self.window, text="Вид абонемента", background='#FFFFFF', foreground="#000000",
                          font="Verdana 14")
        self.Time.place(x=250, y=215)
        self.Time = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Time.place(x=250, y=245)

        self.With = Label(self.window, text="Действителен с:", background='#FFFFFF', foreground="#000000",
                          font="Verdana 14")
        self.With.place(x=40, y=285)
        self.With = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.With.place(x=40, y=315)

        self.By = Label(self.window, text="По:", background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.By.place(x=250, y=285)
        self.By = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.By.place(x=250, y=315)

        self.Workout = Label(self.window, text="Тариф тренировок:", background='#FFFFFF', foreground="#000000",
                             font="Verdana 14")
        self.Workout.place(x=40, y=355)
        self.Workout = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Workout.place(x=40, y=385)

        ButtonClose = Button(self.window, text="Закрыть", background="#546A76", foreground="#FFFFFF",
                                    width=20, height=1, font="Verdana 16", command=self.close)
        ButtonClose.place(x=100, y=435)

        try:
            sqlite_connection = sqlite3.connect('CustomerBase.db')
            cursor = sqlite_connection.cursor()
            t = (self.number,)
            cursor.execute("SELECT * FROM Membership WHERE CardNumber=?", t)
            mas = cursor.fetchone()
            self.window.Surname = mas[0]
            self.window.Name = mas[1]
            self.window.Patronymic = mas[2]
            self.window.Birthdate = mas[3]
            self.window.PhoneNumber = mas[4]
            self.window.CardNumber = mas[5]
            self.window.With = mas[6]
            self.window.By = mas[7]
            self.window.Workout = mas[8]

            self.CardNumber['text'] = self.window.CardNumber
            self.Time['text']=self.type()
            self.FIO['text'] = self.window.Surname + ' ' + self.window.Name + ' ' + self.window.Patronymic
            self.BD['text'] = self.window.Birthdate
            self.Phone['text']= self.window.PhoneNumber
            self.With['text'] = self.window.With
            self.By['text'] = self.window.By
            self.Workout['text'] = self.window.Workout

            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

        finally:
            if sqlite_connection:
                sqlite_connection.close()

    def close(self):
        self.window.destroy()
        Main()

    def type(self):
        date_time1 = datetime.datetime.strptime(self.window.With, '%d.%m.%Y')
        date_time2 = datetime.datetime.strptime(self.window.By, '%d.%m.%Y')
        t = (date_time2 - date_time1)
        if t == datetime.timedelta(days=1):
            return 'Разовое посещение'
        if datetime.timedelta(days=28) <= t <= datetime.timedelta(days=31):
            return '1 месяц'
        if datetime.timedelta(days=89) <= t <= datetime.timedelta(days=92):
            return '3 месяца'
        if datetime.timedelta(days=181) <= t <= datetime.timedelta(days=184):
            return '6 месяцев'
        if t == datetime.timedelta(days=365) or t == datetime.timedelta(days=366):
            return '12 месяцев'

# Окно "Печать чека"
class PrintReceiptCard:
    def __init__(self, num):
        self.window = Tk()
        self.window.title("Печать чека")
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()
        width = 500
        height = 500
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.window.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.window.configure(bg='#FFFFFF')

        self.Title = Label(self.window, text="Чек", background='#FFFFFF', foreground="#000000",
                           font="Verdana 18")
        self.Title.place(x=220, y=20)

        self.CardNumber = Label(self.window, text="№ карты", background='#FFFFFF', foreground="#000000",
                                font="Verdana 14")
        self.CardNumber.place(x=40, y=70)
        self.CardNumber = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.CardNumber.place(x=40, y=105)

        self.Time = Label(self.window, text="Вид абонемент", background='#FFFFFF', foreground="#000000",
                          font="Verdana 14")
        self.Time.place(x=250, y=70)
        self.Time = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Time.place(x=250, y=105)

        self.FIO = Label(self.window, text="ФИО", background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.FIO.place(x=40, y=145)
        self.FIO = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.FIO.place(x=40, y=175)

        self.With = Label(self.window, text="Действителен с:", background='#FFFFFF', foreground="#000000",
                          font="Verdana 14")
        self.With.place(x=40, y=215)
        self.With = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.With.place(x=40, y=245)

        self.Workout = Label(self.window, text="Тариф тренировок:", background='#FFFFFF', foreground="#000000",
                             font="Verdana 14")
        self.Workout.place(x=40, y=285)

        self.Workout = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Workout.place(x=40, y=315)

        self.By = Label(self.window, text="По:", background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.By.place(x=250, y=215)
        self.By = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.By.place(x=250, y=245)

        self.Total = Label(self.window, text="Итого к оплате:", background='#FFFFFF', foreground="#000000",
                           font="Verdana 14")
        self.Total.place(x=180, y=355)
        self.Total = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Total.place(x=230, y=385)

        ButtonClose = Button(self.window, text="Закрыть", background="#546A76", foreground="#FFFFFF", width=20, height=1,
                             font="Verdana 16", command=self.close)
        ButtonClose.place(x=130, y=425)

        try:
            sqlite_connection = sqlite3.connect('CustomerBase.db')
            cursor = sqlite_connection.cursor()
            t = (num,)
            cursor.execute("SELECT * FROM Membership WHERE CardNumber=?", t)
            mas = cursor.fetchone()
            self.window.Surname = mas[0]
            self.window.Name = mas[1]
            self.window.Patronymic = mas[2]
            self.window.CardNumber = mas[5]
            self.window.With = mas[6]
            self.window.By = mas[7]
            self.window.Workout = mas[8]

            self.CardNumber['text'] = self.window.CardNumber
            self.Time['text'] = self.type()
            self.FIO['text'] = self.window.Surname + ' ' + self.window.Name + ' ' + self.window.Patronymic
            self.With['text'] = self.window.With
            self.By['text'] = self.window.By
            self.Workout['text'] = self.window.Workout
            self.Total['text'] = self.cost()
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

        finally:
            if sqlite_connection:
                sqlite_connection.close()

    def close(self):
        self.window.destroy()
        Main()

    def type(self):
        date_time1 = datetime.datetime.strptime(self.window.With, '%d.%m.%Y')
        date_time2 = datetime.datetime.strptime(self.window.By, '%d.%m.%Y')
        t = (date_time2 - date_time1)
        if t == datetime.timedelta(days=1):
            return 'Разовое посещение'
        if datetime.timedelta(days=28) <= t <= datetime.timedelta(days=31):
            return '1 месяц'
        if datetime.timedelta(days=89) <= t <= datetime.timedelta(days=92):
            return '3 месяца'
        if datetime.timedelta(days=181) <= t <= datetime.timedelta(days=184):
            return '6 месяцев'
        if t == datetime.timedelta(days=365) or t == datetime.timedelta(days=366):
            return '12 месяцев'

    def cost(self):
        if self.type() == 'Разовое посещение':
            if self.window.Workout == 'Нет':
                self.price = 700
            if self.window.Workout == 'Разовая тренировка':
                self.price = 2200
        if self.type() == '1 месяц':
            if self.window.Workout == 'Нет':
                self.price = 4500
            if self.window.Workout == 'Разовая тренировка':
                self.price = 6000
            if self.window.Workout == '5 тренировок':
                self.price = 10500
            if self.window.Workout == '10 тренировок':
                self.price = 13500
            if self.window.Workout == '20 тренировок':
                self.price = 20500
            if self.window.Workout == '30 тренировок':
                self.price = 27500
            if self.window.Workout == 'Составление программы тренировок':
                self.price = 7500
        if self.type() == '3 месяца':
            if self.window.Workout == 'Нет':
                self.price = 5900
            if self.window.Workout == 'Разовая тренировка':
                self.price = 7400
            if self.window.Workout == '5 тренировок':
                self.price = 11900
            if self.window.Workout == '10 тренировок':
                self.price = 14900
            if self.window.Workout == '20 тренировок':
                self.price = 21900
            if self.window.Workout == '30 тренировок':
                self.price = 28500
            if self.window.Workout == 'Составление программы тренировок':
                self.price = 8900
        if self.type() == '6 месяцев':
            if self.window.Workout == 'Нет':
                self.price = 6900
            if self.window.Workout == 'Разовая тренировка':
                self.price = 8400
            if self.window.Workout == '5 тренировок':
                self.price = 12900
            if self.window.Workout == '10 тренировок':
                self.price = 15900
            if self.window.Workout == '20 тренировок':
                self.price = 22900
            if self.window.Workout == '30 тренировок':
                self.price = 29900
            if self.window.Workout == 'Составление программы тренировок':
                self.price = 9900
        if self.type() == '12 месяцев':
            if self.window.Workout == 'Нет':
                self.price = 9900
            if self.window.Workout == 'Разовая тренировка':
                self.price = 11400
            if self.window.Workout == '5 тренировок':
                self.price = 15900
            if self.window.Workout == '10 тренировок':
                self.price = 18900
            if self.window.Workout == '20 тренировок':
                self.price = 25900
            if self.window.Workout == '30 тренировок':
                self.price = 32900
            if self.window.Workout == 'Составление программы тренировок':
                self.price = 12900
        return self.price

# Окно "Печать чека"
class PrintReceiptWorkout:
    def __init__(self, num):
        self.window = Tk()
        self.window.title("Печать чека")
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()
        width = 500
        height = 420
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.window.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.window.configure(bg='#FFFFFF')

        self.Title = Label(self.window, text="Печать чека", background='#FFFFFF', foreground="#000000",
                           font="Verdana 18")
        self.Title.place(x=170, y=20)

        self.CardNumber = Label(self.window, text="№ карты", background='#FFFFFF', foreground="#000000",
                                font="Verdana 14")
        self.CardNumber.place(x=40, y=70)
        self.CardNumber = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.CardNumber.place(x=40, y=105)

        self.Workout = Label(self.window, text="Тариф тренировок:", background='#FFFFFF', foreground="#000000",
                          font="Verdana 14")
        self.Workout.place(x=40, y=145)
        self.Workout = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Workout.place(x=40, y=175)

        self.FIO = Label(self.window, text="ФИО", background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.FIO.place(x=40, y=215)
        self.FIO = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.FIO.place(x=40, y=245)

        self.Total = Label(self.window, text="Итого к оплате:", background='#FFFFFF', foreground="#000000",
                           font="Verdana 14")
        self.Total.place(x=175, y=285)
        self.Total = Label(self.window, background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.Total.place(x=225, y=315)

        ButtonClose = Button(self.window, text="Закрыть", background="#546A76", foreground="#FFFFFF",
                             width=15, height=1, font="Verdana 16", command=self.close)
        ButtonClose.place(x=150, y=355)

        try:
            sqlite_connection = sqlite3.connect('CustomerBase.db')
            cursor = sqlite_connection.cursor()
            t = (num,)
            cursor.execute("SELECT * FROM Membership WHERE CardNumber=?", t)
            mas = cursor.fetchone()
            self.window.Surname = mas[0]
            self.window.Name = mas[1]
            self.window.Patronymic = mas[2]
            self.window.CardNumber = mas[5]
            self.window.Workout = mas[8]

            self.CardNumber['text'] = self.window.CardNumber
            self.FIO['text'] = self.window.Surname + ' ' + self.window.Name + ' ' + self.window.Patronymic
            self.Workout['text'] = self.window.Workout
            self.Total['text'] = self.cost()
            cursor.close()

        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

        finally:
            if sqlite_connection:
                sqlite_connection.close()

    def close(self):
        self.window.destroy()
        Main()

    def cost(self):
        if self.window.Workout == 'Разовая тренировка':
            self.price = 1500
        if self.window.Workout == '5 тренировок':
            self.price = 6000
        if self.window.Workout == '10 тренировок':
            self.price = 9000
        if self.window.Workout == '20 тренировок':
            self.price = 16000
        if self.window.Workout == '30 тренировок':
            self.price = 23000
        if self.window.Workout == 'Составление программы тренировок':
            self.price = 3000
        return self.price

# Окно "Тарифы"
class Rates:
    def __init__(self):
        self.window = Tk()
        self.window.title("Тарифы")
        screenWidth = self.window.winfo_screenwidth()
        screenHeight = self.window.winfo_screenheight()
        width = 900
        height = 250
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        self.window.geometry("%dx%d+%d+%d" % (width, height, left, top))
        self.window.configure(bg='#FFFFFF')

        self.LabH1 = Label(self.window, text='Для абонемента:', background='#FFFFFF', foreground="#000000", font="Verdana 14 bold")
        self.LabH1.place(x=20, y=0)
        self.LabT1 = Label(self.window, text='Разовое посещение – 700 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT1.place(x=20, y=30)
        self.LabT2 = Label(self.window, text='1 месяц – 4500 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT2.place(x=20, y=60)
        self.LabT3 = Label(self.window, text='3 месяца – 5900 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT3.place(x=20, y=90)
        self.LabT4 = Label(self.window, text='6 месяцев – 6900 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT4.place(x=20, y=120)
        self.LabT5 = Label(self.window, text='12 месяцев – 9900 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT5.place(x=20, y=150)

        self.LabH2 = Label(self.window, text='Для тренировок:', background='#FFFFFF', foreground="#000000", font="Verdana 14 bold")
        self.LabH2.place(x=400, y=0)
        self.LabT6 = Label(self.window, text='Нет', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT6.place(x=400, y=30)
        self.LabT7 = Label(self.window, text='Разовая тренировка – 1500 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT7.place(x=400, y=60)
        self.LabT8 = Label(self.window, text='5 тренировок – 6000 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT8.place(x=400, y=90)
        self.LabT9 = Label(self.window, text='10 тренировок  – 9000 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT9.place(x=400, y=120)
        self.LabT10 = Label(self.window, text='20 тренировок – 16000 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT10.place(x=400, y=150)
        self.LabT11 = Label(self.window, text='30 тренировок – 23000 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT11.place(x=400, y=180)
        self.LabT12 = Label(self.window, text='Составление программы тренировок – 3000 р', background='#FFFFFF', foreground="#000000", font="Verdana 14")
        self.LabT12.place(x=400, y=210)

# Окно "История клиентов"
class Report(Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        screenWidth = parent.winfo_screenwidth()
        screenHeight = parent.winfo_screenheight()
        width = 600
        height = 300
        left = (screenWidth - width) / 2
        top = (screenHeight - height) / 2
        parent.geometry("%dx%d+%d+%d" % (width, height, left, top))
        parent.title("История клиентов")

        with sqlite3.connect('CustomerBase.db') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM Membership")
            data = (row for row in cursor.fetchall())
        headings = ('Фамилия', 'Имя', 'Отчество', 'Дата рождения', 'Номер телефона', 'Номер карты', 'Действителен с',
                    'Действителен по', 'Тариф тренировок')
        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"] = headings

        for head in headings:
            table.heading(head, text=head, anchor=CENTER)
            table.column(0, anchor=CENTER, width=100)
            table.column(1, anchor=CENTER, width=80)
            table.column(2, anchor=CENTER, width=100)
            table.column(3, anchor=CENTER, width=100)
            table.column(4, anchor=CENTER, width=110)
            table.column(5, anchor=CENTER, width=90)
            table.column(6, anchor=CENTER, width=110)
            table.column(7, anchor=CENTER, width=110)
            table.column(8, anchor=CENTER, width=240)
        for row in data:
            table.insert('', END, values=tuple(row))

        # scrollbar
        scrolltable_y = Scrollbar(table, orient='vertical')
        scrolltable_x = Scrollbar(table, orient='horizontal')
        table.configure(yscrollcommand=scrolltable_y.set, xscrollcommand=scrolltable_x.set)

        scrolltable_y.pack(side=RIGHT, fill=Y,)
        scrolltable_x.pack(side=BOTTOM, fill=X,)
        scrolltable_x.config(command=table.xview)
        scrolltable_y.config(command=table.yview)
        table.pack(expand=1, fill=BOTH)

if __name__ == '__main__':
    Main()
