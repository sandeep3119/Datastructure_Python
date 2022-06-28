class queue:
    def __init__(self,initialVal=[]):
        self.queue=initialVal
    def enqueue(self,element):
        self.queue.append(element)
        return self.queue
    def dequeue(self):
        return self.queue.pop(0)
    def printQueue(self):
        return self.queue
    def tail(self):
        return self.queue[-1]
    def head(self):
        return self.queue[0]
