class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add_end(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        lastdata=self.head
        while lastdata.next:
            lastdata=lastdata.next
        lastdata.next=newnode
linkedlist=Linkedlist()
linkedlist.head=Node(20)
second=Node(30)
third=Node(40)
linkedlist.head.next=second
second.next=third
linkedlist.add_end(50)
while linkedlist.head is not None:
    print(linkedlist.head.data,end=" ")
    linkedlist.head=linkedlist.head.next


'''def add_end(self,newitem):
    new_node=Node(newitem)
    if self.head is None:
        self.head=new_node
        return 
    lastitem=self.head
    while lastitem.next:
        lastitem=lastitem.next
    lastitem.next=new_node'''