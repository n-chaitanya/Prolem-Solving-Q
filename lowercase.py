class TestCases:
    def __init__(self,input,output):
        self.input = input
        self.output = output
c1 = TestCases('CHAITANYA NAGULAPALLI','chaitanya nagulapalli')
c2 = TestCases('UpPerCaSe','uppercase')
c3 = TestCases([],[])

testList = [c1,c2,c3]


def lowercase(st):
    x = ''
    for i in st:
        if (ord(i) >= 65 and ord(i)<=90)  :
            x += chr(ord(i) + 32)
        else:
            x += i
    return(x) 

for i in testList:
    value = lowercase(str(i.input))
    if(value==str(i.output)):
        print('Passed')
    else:
        print('failed')