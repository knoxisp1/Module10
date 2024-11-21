from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name_, power):
        self.name_ = str(name_)
        self.power = int(power)
        super().__init__()

    def run(self):
        print(f'{self.name_}, на нас напали')
        days = 0
        enemy = 100
        while enemy > 0:
            sleep(1)
            days += 1
            enemy -= self.power
            if enemy < 0:
                enemy = 0
            print(f'{self.name_} сражается {days}..., осталось {enemy} воинов.')
        print(f"{self.name_} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
first_knight.start()
second_knight = Knight("Sir Galahad", 20)
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончены')
