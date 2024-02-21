'''queue=[]
def enqueue():
    queue.append("mahabub")
    queue.append("alam")
    queue.append("bishal")
Enqueue=enqueue()
print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        print(queue.pop(0))


Dequeue=dequeue()
print(queue)


def display():
    print(queue)

Display=display()'''


class Queue:
    def __init__(self):
        self.data=[]
    def enqueue(self,item):
        self.data.append(item)
    def dequeue(self):
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.data==[]
queue=Queue()
queue.enqueue("mahabub")
queue.enqueue("alam")
queue.enqueue("bishal")
print(queue)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.size())
print(queue.isEmpty())



class Queue:
    def __init__(self):
        self.data=[]
    def enqueue(self,item):
        self.data.append(item)
    def dequeue(self):
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.data==[]




class Queue:
    def __init__(self):
        self.data=[]
    def enqueue(self,item):
        self.data.append(item)
    def dequeue(self):
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.data==[]




class Queue:
    def __init__(self):
        self.data=[]
    def enqueue(self,item):
        self.data.append(item)
    def dequeue(self):
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.data==[]


class Queue:
    def __init__(self):
        self.data=[]
    def enqueue(self,item):
        self.data.append(item)
    def dequeue(self):
        return self.data.pop(0)
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return self.data==[]






