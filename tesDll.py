from dll import *;

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

# sl2 = sll()
# sl2.insertAt(0,9)
# sl2.insertAt(0,8)
# sl2.insertAt(0,7)
# sl2.insertAt(0,6)
# sl2.insertAt(0,5)
# sl2.insertAt(0,4)
# sl2.insertAt(0,3)
# sl2.insertAt(0,2)
# sl2.insertAt(0,1)
# sl2.deleteAt(4)
# sl2.updateAt(7,90)
# a2 = sl2.printSll()

class TestCases:
    def __init__(self,input,output):
        self.input = input
        self.output = output
c1 = TestCases(a1,'5-->10-->100-->20-->25-->30-->')
#c2 = TestCases(a2,'1-->2-->3-->4-->6-->7-->8-->90-->')
testList = [c1]

if(a1 == c1.output):
    print('passed')
else:
    print('failed')

# if(a2 == c2.output):
#     print('passed')
# else:
#     print('failed')