from threading import Thread, Condition
from queue import Queue
import time
import random

MAX_BUFFER = 5000

# condition = Condition()
# list_queue = []
q = Queue(MAX_BUFFER)

class ProducerThread(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id
    def run(self):
        while True:
            # condition.acquire()
            # if len(list_queue) == MAX_BUFFER:
                # print("Buffer full")
                # condition.wait()
            
            data = self.create_data()
            q.put(data)
            print("PRThread[%d] Produced[%d]: " % (self.id,data), list(q.queue))
            
            # list_queue.append(data)
            # condition.notify()
            # condition.release()
            
            # (3) Producer will need certain time(1~15sec) to produce the resource.
            time.sleep(random.randint(1,15))
    
    # (2) Produced data is random integer between 1~99.
    def create_data(self):
        return random.randint(1,99)

class ConsumerThread(Thread):
    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        while True:

            # (5)
            # condition.acquire()
            # if len(list_queue) < 1:
            #     print("Thread[%d]: Buffer Empty" % self.id)
            #     condition.wait()
            #     print("Thread[%d]: Woke up" % self.id)
            # data = list_queue.pop(0)
            
            # (4)
            data = q.get()
            print("CSThread[%d] Consumed[%d]: " % (self.id, data), list(q.queue))

            # condition.notify()
            # condition.release()

            # I assumed that consumer need 3sec to use the resource.
            time.sleep(3)

pr_threads = []
cs_threads = []
threads = []
# Five Producer
for i in range(1,6):
    # pr_threads.append(ProducerThread())
    threads.append(ProducerThread(i))
for i in range(1,3):
    threads.append(ConsumerThread(i))
# for th in pr_threads:
#     th.start()
# for th in pr_threads:
#     th.join()
for th in threads:
    th.start()
for th in threads:
    th.join()

# Two Consumer
# for i in range(1,3):
#     cs_threads.append(ConsumerThread(i))
# for th in cs_threads:
#     th.start()
# for th in cs_threads:
#     th.join()

print("<End>")