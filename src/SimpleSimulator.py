import sys
import math


def operatorCall(List,pc):
    if (List[pc][:5] == "10000"):
        Addition(List, i)

    elif (List[pc][:5] == "10001"):
        Subtraction(List, i)

    elif (List[pc][:5] == "10010"):
        Move_Immediate(List, i)

    elif (List[pc][:5] == "10011"):
        Move_Register(List, i)

    elif (List[pc][:5] == "10100"):
        Load(List, i)

    elif (List[pc][:5] == "10101"):
        Store(List, i)

    elif (List[pc][:5] == "10110"):
        Multiply(List, i)

    elif (List[pc][:5] == "10111"):
        Divide(List, i)

    elif (List[pc][:5] == "11000"):
        Right_Shift(List, i)

    elif (List[pc][:5] == "11001"):
        Left_Shift(List, i)

    elif (List[pc][:5] == "11010"):
        Exclusive_OR(List, i)

    elif (List[pc][:5] == "11011"):
        Or(List, i)

    elif (List[pc][:5] == "11100"):
        And(List, i)

    elif (List[pc][:5] == "11101"):
        Invert(List, i)

    elif (List[pc][:5] == "11110"):
        Compare(List, i)

    elif (List[pc][:5] == "11111"):
        Unconditional_Jump(List, i)

    elif (List[pc][:5] == "01100"):
        Jump_If_Less_Than(List, i)

    elif (List[pc][:5] == "01101"):
        Jump_If_Greater_Than(List, i)

    elif (List[pc][:5] == "01111"):
        Jump_If_Equal(List, i)

    elif (List[pc][:5] == "01010"):
        Halt(List, i)





