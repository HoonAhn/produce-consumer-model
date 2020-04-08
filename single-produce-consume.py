class Producer:
    def __init__(self):
        self.id = 0

    def produce(self):
        return self.next_id()
    def next_id(self):
        self.id += 1
        return self.id


class Consumer:
    def consume(self, id):
        print("ID: ",id)

p = Producer()
c = Consumer()
result = p.produce()
c.consume(result)