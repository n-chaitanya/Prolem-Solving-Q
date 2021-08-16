# #string reverse
class TestCases:
    def __init__(self,input,output):
        self.input = input
        self.output = output
c1 = TestCases('My name is Chaitanya Nagulapalli','yM eman si aynatiahC illapalugaN')
c2 = TestCases('uppercase','esacreppu')
c3 = TestCases(' ',' ') 
testList = [c1,c2,c3]

def stringWordReverse(string):
    x = []
    l = []
    s = ''
    a = ''
    for i in string:
        x.append(i)
    for j in x:
        if(j== ' '):
            l.append(s)
            s = ''
        else:
            s = s+j
    l.append(s)
    for i in l:
        c = i.split()
        for j in c:
            for k in j[::-1] :
                a +=  k
    # print(k)
                # print(k,end='')
            # print(' ',end='')
            a += ' '
    return a
#stringWordReverse('My name is Chaitanya Nagulaplli')

for i in testList:
    value = stringWordReverse(str(i.input))
    if(value==str(i.output)):
        print('Passed')
    else:
        print('failed')