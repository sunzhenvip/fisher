"""
 Created by sz on 2021/2/6
"""
__author__ = 'sz'

import threading
import time


def worker1():
    print('i am thread')
    t = threading.current_thread()
    print(t.getName())


def worker2():
    print('i am thread')
    t = threading.current_thread()
    time.sleep(2)
    print(t.getName())


new_t = threading.Thread(target=worker1)
new_t.start()

new_t = threading.Thread(target=worker2)
new_t.start()

t = threading.current_thread()
print(t.getName())
