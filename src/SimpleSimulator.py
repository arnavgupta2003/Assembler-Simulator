from sys import stdin
from uuid import RFC_4122


global pc,halt
halt=0
pc=0
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
    summ=summ.zfill(16)
    return summ

def binsub(a,b):
    diff = bin(int(a, 2) - int(b, 2))
    if(diff[0]=='-'):
        diff=diff[3:]
        diff=diff.zfill(15)
        diff='-'+diff
    else:
        diff=diff[2:]
        diff=diff.zfill(16)
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
    div=div.zfill(16)
    return div

    

def return_reg(a):
    pass

def update_reg(a):
    pass

def Addition(List):
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binadd(r1,r2)
    r3=List[13:]
    if(newval[0]=='-'):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        if(len(newval)==17):
            newval=newval[1:]
        else:
            newval='0'+newval[1:]
    elif(int(newval,2)>2**15):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval=newval[len(newval)-16:]
    
    update_reg(r3,newval)

def Subtraction(List):
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binsub(r1,r2)
    r3=List[13:]
    if(newval[0]=='-'):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        if(len(newval)==17):
            newval=newval[1:]
        else:
            newval='0'+newval[1:]
    elif(int(newval,2)>2**15):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval=newval[len(newval)-16:]

    update_reg(r3,newval)

def Multiply(List):
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binmul(r1,r2)
    r3=List[13:]
    if(newval[0]=='-'):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        if(len(newval)==17):
            newval=newval[1:]
        else:
            newval='0'+newval[1:]
    elif(int(newval,2)>2**15):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval=newval[len(newval)-16:]

    update_reg(r3,newval)

def Divide(List):
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=bindiv(r1,r2)
    r3=List[13:]
    update_reg(r3,newval)

def Move_Immediate(List):
    imm=List[8:]
    r1=List[5:8]
    update_reg(r1,imm)

def Move_Register(List):
    r1=return_reg(List[10:13])
    r2=List[13:]
    update_reg(r2,r1)

def Load(List):
    pass

def Store(List):
    pass

def Right_Shift(List):
    r1=return_reg(List[5:8])
    imm=int(List[8:],2)
    if(imm>16):
        newval="0"*16
    else:
        newval="0"*imm+r1[0:16-imm]
    update_reg(List[5:8],newval)

def Left_Shift(List):
    r1=return_reg(List[5:8])
    imm=int(List[8:],2)
    if(imm>16):
        newval="0"*16
    else:
        newval=r1[16-imm::]+"0"*imm
    update_reg(List[5:8],newval)
    
def Exclusive_OR(List):
    r1 = int(return_reg(List[7:10]),2)
    r2 = int(return_reg(List[10:13]),2)
    newval = bin(r1^r2)[2:]
    r3 = List[13:]
    update_reg(r3, newval)


def Or(List):
    r1 = int(return_reg(List[7:10]),2)
    r2 = int(return_reg(List[10:13]),2)
    newval = bin(r1 | r2)[2:]
    r3 = List[13:]
    update_reg(r3, newval)

def And(List):
    r1 = int(return_reg(List[7:10]),2)
    r2 = int(return_reg(List[10:13]),2)
    newval = bin(r1 & r2)[2:]
    r3 = List[13:]
    update_reg(r3, newval)

def Invert(List):
    r1 = return_reg(List[10:13],2)

    newval = bin(~r1)[2:]
    r3 = List[13:]
    update_reg(r3, newval)

def Compare(List):
    r1=int(return_reg(List[8:13]),2)
    r2=int(return_reg(List[13:]),2)

    if(r1==r2):
        newval='1'
        newval=newval.zfill(16)
        update_reg('111',newval)
    elif(r1>r2):
        newval='10'
        newval=newval.zfill(16)
        update_reg('111',newval)
    elif(r1<r2):
        newval='100'
        newval=newval.zfill(16)
        update_reg('111',newval)

def Unconditional_Jump(List):
    global pc
    pc=int(List[8:],2)

def Jump_If_Less_Than(List):
    global pc
    Flag=int(return_reg("111"),2)
    if(Flag==4):
        pc=int(List[8:],2)

def Jump_If_Greater_Than(List):
    global pc
    Flag=int(return_reg("111"),2)
    if(Flag==2):
        pc=int(List[8:],2)


def Jump_If_Equal(List):
    global pc
    Flag=int(return_reg("111"),2)
    if(Flag==1):
        pc=int(List[8:],2)

def Halt(List):
    global halt
    halt=1

def operatorCall(List,pc):
    if (List[pc][:5] == "10000"):
        Addition(List[pc])

    elif (List[pc][:5] == "10001"):
        Subtraction(List[pc])

    elif (List[pc][:5] == "10010"):
        Move_Immediate(List[pc])

    elif (List[pc][:5] == "10011"):
        Move_Register(List[pc])

    elif (List[pc][:5] == "10100"):
        Load(List[pc])

    elif (List[pc][:5] == "10101"):
        Store(List[pc])

    elif (List[pc][:5] == "10110"):
        Multiply(List[pc])

    elif (List[pc][:5] == "10111"):
        Divide(List[pc])

    elif (List[pc][:5] == "11000"):
        Right_Shift(List[pc])

    elif (List[pc][:5] == "11001"):
        Left_Shift(List[pc])

    elif (List[pc][:5] == "11010"):
        Exclusive_OR(List[pc])

    elif (List[pc][:5] == "11011"):
        Or(List[pc])

    elif (List[pc][:5] == "11100"):
        And(List[pc])

    elif (List[pc][:5] == "11101"):
        Invert(List[pc])

    elif (List[pc][:5] == "11110"):
        Compare(List[pc])

    elif (List[pc][:5] == "11111"):
        Unconditional_Jump(List[pc])

    elif (List[pc][:5] == "01100"):
        Jump_If_Less_Than(List[pc])

    elif (List[pc][:5] == "01101"):
        Jump_If_Greater_Than(List[pc])

    elif (List[pc][:5] == "01111"):
        Jump_If_Equal(List[pc])

    elif (List[pc][:5] == "01010"):
        Halt(List[pc])



# while (line!="hlt"):#hlt opcode
#     PC+=1
#     InsStack.append(line)
