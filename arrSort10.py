#sort an array with 0 and 1
class TestCases:
    def __init__(self,input,output):
        self.input = input
        self.output = output
c1 = TestCases([1,1,0,0],[0,0,1,1])
c2 = TestCases([1,0,1,0],[0,0,1,1])
c3 = TestCases([],[])
c4 = TestCases([1,2,3,4],[1])
c5 = TestCases([5,6,7,0,6],[0])
testList = [c1,c2,c3,c4,c5]

l = [1,2,3,4]
def arrSort10(l):
    x = []
    y = []
    for i in l :
        if(i == 0):
            x.append(i)
        elif(i==1):
            y.append(i)
    joined_list = [*x, *y]
    return(joined_list)


for i in testList:
    value = arrSort10(i.input)
    if(value==i.output):
        print('Passed')
    else:
        print('failed')