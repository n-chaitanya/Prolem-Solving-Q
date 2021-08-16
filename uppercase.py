#uppercase and lower case
#65 90 A Z 97-122 a z 

class TestCases:
    def __init__(self,input,output):
        self.input = input
        self.output = output
c1 = TestCases('chaitanya nagulapalli','CHAITANYA NAGULAPALLI')
c2 = TestCases('upPerCase','UPPERCASE')
c3 = TestCases([],[])

testList = [c1,c2,c3]

def uppercase(st):
    x = ''
    for i in st:
        if (ord(i) >= 97 and ord(i)<=122)  :
            x += chr(ord(i) - 32)
        else:
            x += i
    return(x) 
# x = uppercase('CHaitanya Nagulapalli')
# print(x)

for i in testList:
    value = uppercase(str(i.input))
    if(value==str(i.output)):
        print('Passed')
    else:
        print('failed')
