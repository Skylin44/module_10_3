import threading
import time
import random

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            self.lock.acquire()
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += amount
            print(f'Пополнение: {amount}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на {amount}')
            if amount <= self.balance:
                self.lock.acquire()
                self.balance -= amount
                print(f'Снятие: {amount}. Баланс: {self.balance}')
                self.lock.release()
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
                self.lock.release()
            time.sleep(0.001)

bk = Bank()
th1 = threading.Thread(target=bk.deposit)
th2 = threading.Thread(target=bk.take)

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

