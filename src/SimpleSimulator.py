import sys
import math


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




