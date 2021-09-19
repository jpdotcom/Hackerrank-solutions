import random
class Node:

    def __init__(self,val):
        
        self.val=val
        self.next=None


class LinkedList:

    def __init__(self):
        self.head = None
    
    def gethead(self):
        if self.head is not None:
            return self.head.val
        else:
            return None
    def insert(self,val):
        v=Node(val)

        if self.head is None:
            self.head=v
            return 
        
        n=self.head
        self.head=v
        v.next=n
    

    def traverse(self):


        n=self.head
        arr=[]
        while n is not None:
            arr.append(n.val)
            n=n.next
        return arr
    def reverse(self):


        n=self.head
        prev_node=None

        while n is not None:

            next_node=n.next
            n.next=prev_node
            prev_node=n
            n=next_node
        self.head=prev_node
        return 

i=0
linked=LinkedList()
for _ in range(i):

    linked.insert(random.randint(1,100))

print(linked.gethead())
print(linked.traverse())
linked.reverse()
print(linked.traverse())
print(linked.gethead())






    




