//import java.io.File;
//import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class SimpleAssembler {
	//ArrayList for STDOut
	public static ArrayList<String> error_list = new ArrayList<String>();
    public static ArrayList<String> finalBinary = new ArrayList<String>();
	public static String[] reservedWords = {"add","sub","mov","ld","st","mul","div",
											"rs","ls","xor","or","and","not","cmp",
											"jmp","jlt","jgt","je","hlt","FLAGS",
											"R0","R1","R2","R3","R4","R6","R5","var"};
	
	public static void main(String[] args) {
		// TODO Main I/O file
		
		//var
		
		//Local I/O Code (Stdin)
		Scanner sc = new Scanner(System.in);
			
		
		int line_counter=1;
		int program_counter=0;
		boolean Notvar=false;
		int hlt_count=0;
		
		HashMap <String,Integer> Labels = new HashMap <String,Integer>();
        ArrayList<String> instructions = new ArrayList<String>();
        HashMap<String,Integer> variables = new HashMap<String,Integer>();

        
        //Input Handle
		while(sc.hasNextLine()) {//Taking input
			String line = sc.nextLine().strip();
			String[] in = line.split(" ");
			
			//Handling Extra Space error
			boolean isBlankAvailable = false;
			for(String h:in) {
				if(h.isBlank()||h.isEmpty()||h.equals(" ")) {
					genError("Faulty number of spaces",line_counter);
					isBlankAvailable=true;
					break;
				}
			}
			
			
			if(isBlankAvailable) {
				continue;
			}
			
			//Var def for checking input
			boolean isLabel=false;boolean isVar = false;boolean isInstruct = false;
			
			//Checking for Type of input
			if(line.isBlank()||line.isEmpty()) {
				instructions.add("@#empty");//placeholder for empty
				program_counter--;
			}
            else if(in[0].charAt(in[0].length()-1)==':') {
				isLabel=true;
                Notvar=true;
                if(Labels.keySet().contains(in[0])){
                    genError("generror", line_counter);
					line_counter++;program_counter++;
                    continue;
                }
                else if(variables.keySet().contains(in[0])){
                    genError("label_as_var", line_counter);
					line_counter++;program_counter++;
                    continue;
                }
                else if(Arrays.asList(SimpleAssembler.reservedWords).contains(in[0])){
                    genError("generror", line_counter);
					line_counter++;program_counter++;
                    continue;
                }
			}
            else if(in[0].equals("var")) {
				isVar=true;
                program_counter--;
				if(Notvar){
                    genError("var_declared_between", line_counter);
					line_counter++;program_counter++;
                    continue;
                }
                else if(variables.keySet().contains(in[1])){
                    genError("generror", line_counter);
					line_counter++;program_counter++;
                    continue;
                }
                else if(Labels.keySet().contains(in[1])){
                    genError("var_as_label", line_counter);
					line_counter++;program_counter++;
                    continue;
                }
                else if(Arrays.asList(SimpleAssembler.reservedWords).contains(in[1])){
                    genError("generror", line_counter);
					line_counter++;program_counter++;
                    continue;
                }

				
			}
            else if(in[0].equals("hlt")) {
            	isInstruct=true;
                Notvar=true;
                hlt_count++;
            }
            else {
				isInstruct = true;
                Notvar=true;
			}
			
			//Commit to lists
			if(isVar) {
				variables.put(in[1], program_counter+1);
			}else if(isLabel) {
				Labels.put(in[0], program_counter);
				instructions.add(genLine(in,1,in.length-1));
			}else if(isInstruct) {
				instructions.add(genLine(in,0,in.length-1));
			}
			
			
			
			line_counter++;program_counter++;
		}	
		sc.close();
		
		//Ans Computation Handle
		
		if(hlt_count==0) {
			genError("hlt_missing", line_counter);
		}

		for(int insCount=0;insCount<instructions.size();insCount++) {
			String line = instructions.get(insCount);

			
			int cnt=insCount+variables.size()+1;
            if(line.equals("@#empty")){
                continue;
            }
            
            //Try Block
			try {
				
	            String in[] = line.split(" ");
					
				//Getters
				String OPCode = returnOP(in,cnt);
	            if (OPCode=="_"){
	                continue;
	            }
				String instructionType = returnType(OPCode);
				
				//#Check for bit errors 
				
				//Setters
				if (instructionType.equals("A")){
					//Registers Load
	                String reg1=returnReg(in[1],cnt);
	                String reg2=returnReg(in[2],cnt);
	                String reg3=returnReg(in[3],cnt);
	                if(reg1=="_"||reg2=="_"||reg3=="_"){
	                    continue;
	                }
	                
	                //Error handle
	                if(checkFlag(reg1) || checkFlag(reg2) || checkFlag(reg3)){
	                    genError("illegal_flag",cnt);
	                }else {
	                //Function Out
	                finalBinary.add(OPCode+"00"+reg1+reg2+reg3);
	                }
	            }
	            else if(instructionType.equals("B")){
	            	//Registers Load
	                String reg1=returnReg(in[1],cnt);
	                if(reg1=="_"){
	                    continue;
	                }
	                //Error handle
	                if(checkFlag(reg1)){
	                    genError("illegal_flag",cnt);
	                    continue;
	                }
	                //	Imm Handle
	                String Imm; 
	                String Imm_val_String = in[2].substring(1, in[2].length());//Took decimal Input
	                int Imm_val_Integer = Integer.parseInt(Imm_val_String);//Converted to Integer
	                
	                if(Imm_val_Integer>255 || Imm_val_Integer<0){
	                    genError("immediateVal", cnt);
	                    continue;
	                }
	                
	                String Imm_val_Binary = Integer.toBinaryString(Imm_val_Integer);//convert to bin 
	                Imm=String.format("%08d", Integer.parseInt(Imm_val_Binary));//convert to 8bit
	                
	                
	                //Function Out
	                finalBinary.add(OPCode+reg1+Imm);
	            }
	            else if(instructionType.equals("C")){
	            	//Registers Load
	                String reg1=returnReg(in[1],cnt);
	                String reg2=returnReg(in[2],cnt);
	                if(reg1=="_"||reg2=="_"){
	                    continue;
	                }
	                //Error handle
	                if(OPCode=="10011"){
	                    if(checkFlag(reg2)){
	                        genError("illegal_flag",cnt);
	                        continue;
	                    }
	                }
	                else{
	                    if(checkFlag(reg1) || checkFlag(reg2)){
	                    	genError("illegal_flag",cnt);
	                        continue;
	                    }else {
	                    	//Function Out
	                        finalBinary.add(OPCode+"00000"+reg1+reg2);
	                    }
	                }
	                
	                
	            }
	            else if(instructionType.equals("D")){
	            	//Registers Load
	                String reg1=returnReg(in[1],cnt);
	                String Memadd = null;
	                if(reg1=="_"){
	                    continue;
	                }
	                //Error Handle + processing
	                if(checkFlag(reg1)){
	                    genError("illegal_flag",cnt);
	                }
	                else {
		                if ((variables.keySet().contains(in[2]))){
		                    int variable_val=variables.get(in[2])+program_counter;
		                    String bin = Integer.toBinaryString(variable_val);
		                    Memadd=String.format("%08d", Integer.parseInt(bin));
		
		                }else{
		                    if((Labels.keySet().contains(in[2]))){
		                    	genError("label_as_var", cnt);
		                    }else{
		                    	genError("undefined_var", cnt);
		                    }
		                }
		                //Function Out
		                finalBinary.add(OPCode+reg1+Memadd);
	                }
	            }
	            else if(instructionType.equals("E")){
	            	String Memadd=null;
	            	
	            	//Error handle + processing
	            	if ((Labels.keySet().contains(in[1]))){
	                    int label_val=Labels.get(in[1]);
	                    String bin = Integer.toBinaryString(label_val);
	                    Memadd=String.format("%08d", Integer.parseInt(bin));
	                    
	                    //Function Out
	                	finalBinary.add(OPCode+"000"+Memadd);
	                }
	                else{
	                    if((variables.keySet().contains(in[1]))){
	                    	genError("var_as_label", cnt);
	                    }
	                    else{
	                    	genError("undefined_label", cnt);
	                    }
	                }
	            }else if(instructionType.equals("F")){
	            	
	            	//Error handle
	            	if(insCount+1!=program_counter){
	                    genError("hlt_not_at_end", cnt);
	                }
	                else {            	
	            	//Function Out
	                finalBinary.add(OPCode+"00000"+"00000"+"0");
	                }
	            }
			}catch(Exception e) {
				genError("Gen-Error", cnt);
			}
		}
		
		//STDOut
		if(error_list.size()!=0) {
			for(String h:error_list) {
				System.out.println(h);
			}
		}else {
			for(String h:finalBinary) {
				System.out.println(h);
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
	 public static void genError(String Type,int program_counter){//check hlt error
	        
	        if (Type.equals("Typo")) {
	            String error_line=String.format("Error @~%d: Typo in name of register or instruction", program_counter);
	            error_list.add(error_line);
	            
	            // println("Typo in line $program_counter");
	        }
	        else if(Type.equals("undefined_var")){
	        	String error_line=String.format("Error @~%d: Used undefined variable ", program_counter);
	            error_list.add(error_line);
	            // println("Used undefined variable in line $program_counter");
	        }else if(Type.equals("undefined_label")){
	        	String error_line=String.format("Error @~%d: Used undefined label ", program_counter);
	            error_list.add(error_line);
	            // println("Error: Used undefined label in line $program_counter");
	        }
	        else if(Type.equals("illegal_flag")){
	        	String error_line=String.format("Error @~%d: Illegal flag usage ", program_counter);
	            error_list.add(error_line);
	            // println("Error: illegal flag usage in line $program_counter");
	        }
	        else if(Type.equals("immediateVal")){
	        	String error_line=String.format("Error @~%d: Immediate value out of given range in line", program_counter);
	            error_list.add(error_line);
	            // println("Error: Immediate value out of given range in line $program_counter");
	        }
	        else if(Type.equals("label_as_var")){
	        	String error_line=String.format("Error @~%d: Used label as varaible ", program_counter);
	            error_list.add(error_line);
	            // println("Error: Used label as flag in line $program_counter");
	        }
	        else if(Type.equals("var_as_label")){
	        	String error_line=String.format("Error @~%d: Used variable as label ", program_counter);
	            error_list.add(error_line);
	            // println("Error: Used var as label in line $program_counter");
	        }
	        else if(Type.equals("var_declared_between")){
	        	String error_line=String.format("Error @~%d: Variable not declared at the beginning in line", program_counter);
	            error_list.add(error_line);
	            // println("Error: Variable not declared at the beginning in line $program_counter");
	        }
	        else if(Type.equals("hlt_missing")){
	        	String error_line=String.format("Error @~%d: hlt statement missing ", program_counter);
	            error_list.add(error_line);
	            // println("Error: hlt statement missing in line $program_counter");
	        }
	        else if(Type.equals("hlt_not_at_end")){
	        	String error_line=String.format("Error @~%d: hlt not used at the end ", program_counter);
	            error_list.add(error_line);
	            // println("Error: hlt not used at the end in line $program_counter");
	        }
            else{
                String error_line=String.format("Error @~%d: General Syntax error", program_counter);
	            error_list.add(error_line);
            }
	    } 
	public static boolean checkFlag(String regs){
	     if (regs=="111"){
	         return true;
	     }
	     return false;
	} 
	    

    public static String genLine(String[] arr,int st,int end) {
		String ans="";
		for(int i=st;i<=end;i++) {
			ans+=(arr[i]+" ");
		}
		return ans.strip();
	}

    public static String returnType(String OPCode){
        String [] Atype={"10000","10001","10110","11010","11011","11100"};
        String [] Btype={"10010","11001","11000"};
        String [] Ctype ={"10011","10111","11101","11110"};
        String [] Dtype={"10100","10101"};
        String [] Etype={"11111","01100","01101","01111"};
        String [] Ftype ={"01010"};
        if(Arrays.asList(Atype).contains(OPCode)){
            return "A";
        }
        else if(Arrays.asList(Btype).contains(OPCode)){
            return "B";
        }
        else if(Arrays.asList(Ctype).contains(OPCode)){
            return "C";
        }
        else if(Arrays.asList(Dtype).contains(OPCode)){
            return "D";
        }
        else if(Arrays.asList(Etype).contains(OPCode)){
            return "E";
        }
        else if(Arrays.asList(Ftype).contains(OPCode)){
            return "F";
        }
        else{
            return "-";
        }
    }

	public static String returnOP(String[] instruction,int cnt){
        switch (instruction[0]){
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
                switch (instruction[2].charAt(0)){
                    case '$':
                        return "10010";       
                    case 'R':
                        return "10011";    
                };     

        }
            genError("Typo", cnt);
            return "_";
			
            
    }
	
	 public static String returnReg(String register,int cnt){
	        switch (register){
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
            genError("Typo", cnt);
	        return "_";
	    }
}