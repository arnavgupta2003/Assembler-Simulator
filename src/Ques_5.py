def normal_query(instruction,register,space,addressed):
    # tpye-a
    i=0
    while(P_address!=1):
        P_address=space/2**i
        i+=1
    P_address=i
    print(f"minimum bits are needed to represent an address in this architecture is {P_address}")
    opcode_bits=instruction-register-P_address
    print(f"Number of bits needed by opcode {opcode_bits}")
    # type-b
    filler_bit=instruction-2*register-opcode_bits
    print(f"Number of filler bits is {filler_bit}")
    max_instruction=space/instruction
    printf(f"the maximum number of instructions this ISA can support is {len(str(int(max_instruction,2)))-1}")
    max_register=space/register
    printf(f"the maximum number of registers this ISA can support is {len(str(int(max_register,2)))-1}")



def type1(cpu_bits,address_memory,space,addressed,retMemSize):
    if(address_memory=="word_size"):
        initial_pin=space/retMemSize(addressed)
        current_pin=space/cpu_bits
        pin_difference=len(str(int(initial_pin,2)))-1-len(str(int(current_pin,2)))-1
        print(f"the number pin difference is {pin_difference}")
    else:
        initial_pin = space / retMemSize(adddressed)
        current_pin = space / retMemSize(address_memory)
        pin_difference = len(str(int(initial_pin, 2))) - 1 - len(str(int(current_pin, 2))) - 1
        print(f"the number pin difference is {pin_difference}")

def type2(cpu_bits,address_pin,address_memory,retMemSize):
    if (address_memory == "word_size"):
        main_memory_size_power=(len(str(int(cpu_bits,2)))-1)+address_pin-3
        main_memory_size=2**main_memory_size_power
        print(f"the main memory size is {main_memory_size} bytes")
    else:
        main_memory_size_power = (len(str(int(retMemSize(address_memory), 2))) - 1) + address_pin - 3
        main_memory_size = 2 ** main_memory_size_power
        print(f"the main memory size is {main_memory_size} bytes")


retMemSize={"Bit":1,"Nibble":4,"Byte":8}
# print("what is the type of your query?\n1)Normal Query\n2)Type 1\n3)Type 2\n Enter the number.")
# type=input("enter the type number")
# space=input("enter the space in memory")
# addressed=input("enter how the memory is addressed")

# if(type ==1):
#     instruction=input("enter length of one instruction in bits")
#     register=input("enter length of register in bits")
#     normal_query(instruction,register,space,addressed)
# elif(type==2):
#     cpu_bits=input("how many bits is the cpu?")
#     address_memory=input("input how you would want to change the current addressable memory to any of the rest 3 options")
#     type1(cpu_bits,address_memory,space,addressed,retMemSize)
# elif(type==3):
#     cpu_bits=input("how many bits is the cpu?")
#     address_pin=input("how many address pins?")
#     address_memory=input("enter type of addressable memory")
#     type2(cpu_bits,address_pin,address_memory,retMemSize)
def i_o():
    print("------------------------------------------")
    print("----------------Welcome-------------------")
    print("------------------------------------------")
    print("Share initial input-->")
    memSpace=input("Memory Space(x b/B/kB/mB):")
    memType=input("Type of addressable memeory(Bit/Byte/Nibble/word_add):")
    print("Queries start")
    while(True):
        





        cont=input("Continue?(0/1)")
        if(cont=="0"):
            break