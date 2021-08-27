# Demonstrate multithreading.
# Name: Yashas H Majmudar     Enrollment Number: IU1941230066


import threading


def thread1():
    for i in range(100):
        print('This is Thread 1')


def thread2():
    for i in range(100):
        print('This is Thread 2')


if __name__ == '__main__':
    t1 = threading.Thread(target=thread1, name='thread 1')
    t2 = threading.Thread(target=thread2, name='thread 2')

    t1.start()
    t2.start()

    t1.join()
    t2.join()
