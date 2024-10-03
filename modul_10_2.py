import time
from threading import Thread

class Knight(Thread):
    def __init__(self, name, power,foes=100):
        self.sir_name = name
        self.power = power
        self.foes=foes
        super ().__init__ ()
    def run(self):
        day=0
        print(f'{self.sir_name}, на нас напали!')
        while self.foes>= self.power :
            time.sleep (1)
            day+=1
            self.foes=self.foes-self.power
            print(f'{self.sir_name} сражается {day} день(дня), осталось {self.foes} воинов.')
        print(f'{self.sir_name} одержал победу спустя {day} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print(f'Все битвы закончились!')