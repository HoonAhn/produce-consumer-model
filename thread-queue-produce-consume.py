from threading import Thread, Condition
import time
import random

queue = []
condition = Condition()
MAX_BUFFER = 5
i = 0

class ProducerThread(Thread):
    def run(self):
        global queue, i
        for i in range(10):
            condition.acquire()
            i += 1
            queue.append(i)
            condition.notify()
            condition.release()
            time.sleep(2)

class ConsumerThread(Thread):

    def __init__(self, id):
        Thread.__init__(self)
        self.id = id

    def run(self):
        global queue, i

        for i in range(5):
            condition.acquire()
            while len(queue) < 1:
                print("Consumer[%d] waiting..." % self.id)
                condition.wait()
            print("Consumer[%d] -> Resource[%d]" % (self.id, queue.pop(0)))
            condition.release()
            time.sleep(1)

threads = []

for i in range(10):
    threads.append(ConsumerThread(i))
for i in range(10):
    threads.append(ProducerThread())

for th in threads:
    th.start()

for th in threads:
    th.join()

print("<End>")