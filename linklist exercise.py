'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def accesitem(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def addafter(self,prev_node,new_data):
        if prev_node is None:
            print("node must ne linkedlist")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def addend(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node

    def printlinkedlist(self):
        temp=self.head
        while(temp):
            print(str(temp.data)+" ",end="")
            temp=temp.next
if __name__=='__main__':
    llist=Linkedlist()
    llist.accesitem(1)
    llist.accesitem(2)
    llist.addafter(llist.head.next,0)
    llist.addend(4)
    llist.printlinkedlist()'''
'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def addaccess(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def addafteraccess(self,prev_node,new_data):
        if prev_node is None:
            print("node must be linkedlist")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def addenditem(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def printlinkedlist(self):
        temp=self.head
        while(temp):
            print(str(temp.data)+" ",end=" ")
            temp=temp.next
if __name__=='__main__':
    llist=Linkedlist()
    llist.addaccess(1)
    llist.addaccess(2)
    llist.addaccess(3)
    llist.addafteraccess(llist.head.next,4)
    llist.addenditem(5)
    llist.printlinkedlist()'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def access(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def afteraccess(self,prev_node,new_data):
        if prev_node is None:
            print("node must be linkedlist")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def endaccess(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node

    def deletenode(self,position):
        if self.head is None:
            return
        temp=self.head

        if position==0:
            self.head=temp.next
            temp=None
            return

        if i in range(position-1):
            temp=temp.next
            if temp is None:
                break

        if temp is None:
            return

        if temp.next is None:
            return
        next=temp.next.next
        temp.next=None
        temp.next=next

    def printlinkedlist(self):
        temp=self.head
        while(temp):
            print(str(temp.data)+" ",end="")
            temp=temp.next
if __name__=='__main__':
    llist=Linkedlist()
    llist.access(1)
    llist.access(2)
    llist.afteraccess(llist.head.next,3)
    llist.endaccess(4)
    llist.deletenode(1)
    llist.printlinkedlist()

