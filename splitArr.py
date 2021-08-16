class TestCases:
    def __init__(self,input,output):
        self.input = input
        self.output = output
c1 = TestCases('chaitanya nagulapalli',['chaitanya','nagulapalli'])
c2 = TestCases('uppercase',['uppercase'])
c3 = TestCases('withspace ',['withspace','']) 
c4 = TestCases('',[''])

testList = [c1,c2,c3,c4]

def splitArr(st):
    x = []
    l = []
    s = ''
    for i in st:
        x.append(i)
    for j in x:
        if(j== ' '):
            l.append(s)
            s = ''
        else:
            s = s+j
    l.append(s)
    return(l)
# x = splitArr('chaitaYAAAAAAAAA yghchgc gch kvhf')
# print(x)

for i in testList:
    value = splitArr(str(i.input))
    if(value==(i.output)):
        print('Passed')
    else:
        print('failed')