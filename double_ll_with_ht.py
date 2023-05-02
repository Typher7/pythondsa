class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def insert_first(self, data):
        node = Node(data, self.head, None)
        self.head = node
        self.size+=1
        
    def append_last(self, data):
        if self.head is None:
            self.head = Node(data, None, None )
            self.tail = self.head
            self.size+=1
            return

        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next=Node(data, None, itr)
            self.tail=itr.next
            self.size+=1
                
    def pop_last(self):
        if self.head is None:
            raise Exception("Empty Linked List")
        else:
            itr = self.head
            while itr:
                if itr.next.next is None:
                    itr.next=None
                    self.tail=itr
                    self.size-=1
                    return
                itr = itr.next
                
    def insert_list(self, datalist):
        for i in datalist:
            self.append_last(i)
            
    def get_length(self):
        
        return self.size
            
    def print_forward(self):
        if self.head is None:
            print("Empy Linked List")
        else:
            llstr=""
            itr=self.head
            while itr:
                llstr+=f"{str(itr.data)} --> "
                itr=itr.next
                
        return print(llstr+"None")
        
    def print_backward(self):
        if self.head is None:
            print("Empy Linked List")
        else:
            llstr=""
            itr=self.tail
            while itr:
                llstr+=f"{str(itr.data)} --> "
                itr=itr.prev
                
        return print(llstr+"None")
        
    
ll=LinkedList()

ll.insert_list([0,1,2,3,4,5,6,7,8,9])
ll.print_forward()
ll.print_backward()
print(ll.get_length())

