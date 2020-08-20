"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
class Queue:
    def __init__(self):
        self.size = 0
        self.queue = []
    
    def __len__(self):
        return len(self.queue)

    def enqueue(self, value):
        self.queue.insert(0, value)

    def dequeue(self):
        if len(self.queue) == 0:
            return
        
        else:
            item = self.queue[len(self.queue) - 1]
            self.queue.remove(item)
            return item

q = Queue()

q.enqueue(5)
q.enqueue(6)
q.enqueue(4)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())