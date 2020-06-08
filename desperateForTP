"""
You've just received intel that your local market has received a huge
shipment of toilet paper! In desperate need, you rush out to the store.
Upon arrival, you discover that there is an enormously large line of
people waiting to get in to the store. You step into the queue and start
to wait. While you wait, you being to think about data structures and come
up with a challenge to keep you busy. Your mission: create a queue data
structure. Remember, queues are FIFO - first in first out - in nature.
Your queue should be a class that has the methods "add" and "remove".
Adding to the queue should store an element until it is removed.

"""

class queue():
    def __init__(self):
        self.items = []
        
    def add(self, item):
        self.items.insert(0,item)

    def remove(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


newQueue = queue()
newQueue.add(35)
newQueue.add(10)
print(newQueue.size())
newQueue.remove()
print(newQueue.size())
