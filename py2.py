class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def insert_first(self, data):
        new_node = Node(data, self.head)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node

    
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
        self.tail = itr.next.next

    def insert_list(self, datalist):
        self.head = None
        for i in datalist:
            self.insert_last(i)


    def get_length(self):
        count=0

        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count
    

    def insert_at_index(self, index, data):

        if index < 0 or index > self.getlength():
            raise Exception("Invalid index")
        
        if index==0:
                self.insertfirst(data)
        elif index==self.getlength():
            self.insertlast(data)
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = Node(data, itr.next)
                    break

                itr = itr.next
                count+=1


    def insert_after_data(self, data_after, data_ins):
        itr = self.head
        
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_ins, itr.next)
                return
            itr = itr.next
            
        raise Exception("data_after not found in LL")
        
    
    def insert_before_data(self, data_before, data_ins):
        if self.head.data == data_before:
            self.insert_first(data_ins)
            return
        else:
            itr = self.head
            
            while itr:
                if itr.next.data == data_before:
                    itr.next = Node(data_ins, itr.next)
                    return
                itr = itr.next
                
            raise Exception("data_after not found in LL")
        
    
    def remove_at_index(self, index):

        if index < 0 or index >= self.getlength():
            raise Exception("Invalid index")
        
        if index == 0:
            self.head = self.head.next
        
        else:

            count = 0
            itr = self.head
            while itr:
                if count == index-1:
                    itr.next = itr.next.next
                    break

                itr = itr.next
                count+=1

        
    def remove_by_value(self, data):
        
        count=0
        itr = self.head
        
        while itr != None:
            if itr.data == data:
                self.remove_at(count)
                break
            count+=1
            itr = itr.next

        if count == self.getlength()+1:
            raise Exception("data not in linked list")
        

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
ll.Print()
print(f"length: {ll.get_length()}")