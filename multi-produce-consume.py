from threading import Thread, Condition
import time
import random

queue = []
condition = Condition()

MAX_BUFFER = 5

class ProducerThread(Thread):
    i = 0

    def run(self):
        global queue

        while True:
            # Access to shared resource and lock.
            condition.acquire()
            # Queue is full
            if len(queue) == MAX_BUFFER:
                print("Wait for consumer: Buffer Full: ",queue)
                # Wait for other notification.
                condition.wait()
            num = self.next_id()
            print("Produced: ", queue)
            queue.append(num)
            # Notify other threads that resource is ready.
            condition.notify()
            # Release the lock for shared resource.
            condition.release()
            # Producer take random time(1~3) to produce the resource.
            time.sleep(random.randint(1,3))

    def next_id(self):
        self.i += 1
        return self.i

class ConsumerThread(Thread):

    def run(self):
        global queue
        while True:
            condition.acquire()
            if not queue:
                print("Wait for producer: Buffer Empty: ",queue)
                condition.wait()
            num = queue.pop(0)

            print("Consumed: ",num)
            condition.notify()
            condition.release()
            # Consumer take random time(1~5) to consume the resource.
            time.sleep(random.randint(1,5))

ct = ConsumerThread()
pt = ProducerThread()
ct.start()
pt.start()