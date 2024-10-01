import threading
import time

lock = threading.Lock()

class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemy = 100
        days = 0

        print(f'{self.name}, на нас напали!')

        while True:
            with lock:
                if enemy <= 0:
                    break

                days += 1
                m_enemy = min(self.power, enemy)
                enemy -= m_enemy

            print(f"{self.name} сражается {days} день(дня)..., осталось {enemy} воинов.")

            time.sleep(1)

        print(f"{self.name} одержал победу спустя {days} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()


print("Все битвы закончились!")