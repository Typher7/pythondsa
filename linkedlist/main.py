class SingleListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next=next
    
class DoubleListNode:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next=next
        self.prev=prev

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail=None
        self.length=0
        
    def add_head(self, value):
        node = SingleListNode(value, self.head)
        self.head = node
    
    def getNode(self, index):
        if index < 0 or index >= self.length:
            raise ValueError("Index out of Bounds")
        count=0
        current=self.head
        while count < index and current:
            current = current.next
            count+=1
        return current

    def delete_at_index_doub(self, index):
        temp = self.getNode(index)
        if temp:
            if temp.prev:
                temp.prev.next = temp.next
            if temp.next:
                temp.next.prev = temp.prev
            temp.prev = None
            temp.next = None
            temp.data = None
            self.length-=1

    def Print(self):
        itr=self.head
        while itr:
            print(itr.data, end=" -> ")
            itr=itr.next
        print("Nonny")

    def reverse_recursive(self, current, prev=None):
        if not current:
            return prev

        next_node = current.next
        current.next = prev

        return self.reverse_recursive(next_node, current)
        
llist = SingleLinkedList()
llist.add_head(1)
llist.add_head(2)
llist.add_head(3)
llist.add_head(4)
llist.Print()
