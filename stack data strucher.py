#stack a muloto six dhoroner operation kora hoy
'''class stack:      #stack class create korlam
    def __init__(self):    #constractor create korlam
        self.data=[ ]      #properties hisabe data nilam(data hisabe list rakhi
    def push(self,item):   #push method toiri korlam(item add korar jonno)
        self.data.append(item)
    def pop(self):         #pop method toiri korlam(item sesh theke badh dewar jonno)
        if (len(self.data)):
            return self.data.pop()
        else:
            return "pop failed"
    def size(self):     #stack a koiti item use hoyeche ta dekhar jonno size method toiri korlam
        return len(self.data)
    def isEmpty(self):   #stack a kono item use hoyeche kina ta dekhar jonno isempty method toiri korlam
        return len(self.data)==0    #kono item use na hole true ar use hole false return korbe
    def topElement(self):        #stack a first item ti newar ba dekhar jonno topElement method toiri korlam
        if (len(self.data)):
            return self.data[0]
        else:
            return "stack is empty"
    def tailElement(self):       #stack a sesher item ti newar ba dekhar jonno tailElement method toiri korlam
        if (len(self.data)):
            return self.data[-1]
        else:
            return "stack is empty"'''


#stack operation
'''class stack:
    def __init__(self):
        self.data=[ ]
    def push(self,item):   #first operation
        self.data.append(item)
    def pop(self):    #secend operation    
        if len(self.data):
            return self.data.pop()
        else:
            return "pop failed"
    def size(self):      #third operation
        return len(self.data)
    def isEmpty(self):      #fourth operation
        return len(self.data)==0
    def topElement(self):      #fifth operation
        if (len(self.data)):
            return self.data[0]
        else:
            return "stack is empty"
    def tailElement(self):     #sixth operation
        if (len(self.data)):
            return self.data[-1]
        else:
            return "stack is empty"'''



#stack data strucher operation exercise
'''class stack:
    def __init__(self):
        self.data=[ ]
    def push(self,item):
        self.data.append(item)
    def pop(self):
        if (len(self.data)):
            return self.data.pop()
        else "pop failed"
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return len(self.data)==0
    def topElement(self):
        if (len(self.data)):
            return self.data[0]
        else:
            return "stack is empty"
    def tailElement(self):
        if (len(self.data)):
            return self.data[-1]
        else:
            return "stack is empty"'''



#stack data strucher
class Stack:
    def __init__(self):
        self.data=[]
    def push(self,item):
        self.data.append(item)
    def pop(self):
        if (len(self.data)):
            return self.data.pop()
        else:
            return "pop failed"
    def size(self):
        return len(self.data)
    def isEmpty(self):
        return len(self.data)==0
    def topElement(self):
        if (len(self.data)):
            return self.data[0]
        else:
            return "stack is empty"
    def tailElement(self):
        if len(self.data):
            return self.data[-1]
        else:
            return "stack is empty"
stack=Stack()
stack.push("mahabub")
'''stack.push("alam")
stack.push("bishal")
print(stack.pop())
print(stack.size())
print(stack.isEmpty())
print(stack.size())
print(stack.topElement())
print(stack.tailElement())'''















