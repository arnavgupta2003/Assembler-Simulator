
dic={   "b":0,
        "bit":0,
        "Kb":10,
        "Mb":20,
        "Gb":30,
        "kb":10,
        "mb":20,
        "gb":30,
        
        "byte":3,
        "B":3,
        "kB":13,
        "mB":23,
        "gB":33,
        "KB":13,
        "MB":23,
        "GB":33,

        
        "Nibble":2,
        "nibble":2,
        
        "knibble":12,
        "kNibble":12,
        "Knibble":12,
        "KNibble":12,
        
        
        "gnibble":22,
        "gNibble":22,
        "Gnibble":22,
        "GNibble":22,
    }


def word(word,a):
    word=word.lower()
    if(word=="word"):
        return bincount(a)
    elif(word=="kword"):
        return bincount(a)+10
    elif(word=="mword"):
        return bincount(a)+20    
    elif(word=="gword"):
        return bincount(a)+30
    else:
        return False        
        
def bincount(num):
    a=0
    while(2**a<num):
        a+=1
    return a

def ques_1(memSpace,memType):       
    print("1. Type A: <Q bit opcode> <P-bit address> <N bit register>")
    print("2. Type B: <Q bit opcode> <R bits filler> <N bit register> <N bit register>\n\n")    
    insLength=int(input("Length of one inst. in bits:"))
    regLength=int(input("Length of one reg. in bits:"))
    cpu=int(input("Enter the number of bits of CPU:"))
    print()
    print()
    
    idx=0
    inx=0
    for i in memSpace:
        if i.isdigit():
            idx+=1
            inx=inx*10+int(i)
            continue
    l=memSpace[idx:]
    b=0
    if word(l,cpu):
        b=word(l,cpu)
    else:
        b=dic[l]

    totalmempin=bincount(inx)+b

    if word(memType,cpu):
        addinbits=word(memType,cpu)
    else:
        addinbits=dic[memType.lower()]

    totalPins=totalmempin-addinbits
    print(f"Minimum bits needed to represent an address in this architecture is: {totalPins} \n")

    opcode_bits=insLength-regLength-totalPins
    print(f"Number of bits needed by opcode {opcode_bits} \n")
    
    filler_bit=insLength-opcode_bits-2*regLength
    print(f"Number of filler bits are: {filler_bit}\n")

    max_instruction=2**opcode_bits
    print(f"Maximum number of instructions this ISA can support is: {max_instruction} \n")
    
    max_register=2**regLength
    print(f"Maximum number of registers this ISA can support is: {max_register}")





def ques_2(memSpace,memType):    

    quesType=int(input("Type of System Enhancement..(1/2) (0 to quit)?"))
    cpu=int(input("Enter the CPU size in bits:"))
    idx=0
    inx=0
    for i in memSpace:
        if i.isdigit():
            idx+=1
            inx=inx*10+int(i)
            continue
    l=memSpace[idx:]
    b=0
    if word(l,cpu):
        b=word(l,cpu)
    else:
        b=dic[l]

    totalmempin=bincount(inx)+b

    if word(memType,cpu):
        addinbits=word(memType,cpu)
    else:
        addinbits=dic[memType.lower()]
    
    if(quesType==1):   
        cpuBits=cpu

        initPins=totalmempin-addinbits

        changeTo=input("Change the type of CPU to(Bit,Byte,Nibble,word):")

        newmeminbits=0
        if word(changeTo,cpu):
            newmeminbits=word(changeTo,cpuBits)
        else:
            newmeminbits=dic[changeTo.lower()]

        afterpins=totalmempin-newmeminbits

        print("We need ",afterpins-initPins,"pins")

    elif(quesType==2):
        cpuBits=cpu
        addPins=int(input("Address pins of CPU:"))
        memType=input("Type of addressable memory(Bit/Byte/Nibble/word):")
        meminbits=0
        if word(memType,cpu):
            meminbits=word(memType,cpu)
        else:
            meminbits=dic[memType.lower()]
        
        expo=addPins+meminbits
        
        if (expo>33):
            val=2**(expo-33)
            print(val,"GigaBytes\n")
        elif(expo>23):
            val=2**(expo-23)
            print(val,"MegaBytes\n")
        elif(expo>13):
            val=2**(expo-13)
            print(val,"KiloBytes\n")
        else:
            2**(expo-3)
            print(val,"Bytes\n")
    else:
        print("Bye..")    

def i_o():
    print("------------------------------------------")
    print("----------------Welcome-------------------")
    print("------------------------------------------")
    while(True):
        print("Share initial input-->")
        memSpace=input("Memory Space:")
        memType=input("Type of addressable memory(Bit/Byte/Nibble/word):")
        print("Queries start")
    
        quesFlag=int(input("Which question should we try first(1/2)?"))
        if(quesFlag==1):
            print()
            ques_1(memSpace,memType)
            print()
        elif(quesFlag==2):
            print()
            ques_2(memSpace,memType) 
            print()
        cont=input("Continue?(0/1)")
        if(cont=="0"):
            break        

i_o() 
