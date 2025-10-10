from multiprocessing import Process
import time
def y(x):

    for i in range(5000000):
        a = i

def _y_one():
    print('Начало')
    start = time.time()
    for i in range(10000000):
        a = i
    print(f'Заверщено за время {time.time() - start}')
_y_one()

def main():
    print('Начало')
    start = time.time()
    p_1 = Process(target=y, args=(1,))
    p_2 = Process(target=y, args=(2,))

    p_1.start()
    p_2.start()

    p_1.join()
    p_2.join()
    print(f'Заверщено за время {time.time() - start}')

if __name__ == '__main__':
    main()