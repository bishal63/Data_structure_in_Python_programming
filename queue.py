'''queue a list item implement kori'''

'''queue=[]
queue.append('mahabub')
queue.append('alam')
queue.append('bishal')
print(str(queue))
print(str(queue.pop(0)))
print(queue)'''

'''object oriented programming babohar kore queue te data implement kori'''

class Queue:
    def __init__(self):
        self.item=[]
    def __len__(self):
        return len(self.item)
    def __str__(self):
        return str(self.item)
    def enque(self,new_items):
        self.item.append(new_items)
    def deque(self):
        if len(self.item)==0:
            return "queue is empty"
        return self.item.pop(0)
    def peek(self):
        return self.item[0]
    def tail(self):
        return self.item[-1]
    def size(self):
        return len(self.item)
    def is_empty(self):
        return len(self.item)==0
queue=Queue()
print(queue)
queue.enque("mahabub")
queue.enque('alam')
queue.enque('bishal')
print(queue)
print(queue.deque())
print(queue)
print(queue.peek())
print(queue)
print(queue.tail())
print(queue)
print(queue.size())
print(queue)
print(queue.is_empty())
print(queue)