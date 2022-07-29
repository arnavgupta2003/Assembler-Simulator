from sys import stdin
import matplotlib.pyplot as plt

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
    div = bin(int(a, 2) // int(b, 2))
    div=div[2:]
    div=div.zfill(16)
    return div

def return_reg(a):
    val=int(a,2)
    return RegStack[val]

def update_reg(a,b):
    val=int(a,2)
    RegStack[val]=b

def Addition(List):
    global pc
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binadd(r1,r2)
    r3=List[13:]
    if(newval[0]=='-'):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        
        newval='0'*16
    elif(int(newval,2)>2**15):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval=newval[len(newval)-16:]
    
    update_reg(r3,newval)
    pc+=1

def Subtraction(List):
    global pc
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binsub(r1,r2)
    r3=List[13:]
    if(newval[0]=='-'):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval='0'*16
    elif(int(newval,2)>2**15):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval=newval[len(newval)-16:]

    update_reg(r3,newval)
    pc+=1

def Multiply(List):
    global pc
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binmul(r1,r2)
    r3=List[13:]
    if(newval[0]=='-'):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval='0'*16
    elif(int(newval,2)>2**15):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval=newval[len(newval)-16:]

    update_reg(r3,newval)
    pc+=1

def Divide(List):
    global pc
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=bindiv(r1,r2)
    r3=List[13:]
    update_reg(r3,newval)
    pc+=1

def Move_Immediate(List):
    global pc
    imm=List[8:]
    imm=imm.zfill(16)
    r1=List[5:8]
    update_reg(r1,imm)
    pc+=1

def Move_Register(List):
    global pc
    r1=return_reg(List[10:13])
    r2=List[13:]
    update_reg(r2,r1)
    pc+=1

def Load(List):
    global MemStack,pc,cycle,x_axis_cycle,y_axis_mem
    cycle+=1
    x_axis_cycle.append(cycle)
    y_axis_mem.append(pc)

    mem=List[8:]
    memadd=int(mem,2)
    update_reg(List[5:8],MemStack[memadd])
    pc+=1

def Store(List):
    global MemStack,pc,cycle,x_axis_cycle,y_axis_mem
    cycle+=1
    x_axis_cycle.append(cycle)
    y_axis_mem.append(pc)

    r1=return_reg(List[5:8])
    mem=List[8:]
    memadd=int(mem,2)
    MemStack[memadd]=r1
    pc+=1

def Right_Shift(List):
    global pc
    r1=return_reg(List[5:8])
    imm=int(List[8:],2)
    if(imm>16):
        newval="0"*16
    else:
        newval="0"*imm+r1[0:16-imm]
    update_reg(List[5:8],newval)
    pc+=1

def Left_Shift(List):
    global pc
    r1=return_reg(List[5:8])
    imm=int(List[8:],2)
    if(imm>16):
        newval="0"*16
    else:
        newval=r1[16-imm::]+"0"*imm
    update_reg(List[5:8],newval)
    pc+=1

def Exclusive_OR(List):
    global pc
    r1 = int(return_reg(List[7:10]),2)
    r2 = int(return_reg(List[10:13]),2)
    newval = bin(r1^r2)[2:]
    r3 = List[13:]
    update_reg(r3, newval)
    pc+=1

def Or(List):
    global pc
    r1 = int(return_reg(List[7:10]),2)
    r2 = int(return_reg(List[10:13]),2)
    newval = bin(r1 | r2)[2:]
    r3 = List[13:]
    update_reg(r3, newval)
    pc+=1

def And(List):
    global pc
    r1 = int(return_reg(List[7:10]),2)
    r2 = int(return_reg(List[10:13]),2)
    newval = bin(r1 & r2)[2:]
    r3 = List[13:]
    update_reg(r3, newval)
    pc+=1

def Invert(List):
    global pc
    r1 = return_reg(List[10:13],2)

    newval = bin(~r1)[2:]
    r3 = List[13:]
    update_reg(r3, newval)
    pc+=1

def Compare(List):
    global pc
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
    
    pc+=1

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
    else:
            pc+=1

def Jump_If_Equal(List):
    global pc
    Flag=int(return_reg("111"),2)
    if(Flag==1):
        pc=int(List[8:],2)
    else:
        pc+=1


def Halt(List):
    global halt,pc
    pc+=1
    halt=1

def operatorCall(List,pc):
    if (List[:5] == "10000"):
        Addition(List)

    elif (List[:5] == "10001"):
        Subtraction(List)

    elif (List[:5] == "10010"):
        Move_Immediate(List)

    elif (List[:5] == "10011"):
        Move_Register(List)

    elif (List[:5] == "10100"):
        Load(List)

    elif (List[:5] == "10101"):
        Store(List)

    elif (List[:5] == "10110"):
        Multiply(List)

    elif (List[:5] == "10111"):
        Divide(List)

    elif (List[:5] == "11000"):
        Right_Shift(List)

    elif (List[:5] == "11001"):
        Left_Shift(List)

    elif (List[:5] == "11010"):
        Exclusive_OR(List)

    elif (List[:5] == "11011"):
        Or(List)

    elif (List[:5] == "11100"):
        And(List)

    elif (List[:5] == "11101"):
        Invert(List)

    elif (List[:5] == "11110"):
        Compare(List)

    elif (List[:5] == "11111"):
        Unconditional_Jump(List)

    elif (List[:5] == "01100"):
        Jump_If_Less_Than(List)

    elif (List[:5] == "01101"):
        Jump_If_Greater_Than(List)

    elif (List[:5] == "01111"):
        Jump_If_Equal(List)

    elif (List[:5] == "01010"):
        Halt(List)

global pc,halt,MemStack
halt=0
pc=0
cycle=0
x_axis_cycle=[]
y_axis_mem=[]
RegStack=["0000000000000000"]*8
MemStack=["0000000000000000"]*256
lines=[]

i=0
for line in stdin:
    line=line[:-1]
    lines.append(line)
    MemStack[i]=line
    i+=1


with open("out.txt",'w') as f:
    while (True):
        cycle+=1
        x_axis_cycle.append(cycle)
        y_axis_mem.append(pc)
        pc_val=bin(pc)[2:]
        pc_val=pc_val.zfill(8)
        operatorCall(MemStack[pc],pc)
        print(pc_val,end=' ')
        print(*RegStack)
        f.write(pc_val+' ')
        f.write(' '.join(RegStack)+'\n')


        if(halt==1):
            break



    print('\n'.join(MemStack))
    f.write('\n'.join(MemStack))

plt.scatter(x_axis_cycle,y_axis_mem,c='red')
plt.xlabel("cycles")
plt.ylabel("memory access")
plt.show()


