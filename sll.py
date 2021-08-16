class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next
class sll:
    def __init__(self):
        self.head = None

    def length(self):
        itr = self.head
        count = 0
        while itr:
            count+=1
            itr = itr.next
        return(count)

    def insertAt(self,index,data):
        if(index<0 or index>self.length()):
            raise Exception ('Index out of range')
        if(index == 0):
            node = Node(data,self.head)
            self.head = node
        else:
            count = 0
            itr = self.head
            while itr:
                if(itr):
                    if(count==index-1):
                        node = Node(data,itr.next)
                        itr.next = node
                        break
                itr = itr.next
                count = count+1
    def deleteAt(self,index):
        if(index<0 or index>self.length()):
            raise Exception ('Index out of range')

        elif (self.head == None):
            raise Exception('Cant delete as there are no elements')
        
        elif(index == 0):
            itr = self.head
            self.head = self.head.next 
        else:
            itr = self.head
            count = 0
            while itr:
                if(count==index-1):
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count = count+1
    
    def updateAt(self,index,value):

        if(index<0 or index>self.length()):
            raise Exception ('Index out of range')

        elif(index==0):
            self.head.data = value
        else:
            count = 0
            itr = self.head
            while(itr):
                if(count == index):
                    itr.data = value
                    break
                itr = itr.next
                count = count+1
    def printSll(self):
        if(self.head==None):
            raise Exception('The singly linked list is empty')
        else:
            prSll = ''
            itr = self.head
            while(itr):
                prSll += str(itr.data) +'-->'
                itr = itr.next
            return(prSll)


            
            