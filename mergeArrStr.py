l=['Chaitanya','Nagulapalli','had','a','great','day']
class TestCases:
    def __init__(self,input,output):
        self.input = input
        self.output = output
c1 = TestCases(['Chaitanya','Nagulapalli','had','a','great','day'],' Chaitanya Nagulapalli had a great day')
c3 = TestCases([],'')

testList = [c1,c3]
def mergeArrStr(l):
    x = ''
    for i in l:
        x += ' ' + i
    return(x)
    
for i in testList:
    value = mergeArrStr(i.input)
    if(value==str(i.output)):
        print('Passed')
    else:
        print('failed')
