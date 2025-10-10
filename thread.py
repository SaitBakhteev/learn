from threading import Thread
import time

def thread_task(n):  # задача для потоков
    print(f'Начинает выполняться поток №{n}')
    time.sleep(5)  #имитация i/o-bound операции
    print(f'Поток №{n} закончил работу')

# Инициируем потоки
t_1 = Thread(target=thread_task, args=(1,))
t_2 = Thread(target=thread_task, args=(2,))  # инициируем поток #2

start = time
# Начало работы потоков
t_1.start()
t_2.start()

# Установка на то, чтобы главный поток ожидал завершения работы рабочих потоков
# Начало работы потоков
t_1.join()
t_2.join()

print('Все потоки завершили свою работу')



