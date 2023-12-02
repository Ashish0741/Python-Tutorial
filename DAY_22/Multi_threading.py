
# Multithreading :

# It is mostly used in gaming domain

# process : software (paint)
# thread : atomic job or unit job also known as process

# There are three ways to achieve :

# 1. with function 
# 2. with class
# 3. with class with inheritance (standard way)

# In overall program there are 3 threads : 
# 1. user defined thread
# 2. main thread
# 3. daemon thread (background activities)

from threading import *


# With class with inheritance (standard way) :

# class MyThreadClass(Thread):
#     # Thread class have run method w/o body we need to overwrite and add our logic
#     def run(self):
#         for i in range(500):
#             print(i)

# # main thread --> to create user defined threads
# if __name__ == "__main__":
#     t1 = MyThreadClass()
#     # t1.run()   # we can't call run method directly
#     t1.start()  # start method is used to call run method
#     t2 = MyThreadClass()
#     t2.start()


# ------------------------------------------------------------

# With class :

# class MyThreadClass:
#     def show(self):
#         for i in range(500):
#             print("UDI")

# if __name__ == "__main__":
#     obj = MyThreadClass()
#     t1 = Thread(target=obj.show)
#     t1.start()

#     for i in range(500):   # this is main thread
#         print("MT")

# -------------------------------------------------------------

# With function :

# def thread_func():
#     for i in range(500):
#         print("UDI")

# if __name__ == "__main__":
#     t1 = Thread(target=thread_func)
#     t1.start()

#     for i in range(500):
#         print("MT")

# ---------------------------------------------------------------

# sleep method --> it show time in seconds

# from time import sleep

# def thread_func():
#     for i in range(500):
#         sleep(5)
#         print("UDI")

# if __name__ == "__main__":
#     t1 = Thread(target=thread_func)
#     t1.start()

#     for i in range(500):
#         print("MT")

# ---------------------------------------------------------------

# join method : this will help to join other thread when current task is done


# def thread_func():
#     for i in range(500):
#         print(i)

# if __name__ == "__main__":
#     t1 = Thread(target=thread_func)
#     t2 = Thread(target=thread_func)
#     t3 = Thread(target=thread_func)
#     t1.start()
#     t1.join()  # this will join t2 and t3 after completion of t1
#     t2.start()
#     t3.start()

# ---------------------------------------------------------------

# Asynchronous :

# class Laptop:
#     def pycharm(self,name):
#         for access in range(50):
#             print(name)

# class Ashish(Thread):
#     def __init__(self, lap, name):
#         super().__init__()
#         self.lap = lap
#         self.name = name

#     def run(self):
#         self.lap.pycharm(self.name)

# class Shivani(Thread):
#     def __init__(self, lap, name):
#         super().__init__()
#         self.lap = lap
#         self.name = name

#     def run(self):
#         self.lap.pycharm(self.name)


# if __name__ == "__main__":
#     laptop = Laptop()
#     ashish = Ashish(laptop,"Ashish")
#     shivani = Shivani(laptop,"Shivani")

#     ashish.start()
#     # ashish.join()
#     shivani.start()

# --------------------------------------------------------

# Time comparison :

import time

# without thread :

# def job():
#     for i in range(200000):
#         print(i/2)

# def other_job():
#     for i in range(200000):
#         print(i/10)

# start_time = time.time()

# job()
# other_job()
# end_time = time.time()

# print(end_time - start_time)  # total_time = 1.6002380847930908

# ------------------------------------------------------------------

# with thread :

# def job():
#     for i in range(200000):
#         print(i/2)

# def other_job():
#     for i in range(200000):
#         print(i/10)

# start_time = time.time()

# t1 = Thread(target=job())
# t2 = Thread(target=other_job())

# t1.start()
# t2.start()

# end_time = time.time()

# print(end_time - start_time)  # total_time = 1.7342050075531006


# --------------------------------------------------------------------------

# Race condition , synchronization, locks :

# code w/o synchronization :

# import threading

# x = 0

# def thread_task():
#     global x
#     for i in range(100000):
#         x += 1

# def main_task():
#     t1 = threading.Thread(target=thread_task)
#     t2 = threading.Thread(target=thread_task)

#     t1.start()
#     t2.start()

#     # t1.join()
#     # t2.join()

# if __name__ == "__main__":
#     main_task()
#     print("{0}".format(x))


# ------------------------------------------------------------------------

# code with synchronization :


x = 0

def laptop(lock):
    global x
    lock.acquire()
    for i in range(100000):
        x += 1
    lock.release()

def main_task():
    lock = Lock()
    t1 = Thread(target=laptop, args=(lock,))
    t2 = Thread(target=laptop,args=(lock,))

    t1.start()
    t2.start()

    # t1.join()
    # t2.join()

if __name__ == "__main__":
    main_task()
    print("{0}".format(x))














