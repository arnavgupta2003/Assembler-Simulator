from sys import stdin
from uuid import RFC_4122

from numpy import right_shift

global pc
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



def binn_val_after_decimal(binn):
    j=0
    for i in range(len(binn)):
        if(binn[i]=='.'):
            j=i
            break

    sum=0
    for i in range(j,len(binn)):
        if(binn[i]=='1'):
            sum+=1/(2**(i-j))
    return sum
def binn_val_before_decimal(bin):
    j=0
    for i in range(len(bin)):
        if(bin[i]=='.'):
            j=i
    bin = int(bin)
    dec=int(bin[0:i],2)
    return dec
def last_one(ieee):
    ret=0
    for i in range(3,8):
        if(ieee[i]=='1'):
            ret=i
    return ret
def ieee_to_decimal(ieee):
    exp=ieee[:3]
    mantissa=ieee[3:last_one(ieee)+1]
    exponent=int(exp,2)
    binnary='1'+mantissa
    int_binnary=int(binnary)
    final_binn=int_binnary/10**(len(binnary)-1-exponent)

    decimal=binn_val_after_decimal(str(final_binn))+binn_val_before_decimal(str(final_binn))
    return decimal

def f_addition(List):

    global pc
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])

    r3=List[13:]

    val=ieee_to_decimal(r1)+ieee_to_decimal(r2)

    # make val binary

    update_reg(r3, val)
    pc += 1


def f_subtraction(List):

    global pc
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])

    r3=List[13:]
    # make val binary
    val=ieee_to_decimal(r1)-ieee_to_decimal(r2)
    update_reg(r3,val)
    pc+=1
def moveF_immediate(List):
    global pc
    imm = List[8:]
    # imm = imm.zfill(16)
    r1 = List[5:8]
    update_reg(r1, imm)
    pc += 1








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

def Addition(List):
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binadd(r1,r2)
    r3=List[13:]
    update_reg(r3,newval)

def Subtraction(List):
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binsub(r1,r2)
    r3=List[13:]
    update_reg(r3,newval)

def Multiply(List):
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binmul(r1,r2)
    r3=List[13:]
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
    pass

def Or(List):
    pass

def And(List):
    pass

def Invert(List):
    pass

def Compare(List):
    pass

def Unconditional_Jump(List):
    pass

def Jump_If_Less_Than(List):
    pass

def Jump_If_Greater_Than(List):
    pass

def Jump_If_Equal(List):
    pass

def Halt(List):
    pass

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



