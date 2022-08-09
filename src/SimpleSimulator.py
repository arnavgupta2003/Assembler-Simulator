from re import L
from sys import stdin
from turtle import up
import matplotlib.pyplot as plt

def decimaltoieee(deci):
    num=0
    a=deci.split('.')
    nondeci=bin(int(a[0]))[2:]
    remaining=len(nondeci)
    decim=a[1]
    decilen=len(decim)
    decim=int(a[1])/(10**decilen)
    afterdeci=''
    count=0
    flag=0
    if(float(deci)<1):
        flag=1
    elif(float(deci)>=252):
        num=1
    
    while(True):
        
        if(count>(5-remaining)):
            flag=1
            break
        if(decim==0):
            break
        
        decim*=2
        count+=1        
        if(decim>=1):
            decim-=1
            afterdeci+='1'
        
        elif(decim<1):
            afterdeci+='0'

    expo=bin(remaining-1)[2:]
    expo=expo.zfill(3)
    mantisa=nondeci[1:]+afterdeci
    mantisa=mantisa+'0'*(5-len(mantisa))
    binary=expo+mantisa
    if num>0:
        return "number overflow"
    elif(flag>0):
        return "float overflow"
    else:
        return binary

def binn_val_after_decimal(binn):
    sum=0
    for i in range(0,len(binn)):
        if(binn[i]=='1'):
            sum+=1/(2**(i+1))
    return sum

def binn_val_before_decimal(bin):
    dec=int(bin,2)
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
    if(exponent+1<=len(binnary)):
        before=binnary[0:exponent+1]
        after=binnary[exponent+1:]
    else:
        before=binnary+'0'*(-len(binnary)+exponent+1)
        after=''
    decimal=binn_val_after_decimal(after)+binn_val_before_decimal(before)
    return decimal
def resetflag():
    flag='0'*16
    update_reg('111',flag)

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

def binmod(a,b):
    div = bin(int(a, 2) % int(b, 2))
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
    pc+=1
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binadd(r1,r2)
    r3=List[13:]
    if(newval[0]=='-'):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval='0'*16
        update_reg(r3,newval)
        return
    elif(int(newval,2)>2**16-1):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        n=int(newval,2)
        n=n%(2**16)
        newval=bin(n)[2:]
        newval=newval.zfill(16)
        update_reg(r3,newval)
        return
    update_reg(r3,newval)
    resetflag()
    
def Subtraction(List):
    global pc
    pc+=1
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binsub(r1,r2)
    r3=List[13:]
    if(newval[0]=='-'):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval='0'*16
        update_reg(r3,newval)
        return
    elif(int(newval,2)>2**16-1):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        n=int(newval,2)
        n=n%(2**16)
        newval=bin(n)[2:]
        newval=newval.zfill(16)
        update_reg(r3,newval)
        return
    update_reg(r3,newval)
    resetflag()
    
def Multiply(List):
    global pc
    pc+=1
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    newval=binmul(r1,r2)
    r3=List[13:]
    if(newval[0]=='-'):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        newval='0'*16
        update_reg(r3,newval)
        return
    elif(int(newval,2)>2**16-1):
        Flag='1000'
        Flag=Flag.zfill(16)
        update_reg('111',Flag)
        n=int(newval,2)
        n=n%(2**16)
        newval=bin(n)[2:]
        newval=newval.zfill(16)
        update_reg(r3,newval)
        return
    update_reg(r3,newval)
    resetflag()

def Divide(List):
    global pc
    r1=return_reg(List[10:13])
    r2=return_reg(List[13:])
    que=bindiv(r1,r2)
    rem=binmod(r1,r2)
    update_reg('000',que)
    update_reg('001',rem)
    pc+=1
    resetflag()

def Move_Immediate(List):
    global pc
    imm=List[8:]
    imm=imm.zfill(16)
    r1=List[5:8]
    update_reg(r1,imm)
    pc+=1
    resetflag()

def Move_Register(List):
    global pc
    r1=return_reg(List[10:13])
    r2=List[13:]
    update_reg(r2,r1)
    pc+=1
    resetflag()

def Load(List):
    global MemStack,pc,cycle,x_axis_cycle,y_axis_mem
    cycle+=1
    x_axis_cycle.append(cycle)
    y_axis_mem.append(pc)

    mem=List[8:]
    memadd=int(mem,2)
    update_reg(List[5:8],MemStack[memadd])
    pc+=1
    resetflag()

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
    resetflag()

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
    resetflag()

def Left_Shift(List):
    global pc
    r1=return_reg(List[5:8])
    imm=int(List[8:],2)
    if(imm>16):
        newval="0"*16
    else:
        newval=r1[imm::]+"0"*imm
    update_reg(List[5:8],newval)
    pc+=1
    resetflag()

def Exclusive_OR(List):
    global pc
    r1 = int(return_reg(List[7:10]),2)
    r2 = int(return_reg(List[10:13]),2)
    newval = bin(r1^r2)[2:]
    newval=newval.zfill(16)
    r3 = List[13:]
    update_reg(r3, newval)
    pc+=1
    resetflag()

