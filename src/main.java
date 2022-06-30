import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class main {

	public static void main(String[] args) throws FileNotFoundException{
		// TODO Main I/O file
		
		//Local I/O Code (Stdin)
		Scanner sc = new Scanner(System.in);
		int cnt=0;
        HashMap <String,Integer> Labelmapping = new HashMap <String,Integer>();
		while(sc.hasNextLine()) {
			String line = sc.nextLine().strip();
			String[] in = line.split("\\s+");
            String[] in2;
            int len=in.length;
            String output="";
			cnt++;
			boolean isLabel=false;
			if(in[0].charAt(in[0].length()-1)==':') {
				isLabel=true;
			}
            if (isLabel){
                Labelmapping.put(in[0], cnt);
                for(int i=1;i<len;i++){
                    in2=in[i];
                }
            }
			else{
                in2=in;
            }
            String opcode=returnOP(in2);
            String type=returnType(opcode);
            if (type=="A"){
                String reg1=returnReg(in2[2]);
                String reg2=returnReg(in2[3]);
                String reg3=returnReg(in2[4]);
                output=opcode+"00"+reg1+reg2+reg3;
            }
            else if(type=="B"){
                String reg1=returnReg(in2[2]);
                // checking if Imm is in the defined range
                String Imm;//handle binary

                output=opcode+reg1+Imm;
                 
            }/* 
            if(in[0]!="hlt"){
                System.output("Error: no hlt statement found");
            }*/

            else if(type=="C"){
                String reg1=returnReg(in2[2]);
                String reg2=returnReg(in2[3]);
                output=opcode+"00000"+reg1+reg2;
            }
            else if(type=="D"){
                String reg1=returnReg(in[2]);
                String Memadd;//handle variable
                output=opcode+reg1+Memadd;
            }
            else if(type=="E"){
                String Memadd;//handle label
                output=opcode+"000"+Memadd;
            }            
            else if(type=="F"){
                output=opcode+"00000"+"00000"+"0";
            }

		}		
//		//File I/O Code
//		File f = new File("");
//		Scanner sc_f = new Scanner(f);
//		while(sc_f.hasNextLine()) {
//			String line_f = sc_f.nextLine().strip();
//			String[] in_f = line.split("\\s+");
//		}
		

	}

    public static String returnType(String opcode){
        String [] Atype={"10000","10001","10110","11010","11011","11100"};
        String [] Btype={"10010","11001"};
        String [] Ctype ={"10011","10111","11101","11110"};
        String [] Dtype={"10100","10101"};
        String [] Etype={"11111","01100","01101","01111"};
        String [] Ftype ={"01010"};
        if(Arrays.asList(Atype).contains(opcode)){
            return "A";
        }
        else if(Arrays.asList(Btype).contains(opcode)){
            return "B";
        }
        else if(Arrays.asList(Ctype).contains(opcode)){
            return "C";
        }
        else if(Arrays.asList(Dtype).contains(opcode)){
            return "C";
        }
        else if(Arrays.asList(Etype).contains(opcode)){
            return "E";
        }
        else if(Arrays.asList(Ftype).contains(opcode)){
            return "F";
        }
        else{
            return "Error";
        }
    }

	public static String returnOP(String[] code){
        switch (code[0]){
            case "add":
                return "10000";
            case "sub":
                return "10001";
            case "ld":
                return "10100";
            case "st":
                return "10101";
            case "mul":
                return "10110";
            case "div":
                return "10111";
            case "rs":
                return "11000";
            case "ls":
                return "11001";
            case "xor":
                return "11010";
            case "or":
                return "11011";
            case "and":
                return "11100";
            case "not":
                return "11101";
            case "cmp":
                return "11110";
            case "jmp":
                return "11111";
            case "jlt":
                return "01100";
            case "jgt":
                return "01101";
            case "je":
                return "01111";
            case "hlt":
                return "01010";
            case "mov":
                switch (code[2].charAt(0)){
                    case '#':
                        return "10010";       
                    case 'r':
                        return "10011";    
                }     

            }
            return "Error: give eligible instruction";
    }
	
	 public static String returnReg(String regs){
	        switch (regs){
	            case "R0":
	                return "000";
	            case "R1":
	                return "001";
	            case "R2":
	                return "010";
	            case "R3":
	                return "011";
	            case "R4":
	                return "100";
	            case "R5":
	                return "101";
	            case "R6":
	                return "110";
	            case "FLAGS":
	                return "111";
	        }
	        return "Error: give eligible Register";
	    }
    public static String varCheck(String code[0]){
        if(code[0]!="var"){
            return "Error: give variable";
        }
        else if(code[0].length==16){
            return "Error: give 16 bits var value";
        }
        
    }
    // public static String hltCheck(String last_ke_3_check){
    //     if(last_ke_3_check=="hlt"){
    //         return ;
    //     }else{
    //         return "Error: give hlt";
    //     }
    // } 
    public static String error(String code[0]){
        switch (code[0]){
            case : 
        }
    }
}

public static bool checkFlag(String regs){
    if (regs=="111"){
        return true;
    }
    return false;
}





public static void errorgen(String Type,int pc){
    if (Type=="typo"){
        println("Typo in line $pc");
    }
    else if(Type=="undefined_var"){
        println("Used undefined variable in line $pc");
    }else if(Type=="undefined_label"){
        println("Error: Used undefined label in line $pc");
    }
    else if(Type=="illegal_flag"){
        println("Error: illegal flag usage in line $pc");
    }
    else if(Type=="immediateVal"){
        println("Error: Immediate value out of given range in line $pc");
    }
    else if(Type=="label_as_var"){
        println("Error: Used label as flag in line $pc");
    }
    else if(Type=="var_as_label"){
        println("Error: Used var as label in line $pc");
    }
    else if(Type=="var_declared_between"){
        println("Error: Variable not declared at the beginning in line $pc");
    }
    else if(Type=="hlt_missing"){
        println("Error: hlt statement missing in line $pc");
    }
    else if(Type=="hlt_not_at_end"){
        println("Error: hlt not used at the end in line $pc");
    }
}
