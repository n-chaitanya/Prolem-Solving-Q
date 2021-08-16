class Node:
    def __init__(self,prev,data,next):
        self.prev = prev
        self.data = data
        self.next = next

class dll:
    def __init__(self):
        self.head = None
    def length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return(count)

    def printDll(self):
        if(self.head==None):
            raise Exception('The doubly linked list is empty')
        else:
            prDll = ''
            itr = self.head
            while(itr):
                prDll += str(itr.data) +'-->'
                print(itr.data)
                itr = itr.next
            return(prDll)

    def insertAt(self,index,value):
        if(index<0 or index>self.length()):
            raise Exception ('Index out of range')

        if(index==0):
            node = Node(None,value,self.head)
            self.head = node
        else:
            itr = self.head
            count = 0
            while itr:
                if(count==index-1):
                    node = Node(itr,value,itr.next)
                    itr.next = node
                    node.prev = itr
                itr = itr.next
                count+=1
    
    def deleteAt(self,index):
        if(index<0 or index>self.length()):
            raise Exception ('Index out of range')

        if(self.head == None):
            raise Exception('Cannot delete as there are no elements in the doubly linked list')
        elif(index==0):
            self.head.next.prev = None
            self.head = self.head.next
        else:
            count = 0
            itr = self.head
            if(count==index-1):
                itr.next = itr.next.next
                itr.next.next.prev = itr
            itr = itr.next
            count+=1
    
    def updateAt(self,index,value):

        if(index<0 or index>self.length()):
            raise Exception ('Index out of range')

        if(self.head == None):
            raise Exception('Cannot update as your doubly linked list is empty')
        elif(index==0):
            self.head.data = value
        else:
            itr = self.head
            count = 0
            while itr:
                if(count == index-1):
                    itr.next.data = value
                itr = itr.next
                count+=1

dl1 = dll()
dl1.insertAt(0,5)
dl1.insertAt(1,10)
dl1.insertAt(2,15)
dl1.insertAt(3,20)
dl1.insertAt(4,25)
dl1.insertAt(5,30)
#dl1.deleteAt(0)
dl1.updateAt(2,100)
a1 = dl1.printDll()
print(a1)






