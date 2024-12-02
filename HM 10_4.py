from threading import Thread
from time import sleep
from random import randint
from queue import Queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))


class Cafe:
    def __init__(self, *tables):
        self.queue = Queue()
        self.tables = tables

    def guest_arrival(self, *guests):
        for guest in guests:  # добавляем в очередь гостей
            examination = False
            for table in self.tables:  # перебираем все столы в очереди
                if table.guest is None:  # если стол свободен
                    table.guest = guest  # сажаем гостя за стол
                    guest.start()  # запускаем гостя в отдельном потоке
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    examination = True
                    break
            if not examination:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        while (not self.queue.empty()  # проверяет пуст ли стек
               or any(table.guest is not None for table in self.tables)):
            for table in self.tables:
                if table.guest is not None:
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        print(f"Стол номер {table.number} свободен")
                        table.guest = None

                        if not self.queue.empty():
                            next_guest = self.queue.get()
                            table.guest = next_guest
                            next_guest.start()
                            print(f"{next_guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
                'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
                ]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столиками
cafe = Cafe(*tables)
# Прием гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
