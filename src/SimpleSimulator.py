from sys import stdin

PC=0
MemStack=["0000000000000000"]*256
InsStack=[]
# def __init__():
#     for line in stdin:
#         opcode=line[0:4]
#         #handle in
#         PC+=1
#         InsStack.append(line)
#         print(line)


def MemDump():
    for i in MemStack:
        print(i)

def binadd(a,b):
    summ = bin(int(a, 2) + int(b, 2))
    summ=summ[2:]
    summ.zfill(16)
    return summ

def binsub(a,b):
    diff = bin(int(a, 2) - int(b, 2))
    diff=diff[2:]
    diff.zfill(16)
    return diff

def binmul(a,b):
    mul = bin(int(a, 2) * int(b, 2))
    mul=mul[2::]
    if(len(mul)>16):
        mul=mul[len(mul)-16::]
    else:
        mul=mul.zfill(16)
    return mul

def bindiv(a,b):
    div = bin(int(a, 2) / int(b, 2))
    div=div[2:]
    div.zfill(16)
    return div

    

def return_reg(a):
    pass
def update_reg(a):
    pass

def operatorCall(List,i,l):
    if (i==l):
        return
    if (List[i][0]=="10000"):
        Addition(List,i)
        return operatorCall(List,i+1,l)
    elif(List[i][0]=="10001"):
        Subtraction(List,i)
        return operatorCall(List,i+1,l)
    elif (List[i][0] == "10010"):
        Move_Immediate(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "10011"):
        Move_Register(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "10100"):
        Load(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "10101"):
        Store(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "10110"):
        Multiply(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "10111"):
        Divide(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "11000"):
        Right_Shift(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "11001"):
        Left_Shift(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "11010"):
        Exclusive_OR(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "11011"):
        Or(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "11100"):
        And(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "11101"):
        Invert(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "11110"):
        Compare(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "11111"):
        Unconditional_Jump(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "01100"):
        Jump_If_Less_Than(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "01101"):
        Jump_If_Greater_Than(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "01111"):
        Jump_If_Equal(List,i)
        return operatorCall(List, i + 1, l)
    elif (List[i][0] == "01010"):
        Halt(List,i)
        return operatorCall(List, i + 1, l)


# while (line!="hlt"):#hlt opcode
#     PC+=1
#     InsStack.append(line)

def Addition(List,i):
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binadd(r1,r2)
    r3=List[13:]
    update_reg(r3,newval)

def Subtraction(List,i):
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binsub(r1,r2)
    r3=List[13:]
    update_reg(r3,newval)

def Multiply(List,i):
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binmul(r1,r2)
    r3=List[13:]
    update_reg(r3,newval)

