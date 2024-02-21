class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None
    def insertatbeginnig(self,new_data):
        new_node=Node(new_data)

        new_node.next=self.head
        self.head=new_node

    def insertafter(self,prev_node,new_data):
        if prev_node is None:
            print("the given previous node must in linklist")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node

    def insertatend(self,new_data):
        new_node=Node(new_data)

        if self.head is None:
            self.head=new_node
            return

        last=self.head
        while (last.next):
            last=last.next
        last.next=new_node
    def deleteNode(self,posision):
        if self.head is None:
            return
        temp=self.head

        if posision==0:
            self.head=temp.next
            temp=None
            return

        for i in range(posision-1):
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

    def search(self,key):
        current=self.head

        while current is not None:
            if current.data==key:
                return True
            current=current.next
        return False
    def sortLinkedList(self,head):
        current=head
        index=Node(None)

        if head is None:
            return
        else:
            while current is not None:
                index=current.next

                while index is not None:
                    if current.data>index.data:
                        current.data,index.data=index.data,current.data
                    index=index.next
                current=current.next

    def printList(self):
        temp=self.head
        while(temp):
            print(str(temp.data)+" ",end="")
            temp=temp.next

if __name__=='__main__':
    llist=Linkedlist()
    llist.insertatend(1)
    llist.insertatbeginnig(2)
    llist.insertatbeginnig(3)
    llist.insertatend(4)
    llist.insertafter(llist.head.next,5)
    print('linked list:')
    llist.printList()
    print("after deleteing an element:")
    llist.deleteNode(3)
    llist.deleteNode(1)
    llist.deleteNode(0)
    llist.printList()
    print()
    item_to_find=1
    if llist.search(item_to_find):
        print(str(item_to_find)+"is found")
    else:
        print(str(item_to_find)+"is not found")
    llist.sortLinkedList(llist.head)
    print("sorted list:")
    llist.printList()


'''class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linklist:
    def __init__(self):
        self.head=None
    def additem(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def addafteritem(self,prev_node,new_data):
        if prev_node is None:
            print("item accces korte hobe")
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
        while (last.next):
            last=last.next
        last.next=new_node

    def printlinklist(self):
        temp=self.head
        while (temp):
            print(str(temp.data)+"",end="")
            temp=temp.next
if __name__=='__main__':
    llist=Linklist()
    llist.additem(2)
    llist.additem(3)
    llist.additem(4)
    llist.additem(5)
    llist.additem(6)
    llist.additem(7)
    llist.additem(8)
    llist.additem(9)
    llist.addafteritem(llist.head.next,1)
    llist.addenditem(10)
    llist.printlinklist()'''
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
    def accesafteritem(self,prev_node,new_data):
        if prev_node is None:
            print("the given previous node must in linkedlist")
            return
        new_node=Node(new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
    def accessenditem(self,new_data):
        new_node=Node(new_data)
        if self.head is None:
            self.head=new_node
            return
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def printLinkedlist(self):
        temp=self.head
        while(temp):
            print(str(temp.data)+" ",end="")
            temp=temp.next
if __name__=='__main__':
    llist=Linkedlist()
    llist.accesitem(2)
    llist.accesitem(3)
    llist.accesafteritem(llist.head.next,10)
    llist.accessenditem(11)
    llist.accesitem(2)
    llist.accesitem(2)
    llist.accesitem(2)

    llist.printLinkedlist()'''



























