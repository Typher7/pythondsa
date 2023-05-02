class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_first(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_last(self, data):
        if self.head is None:
            self.head = Node(data, None)
        
        else: 
            itr = self.head

            while itr.next:
                itr = itr.next

            itr.next = Node(data, None)


    def insert_list(self, datalist):

        for i in datalist:
            self.insert_last(i)


    def getlength(self):
        count = 0

        itr = self.head
        while itr:
            count+=1
            itr=itr.next

        return count
    
    def remove_at(self, index):
        if index<0 or index>=self.getlength():
            raise Exception("Invalid index")
        
        elif index==0:
            self.head = self.head.next
        else:
            count = 0
            itr = self.head

            while itr:
                if count==index-1:
                    itr.next=itr.next.next

                itr = itr.next
                count+=1
            
    def Print(self):

        if self.head is None:
            print("Empty LinkedList")
            return

        else:

            itr = self.head
            llstr = ""

            while itr:
                llstr += str(itr.data) + " --> " 
                itr = itr.next

        return print(f"{llstr}None")


ll = LinkedList()

ll.insert_list(["zero", "one", "two", "three", "four", "five", "six"])
ll.Print()
print(ll.getlength())

ll.remove_at(4)
ll.Print()
print(ll.getlength())