import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class main {

	public static void main(String[] args) throws FileNotFoundException{
		// TODO Main I/O file
		
		//Local I/O Code (Stdin)
		Scanner sc = new Scanner(System.in);
		int cnt=0;
        HashMap <String,Integer> Labelmapping = new HashMap <String,Integer>();
        HashMap <String,Integer> Variablemapping = new HashMap <String,Integer>();
        int no_lines=0;
		while(sc.hasNextLine()) {
			String line = sc.nextLine().strip();
			String[] in = line.split("\\s+");//change for error gens
            String[] in2 = new String[in.length];
            int len=in.length;
            String output="";
			cnt++;
			boolean isLabel=false;
            if (in[0]=="var"){
                errorgen("Var_used",cnt);

            }
            if(cnt==no_lines&&in[0]!="hlt"){
                errorgen("hlt_missing",cnt);
            }
			if(in[0].charAt(in[0].length()-1)==':') {
				isLabel=true;
			}
            if (isLabel){
                Labelmapping.put(in[0], cnt);
                int j=0;
                for(int i=1;i<in.length;i++){
                    in2[j]=in[i];
                    j++;
                }
            }else{
            	int j=0;
            	for(int i=0;i<in.length;i++){
                    in2[j]=in[i];
                    j++;
                }
            }
            String opcode=returnOP(in2,cnt);
            String type=returnType(opcode);
            if (type=="A"){
                String reg1=returnReg(in2[1],cnt);
                String reg2=returnReg(in2[2],cnt);
                String reg3=returnReg(in2[3],cnt);
                if(checkFlag(reg1) || checkFlag(reg2) || checkFlag(reg3)){
                    errorgen("illegal_flag",cnt);
                }
                output=opcode+"00"+reg1+reg2+reg3;
            }
            else if(type=="B"){
                String reg1=returnReg(in2[1],cnt);
                if(checkFlag(reg1)){
                    errorgen("illegal_flag",cnt);
                }

                String Imm; 
                String Imm_val = in2[2].substring(1, in2[0].length()-1);//handle binary
                int temp = Integer.parseInt(Imm_val);
                if(temp>255&&temp<0){
                    errorgen("immediateVal",cnt);
                }
                String bin = Integer.toBinaryString(temp);//convert to bin;//convert to 8 bit
                Imm=String.format("%08d", Integer.parseInt(bin));
                output=opcode+reg1+Imm;
                 
            }

            else if(type=="C"){
                String reg1=returnReg(in2[1],cnt);
                String reg2=returnReg(in2[2],cnt);
                if(opcode=="10011"){
                    if(checkFlag(reg2)){
                        errorgen("illegal_flag",cnt);
                    }
                }
                else{
                    if(checkFlag(reg1) || checkFlag(reg2)){
                        errorgen("illegal_flag",cnt);
                    }
                }
                output=opcode+"00000"+reg1+reg2;
            }
            else if(type=="D"){
                String reg1=returnReg(in[1],cnt);
                if(checkFlag(reg1)){
                    errorgen("illegal_flag",cnt);
                }

                String Memadd;
                if ((Variablemapping.keySet().contains(in[2]))){
                    int variable_val=Variablemapping.get(in[2]);
                    String bin = Integer.toBinaryString(variable_val);
                    Memadd=String.format("%08d", Integer.parseInt(bin));

                }
                else{
                    if((Labelmapping.keySet().contains(in[2]))){
                        errorgen("label_as_var", cnt);
                    }
                    else{
                        errorgen("undefined_var", cnt);
                    }
                }
                output=opcode+reg1+Memadd;
            }
            else if(type=="E"){
                String Memadd;
                if ((Labelmapping.keySet().contains(in[2]))){
                    int label_val=Labelmapping.get(in[2]);
                    String bin = Integer.toBinaryString(label_val);
                    Memadd=String.format("%08d", Integer.parseInt(bin));

                }
                else{
                    if((Variablemapping.keySet().contains(in[2]))){
                        errorgen("var_as_label", cnt);
                    }
                    else{
                        errorgen("undefined_label", cnt);
                    }
                }

                output=opcode+"000"+Memadd;
            }            
            else if(type=="F"){
                if(cnt!=no_lines){
                    errorgen("hlt_not_at_end", cnt);
                }
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
            return "_";
        }
    }

	public static String returnOP(String[] code,int cmt){
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
            return "_";
            errorgen("Typo", cmt);
    }
	
	 public static String returnReg(String regs,int cmt){
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

        public static boolean checkFlag(String regs){
            if (regs=="111"){
                return true;
            }
            return false;
        }
        public static void errorgen(String Type,int pogc){
        List error_list = new ArrayList();
        String pc=String.valueOf(pogc);
        if (Type=="Typo"){
            String error_line="Error: Typo in line "+ pc;
            error_list.add(error_line);
            // println("Typo in line $pc");
        }
        else if(Type=="undefined_var"){
            String error_line="Error: Used undefined variable in line "+ pc;
            error_list.add(error_line);
            // println("Used undefined variable in line $pc");
        }else if(Type=="undefined_label"){
            String error_line="Error: Typo in line "+ pc;
            error_list.add(error_line);
            // println("Error: Used undefined label in line $pc");
        }
        else if(Type=="illegal_flag"){
            String error_line="Error: illegal flag usage in line "+ pc;
            error_list.add(error_line);
            // println("Error: illegal flag usage in line $pc");
        }
        else if(Type=="immediateVal"){
            String error_line="Error: Immediate value out of given range in line "+ pc;
            error_list.add(error_line);
            // println("Error: Immediate value out of given range in line $pc");
        }
        else if(Type=="label_as_var"){
            String error_line="Error: Used label as flag in line "+ pc;
            error_list.add(error_line);
            // println("Error: Used label as flag in line $pc");
        }
        else if(Type=="var_as_label"){
            String error_line="Error: Used var as label in line "+ pc;
            error_list.add(error_line);
            // println("Error: Used var as label in line $pc");
        }
        else if(Type=="var_declared_between"){
            String error_line="Error: Variable not declared at the beginning in line  "+ pc;
            error_list.add(error_line);
            // println("Error: Variable not declared at the beginning in line $pc");
        }
        else if(Type=="hlt_missing"){
            String error_line="Error: hlt statement missing in line "+ pc;
            error_list.add(error_line);
            // println("Error: hlt statement missing in line $pc");
        }
        else if(Type=="hlt_not_at_end"){
            String error_line="Error: hlt not used at the end in line "+ pc;
            error_list.add(error_line);
            // println("Error: hlt not used at the end in line $pc");
        }
    }
}

