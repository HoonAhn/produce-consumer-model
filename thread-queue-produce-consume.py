from threading import Thread, Condition
from queue import Queue
import time
import random

list_queue = []
condition = Condition()
MAX_BUFFER = 10
i = 0
q = Queue(100)

# P-C model using list as queue
class ProducerThread(Thread):
    def run(self):
        global list_queue, i
        for i in range(10):
            condition.acquire()
            i += 1
            list_queue.append(i)
            condition.notify()
            condition.release()
            time.sleep(2)

class ConsumerThread(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        global list_queue, i

        for i in range(5):
            condition.acquire()
            while len(list_queue) < 1:
                print("Consumer[%d] waiting..." % self.id)
                condition.wait()
            print("Consumer[%d] -> Resource[%d]" % (self.id, list_queue.pop(0)))
            condition.release()
            time.sleep(1)

# threads = []

# for i in range(10):
#     threads.append(ConsumerThread(i))
# for i in range(10):
#     threads.append(ProducerThread())

# for th in threads:
#     th.start()

# for th in threads:
#     th.join()

# print("<End>")

# P-C model using python Queue
class ProducerThread2(Thread):
    def run(self):
        global q, i
        for i in range(10):
            i += 1
            q.put(i)
            time.sleep(2)

class ConsumerThread2(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        global q, i
        for i in range(5):
            print("Consumer[%d] -> Resource[%d]" % (self.id, q.get()))
            time.sleep(1)

threads = []

for i in range(10):
    threads.append(ConsumerThread2(i))
for i in range(10):
    threads.append(ProducerThread2())

for th in threads:
    th.start()

for th in threads:
    th.join()

print("<End>")