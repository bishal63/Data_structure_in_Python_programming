class Node:
    def __init__(self,item):
        self.item=item
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def add_end(self,newdata):
        newnode=Node(newdata)
        if self.head is None:
            self.head=newnode
            return
        lastitem=self.head
        while lastitem.next:
            lastitem=lastitem.next
        lastitem.next=newnode
linkedlist=Linkedlist()
linkedlist.head=Node("mahabub")
second=Node("alam")
third=Node("bishal")
linkedlist.head.next=second
second.next=third
linkedlist.add_end("hridita")
while linkedlist.head is not None:
    print(linkedlist.head.item,end=" ")
    linkedlist.head=linkedlist.head.next


'''def add_end(self,newdata):
    newnode=Node(newdata)
    if self.head is None:
        self.head=newnode
        return
    lastdata=self.head
    while lastdata.next:
        lastdata=lastdata.next
    lastdata.next=newnode'''