def Or(List):
    global pc
    r1 = int(return_reg(List[7:10]),2)
    r2 = int(return_reg(List[10:13]),2)
    newval = bin(r1 | r2)[2:]
    newval=newval.zfill(16)
    r3 = List[13:]
    update_reg(r3, newval)
    pc+=1
    resetflag()

def And(List):
    global pc
    r1 = int(return_reg(List[7:10]),2)
    r2 = int(return_reg(List[10:13]),2)
    newval = bin(r1 & r2)[2:]
    newval=newval.zfill(16)
    r3 = List[13:]
    update_reg(r3, newval)
    pc+=1
    resetflag()

def Invert(List):
    global pc
    r1 = return_reg(List[10:13])
    newval=''.join(['1' if i=='0' else '0' for i in r1])
    r3 = List[13:]
    update_reg(r3, newval)
    pc+=1
    resetflag()

def Compare(List):
    global pc
    pc+=1
    r1=int(return_reg(List[8:13]),2)
    r2=int(return_reg(List[13:]),2)

    if(r1==r2):
        newval='1'
        newval=newval.zfill(16)
        update_reg('111',newval)
        return
    elif(r1>r2):
        newval='10'
        newval=newval.zfill(16)
        update_reg('111',newval)
        return
    elif(r1<r2):
        newval='100'
        newval=newval.zfill(16)
        update_reg('111',newval)
        return  

    resetflag()

def Unconditional_Jump(List):
    global pc
    pc=int(List[8:],2)
    resetflag()



def Jump_If_Less_Than(List):
    global pc
    Flag=int(return_reg("111"),2)
    if(Flag==4):
        pc=int(List[8:],2)
    else:
        pc+=1
    
    resetflag()

def Jump_If_Greater_Than(List):
    global pc
    Flag=int(return_reg("111"),2)
    if(Flag==2):
        pc=int(List[8:],2)
    else:
            pc+=1
    resetflag()

def Jump_If_Equal(List):
    global pc
    Flag=int(return_reg("111"),2)
    if(Flag==1):
        pc=int(List[8:],2)
    else:
        pc+=1
    resetflag()

def Halt(List):
    global halt,pc
    pc+=1
    halt=1
    resetflag()

def f_addition(List):

    global pc
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])
    r2=r2[8:]
    r1=r1[8:]

    r3=List[13:]

    val=str(float(ieee_to_decimal(r1)+ieee_to_decimal(r2)))

    newval=decimaltoieee(val)
    
    if(newval=='float overflow'):
        update_reg(r3,'0'*16)
        update_reg('111','0000000000001000')
    elif(newval=='number overflow'):
        update_reg(r3,'0'*8+'1'*8)
        update_reg('111','0000000000001000')
    else:
        newval=newval.zfill(16)
        update_reg(r3, newval)
        resetflag()
    pc += 1

def f_subtraction(List):

    global pc
    r1=return_reg(List[7:10])
    r2=return_reg(List[10:13])

    r2=r2[8:]
    r1=r1[8:]

    r3=List[13:]

    val=(float(ieee_to_decimal(r1)-ieee_to_decimal(r2)))
    if (val<1):
        update_reg(r3,'0'*16)
        update_reg('111','0000000000001000')
    
    val=str(val)
    newval=decimaltoieee(val)
    
    if(newval=='float overflow'):
        update_reg(r3,'0'*16)
        update_reg('111','0000000000001000')
    elif(newval=='number overflow'):
        update_reg(r3,'0'*8+'1'*8)
        update_reg('111','0000000000001000')
    else:
        newval=newval.zfill(16)
        update_reg(r3, newval)
        resetflag()

    pc+=1

def moveF_immediate(List):
    global pc
    imm = List[8:]
    imm = imm.zfill(16)
    r1 = List[5:8]
    update_reg(r1, imm)
    pc += 1
    resetflag()




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

    elif (List[:5] == "00000"):
        f_addition(List)

    elif (List[:5] == "00001"):
        f_subtraction(List)
    elif (List[:5] == "00010"):
        moveF_immediate(List)


global pc,halt,MemStack
halt=0
pc=0
cycle=0
x_axis_cycle=[]
y_axis_mem=[]
RegStack=["0000000000000000"]*8
MemStack=["0000000000000000"]*257
lines=[]

i=0
for line in stdin:
    if(line[-1]=='\n'):
        line=line[:-1]
    if(len(line)!=16):
        pass

    else:
        f=0
        for j in line:
            if(j!='0' and j!='1'):
                f+=1
        if(f==0):
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
        #print(pc_val,end='')
        f.write(pc_val)

        for i in RegStack:
            #print(' '+i,end='',sep='')
            f.write(' '+i)

        #print('\n',sep='',end='')
        f.write('\n')

        # f.write(str(pc)+" " + MemStack[pc]+'\n')


        if(halt==1):
            break



    print('\n'.join(MemStack[0:-1]))
    f.write('\n'.join(MemStack))

plt.scatter(x_axis_cycle,y_axis_mem,c='red')
plt.xlabel("cycles")
plt.ylabel("memory access")
plt.show()

