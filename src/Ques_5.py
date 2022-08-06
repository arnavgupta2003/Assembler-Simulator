
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

def bincount(num):
    a=0
    while(num):
        a+=1
        num//=2
    return a-1

def ques_1(memSpace,memType):       
    print("1. Type A: <Q bit opcode> <P-bit address> <N bit register>")
    print("2. Type B: <Q bit opcode> <R bits filler> <N bit register> <N bit register>") 
    isaType=int(input("Enter the index of the type of ISA(1/2):"))     
    insLength=int(input("Length of one inst. in bits:"))
    regLength=int(input("Length of one reg. in bits:"))
    cpu=int(input("Enter the CPU size in bits:"))
    meminbits=0
    idx=0
    inx=0
    for i in memSpace:
        if i.isdigit():
            idx+=1
            inx=inx*10+int(i)
            continue
    l=memSpace[idx:]
    b=0
    if l in ['word',"Word"]:
        b=cpu
    else:
        b=2**dic[l.lower()]

    meminbits=inx*2**b         

    if memType in ['word',"Word"]:
        meminbits=cpu
    else:
        meminbits=2**dic[memType.lower()]

    if(isaType==1):
        totalPins=bincount(memSpace/meminbits)
        print(f"Minimum bits needed to represent an address in this architecture is: {totalPins}")

        opcode_bits=insLength-regLength-totalPins
        print(f"Number of bits needed by opcode {opcode_bits}")
        
        max_instruction=2**opcode_bits
        print(f"Maximum number of instructions this ISA can support is: {max_instruction}")
        
        max_register=2**regLength
        print(f"Maximum number of registers this ISA can support is: {max_register}")
    else:

        totalPins=bincount(memSpace/meminbits)
        print(f"Minimum bits needed to represent an address in this architecture is: {totalPins}")

        opcode_bits=insLength-regLength-totalPins-regLength
        print(f"Number of bits needed by opcode {opcode_bits}")

        filler_bit=insLength-opcode_bits-2*regLength
        print(f"Number of filler bits are: {filler_bit}")

        max_instruction=2**opcode_bits
        print(f"Maximum number of instructions this ISA can support is: {max_instruction}")
        
        max_register=2**regLength
        print(f"Maximum number of registers this ISA can support is: {max_register}")

def ques_2(memSpace,memType):    
    quesType=int(input("Type of System Enhancement..(1/2) (0 to quit)?"))
    cpu=int(input("Enter the CPU size in bits:"))
    meminbits=0
    idx=0
    inx=0
    for i in memSpace:
        if i.isdigit():
            idx+=1
            inx=inx*10+int(i)
            continue
    l=memSpace[idx:]
    b=0
    if l in ['word',"Word"]:
        b=cpu
    else:
        b=2**dic[l.lower()]

    meminbits=inx*2**b         

    if memType in ['word',"Word"]:
        meminbits=cpu
    else:
        meminbits=2**dic[memType.lower()]

    
    if(quesType==1):   
        cpuBits=cpu
        meminbits=0
        if memType in ['word',"Word"]:
            meminbits=cpuBits
        else:
            meminbits=2**dic[memType.lower()]

        initPins=bincount(memSpace/meminbits)

        changeTo=input("Change the type of CPU to(Bit,Byte,Nibble,word):")

        newmeminbits=0
        if changeTo in ['word',"Word"]:
            newmeminbits=cpuBits
        else:
            newmeminbits=2**dic[changeTo.lower()]

        afterpins=bincount(memSpace/newmeminbits)

        print("We need ",afterpins-initPins,"pins")

    elif(quesType==2):
        cpuBits=cpu
        addPins=int(input("Address pins of CPU:"))
        memType=input("Type of addressable memory(Bit/Byte/Nibble/word_add):")
        meminbits=0
        if memType in ['word',"Word"]:
            meminbits=cpuBits
        else:
            meminbits=2**dic[memType.lower()]
        
        totalmem=addPins*meminbits
        
        expo=bincount(totalmem)

        if (expo>30):
            val=totalmem/(2**30)
            print(val,"GigaBytes")
        elif(expo>20):
            val=totalmem/(2**20)
            print(val,"MegaBytes")
        elif(expo>10):
            val=totalmem/(2**10)
            print(val,"KiloBytes")
        else:
            print(val,"Bytes")
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
