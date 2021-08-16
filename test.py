class TestCases:
    def __init__(self,input,output):
        self.input = input
        self.output = output
c1 = TestCases([1,2,3,4],[4,3,2,1])
c2 = TestCases([2,-5,-8,7],[7,-8,-5,2])
#c3 = TestCases([],[])
testList = [c1,c2]

def rev (l):
    if(l ==[]):
        raise Exception('Cannot enter an empty list')
    x = len(l)-1
    for i in range(0,int(x/2)+1):
        l[i],l[x] = l[x],l[i]
        x = x-1
    return(l)
for i in testList:
    value = rev(i.input)
    if(value==i.output):
        print('Passed')
    else:
        print('failed')
    