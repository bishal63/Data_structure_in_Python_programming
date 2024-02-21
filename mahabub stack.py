'''stack=[]
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop(-1))
print(stack)
print(stack.pop(0))
print(stack)
print(len(stack))
print(stack)'''

class Stack:
    def __init__(self):
        self.items=[]
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return str(self.items)
    def push(self,new_item):
        self.items.append(new_item)
    def pop(self):
        if len(self.items)==0:
            return "stack is empty"
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def tail(self):
        return self.items[0]
    def size(self):
        return len(self.items)
    def is_empty(self):
        return len(self.items)==0

stack=Stack()
print(stack)
stack.push(10)
stack.push(20)
stack.push(30)
print(stack)
print(stack.pop())
print(stack)
print(stack.peek())
print(stack)
print(stack.tail())
print(stack)
print(stack.size())
print(stack)
print(stack.is_empty())
print(stack)