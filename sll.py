class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def trav(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end="->")
            temp=temp.next
    def insert_at_begin(self,data):
        ne=Node(data)
        ne.next=self.head
        self.head=ne
    def insert_at_end(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=ne
    def inser_at_specfied(self,ps,data):
        ne=Node(data)
        temp=self.head
        for i in range(1,ps-1):
            temp=temp.next
        ne.data=data
        ne.next=temp.next
        temp.next=ne
    def delete_at_bg(self):
        temp=self.head
        self.head=temp.next
        temp.next=None
    def delete_at_specified(self,ps):
        temp=self.head.next
        prv=self.head
        for i in range(1,ps-1):
            temp=temp.next
            prv=prv.next
        prv.next=temp.next
        temp.next=None
    def delete_at_end(self):
        temp=self.head.next
        prv=self.head
        while temp.next is not None:
            temp=temp.next
            prv=prv.next
        prv.next=None
g=sll()
g.insert_at_begin(10)
g.insert_at_begin(5)
g.insert_at_begin(1)

g.inser_at_specfied(4,20)
g.insert_at_end(80)
g.insert_at_begin(0)
g.delete_at_bg()
g.delete_at_end()
g.delete_at_specified(3)
g.trav()
