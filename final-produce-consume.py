from threading import Thread, Condition
from queue import Queue
import time
import random

condition = Condition()
MAX_BUFFER = 100
id = 0
list_queue = []
q = Queue(MAX_BUFFER)

class ProducerThread(Thread):
    def run(self):
        global list_queue, i
        
        while True:
            # condition.acquire()
            # if len(list_queue) == MAX_BUFFER:
                # print("Buffer full")
                # condition.wait()
            data = self.create_data()
            print("Produced: ", data)
            # list_queue.append(data)
            q.put(data)
            # condition.notify()
            # condition.release()
            time.sleep(random.randint(1,10))
            # print(list_queue)
            print(q.queue)
    
    def create_data(self):
        return random.randint(1,99)

class ConsumerThread(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        global list_queue, i
        while True:
            # condition.acquire()
            # if len(list_queue) < 1:
            #     print("Thread[%d]: Buffer Empty" % self.id)
            #     condition.wait()
            #     print("Thread[%d]: Woke up" % self.id)
            # data = list_queue.pop(0)
            data = q.get()
            print("Thread[%d] Consumed: " % self.id, data)
            # condition.notify()
            # condition.release()
            time.sleep(3)

pr_threads = []

for i in range(5):
    pr_threads.append(ProducerThread())
for th in pr_threads:
    th.start()

con_th_1 = ConsumerThread(1)
con_th_2 = ConsumerThread(2)
con_th_1.start()
con_th_2.start()

print("<End>")