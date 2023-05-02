class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def insert_first(self, data):
        #new_node = Node(data, self.head)
        #self.head = new_node
        if self.head is None:
            new_node = Node(data, None)
            self.head = new_node
            self.tail = new_node
            return
        else:
            new_node = Node(data, self.head)
            self.head = new_node

    
    def insert_last(self, data):
        new_node = Node(data, None)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
        self.tail = itr.next

    def insert_list(self, datalist):
        for i in datalist:
            self.insert_last(i)
            

    def get_length(self):
        count=0

        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    
    def reverse(self):
        prev = None
        itr = self.head
        #where itr represents the current node

        while itr:
            next = itr.next
            itr.next = prev
            prev = itr
            itr = next
        self.head = prev
        
    def Print(self):
        if self.head is None:
            print("Empty Linked List")
            return
        
        itr = self.head
        llstr = ""

        while itr:
            llstr+=str(itr.data)+"-->"
            itr = itr.next
        print(llstr)


ll = LinkedList()


ll.insert_list(["zero", "one", "two", "three", "four", "five"])
ll.reverse()
ll.Print()
print(f"length: {ll.get_length()}")