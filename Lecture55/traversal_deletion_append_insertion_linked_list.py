# lecture 55 : traversal, insertion, deletion, append

# creating a node

class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next=node2
node2.next=node3
node3.next=node4

print(node1) # prints self node address

print(node1.next) # prints next node address

print(node1.val) #prints exact node value

print(node1.next.next.next.val) # every nect appends to next address, and as val is mentioned so value is printed


class Node:
    def __init__(self, val):
        self.val=val
        self.next=None

class SinglyLinkedList:
    def __init__(self) -> None:
        self.head=None
    def append(self, val):
        newNode=Node(val)
        if not self.head:
            self.head=newNode
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newNode
    def traverse(self):
        if not self.head:
            print("sll is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val, end=" ")
                curr=curr.next
            print()

sll = SinglyLinkedList()

sll.traverse()
sll.append(10)
sll.traverse()