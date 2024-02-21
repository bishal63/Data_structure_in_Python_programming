'''class stack:
    def __init__(self):
        self.data=[]
    def additem(self,item):
        self.data.append(item)
    def pop(self):
        if len(self.data):
            return self.data.pop()
        else:
            return "pop failed"
    def size(self):
        return len(self.data)
    def isempty(self):
        return len(self.data)==0
    def topelement(self):
        if len(self.data):
            return self.data[0]
        else:
            return "top element is empty"
    def tailelement(self):
        if len(self.data):
            return self.data[-1]
        else:
            return "tailelement is empty"

Stack=stack()
Stack.additem("mahabub")
Stack.additem("alam")
Stack.additem("bishal")
print(Stack.pop())
print(Stack.size())
print(Stack.isempty())
print(Stack.topelement())
print(Stack.tailelement())'''

class stack:
    def __init__(self):
        self.data=[]
    def additem(self,item):
        self.data.append(item)
    def deletelastitem(self):
        if len(self.data):
            return self.data.pop()
        else:
            return "empty item"
    def sizeitem(self):
        return len(self.data)==0
    def size(self):
        return len(self.data)
    def firstitem(self):
        if len(self.data):
            return self.data[0]
        else:
            return "empty"
    def lastitem(self):
        if len(self.data):
            return self.data[-1]
        else:
            return "empty"


Stack=stack()
Stack.additem("mahabub")
Stack.additem("alam")
print(Stack.deletelastitem())
print(Stack.sizeitem())
print(Stack.size())
print(Stack.firstitem())
print(Stack.lastitem())



