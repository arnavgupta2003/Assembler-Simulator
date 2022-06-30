import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Scanner;

public class main {
	//ArrayList for STDOut
	public static ArrayList<String> error_list = new ArrayList<String>();
    public static ArrayList<String> finalBinary = new ArrayList<String>();
	
	public static void main(String[] args) throws FileNotFoundException{
		// TODO Main I/O file
		
		//Local I/O Code (Stdin)
		Scanner sc = new Scanner(System.in);
		
		
		int line_counter=0;
        boolean ishlt=false;
		boolean isBeingGivenVar = false;
		boolean varGiven=false;
		
		
		HashMap <String,Integer> Labels = new HashMap <String,Integer>();
        ArrayList<String> instructions = new ArrayList<String>();
        HashMap<String,Integer> variables = new HashMap<String,Integer>();

        
        //Input Handle
		while(sc.hasNextLine()) {//Taking input
			String line = sc.nextLine().strip();
			String[] in = line.split("\\s+");//change for error gens
			
			//Var def for checking input
			boolean isLabel=false;boolean isVar = false;boolean isInstruct = false;
			
			//Checking for Type of input
			if(line.isBlank()||line.isEmpty()) {
				continue;
			}else if(in[0].charAt(in[0].length()-1)==':') {
				isLabel=true;
				if(isBeingGivenVar && !varGiven) {
					varGiven=true;
				}else if(isBeingGivenVar) {
					//Raise var error
				}
			}else if(in[0]=="var") {
				isVar=true;
				if(!isBeingGivenVar) {
					isBeingGivenVar=true;
				}
			}else if(in[0]=="hlt") {
				ishlt=true;
				if(isBeingGivenVar && !varGiven) {
					varGiven=true;
				}else if(isBeingGivenVar) {
					//Raise var error
				}
			}else {
				isInstruct = true;
				if(isBeingGivenVar && !varGiven) {
					varGiven=true;
				}else if(isBeingGivenVar) {
					//Raise var error
				}
			}
			
			//Commit to lists
			if(isVar) {
				variables.put(in[0], line_counter);
			}else if(isLabel) {
				Labels.put(in[0], line_counter);
			}else if(isInstruct) {
				instructions.add(genLine(in));
			}
			
			
			
			line_counter++;
		}	
		
		
		//Ans Computation Handle
		for(int cnt=0;cnt<instructions.size();cnt++) {
			String line = instructions.get(cnt);
			String in[] = line.split(" ");
			
			
			//Getters
			String OPCode = returnOP(in);
			String instructionType = returnType(OPCode);
			
			//#Check for bit errors 
			
			//Setters
			if (instructionType=="A"){
				//Registers Load
                String reg1=returnReg(in[1]);
                String reg2=returnReg(in[2]);
                String reg3=returnReg(in[3]);
                
                //Function Out
                finalBinary.add(OPCode+"00"+reg1+reg2+reg3);
            }
            else if(instructionType=="B"){
            	//Registers Load
                String reg1=returnReg(in[1]);
                
                //	Imm Handle
                String Imm; 
                String Imm_val_String = in[2].substring(1, in[0].length()-1);//Took decimal Input
                int Imm_val_Integer = Integer.parseInt(Imm_val_String);//Converted to Integer
                String Imm_val_Binary = Integer.toBinaryString(Imm_val_Integer);//convert to bin 
                Imm=String.format("%08d", Integer.parseInt(Imm_val_Binary));//convert to 8bit
                
                //Function Out
                finalBinary.add(OPCode+reg1+Imm);
                
            }//Contd.
            else if(instructionType=="C"){
            	//Registers Load
                String reg1=returnReg(in[1]);
                String reg2=returnReg(in[2]);
                
                //Function Out
                finalBinary.add(OPCode+"00000"+reg1+reg2);
            }
            else if(instructionType=="D"){
            	//Registers Load
                String reg1=returnReg(in[1]);
                String Memadd;//handle variable
                
              //Function Out
                //finalBinary=OPCode+reg1+Memadd;
            }
            else if(instructionType=="E"){
                //int Mem=Labelmapping.get(in[1]);

                String Memadd;//handle binary
                
              //Function Out
               // finalBinary=OPCode+"000"+Memadd;
            }            
            else if(instructionType=="F"){
            	
            	//Function Out
                finalBinary.add(OPCode+"00000"+"00000"+"0");
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
	
	public static void genError(String Type,int programCounter){
	    
	    if (Type=="typo"){
	        String error_line="Error: Typo in line "+ String.valueOf(programCounter);
	        error_list.add(error_line);
	        // println("Typo in line $pc");
	    }
	    else if(Type=="undefined_var"){
	        String error_line="Error: Used undefined variable in line "+ String.valueOf(programCounter);
	        error_list.add(error_line);
	        // println("Used undefined variable in line $pc");
	    }else if(Type=="undefined_label"){
	        String error_line="Error: Typo in line "+ String.valueOf(programCounter);
	        error_list.add(error_line);
	        // println("Error: Used undefined label in line $pc");
	    }
	    else if(Type=="illegal_flag"){
	        String error_line="Error: illegal flag usage in line "+ String.valueOf(programCounter);
	        error_list.add(error_line);
	        // println("Error: illegal flag usage in line $pc");
	    }
	    else if(Type=="immediateVal"){
	        String error_line="Error: Immediate value out of given range in line "+ String.valueOf(programCounter);
	        error_list.add(error_line);
	        // println("Error: Immediate value out of given range in line $pc");
	    }
	    else if(Type=="label_as_var"){
	        String error_line="Error: Used label as flag in line "+ String.valueOf(programCounter);
	        error_list.add(error_line);
	        // println("Error: Used label as flag in line $pc");
	    }
	    else if(Type=="var_as_label"){
	        String error_line="Error: Used var as label in line "+ String.valueOf(programCounter);
	        error_list.add(error_line);
	        // println("Error: Used var as label in line $pc");
	    }
	    else if(Type=="var_declared_between"){
	        String error_line="Error: Variable not declared at the beginning in line  "+ String.valueOf(programCounter);
	        error_list.add(error_line);
	        // println("Error: Variable not declared at the beginning in line $pc");
	    }
	    else if(Type=="hlt_missing"){
	        String error_line="Error: hlt statement missing in line $pc "+ String.valueOf(programCounter);
	        error_list.add(error_line);
	        // println("Error: hlt statement missing in line $pc");
	    }
	    else if(Type=="hlt_not_at_end"){
	        String error_line="Error: hlt not used at the end in line $pc "+ String.valueOf(programCounter);
	        error_list.add(error_line);
	        // println("Error: hlt not used at the end in line $pc");
	    }
	}    
	    
	public static String genLine(String[] arr) {
		String ans="";
		for(String h:arr) {
			ans+=(h+" ");
		}
		return ans.strip();
	}

    public static String returnType(String OPCode){
        String [] Atype={"10000","10001","10110","11010","11011","11100"};
        String [] Btype={"10010","11001"};
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
            return "C";
        }
        else if(Arrays.asList(Etype).contains(OPCode)){
            return "E";
        }
        else if(Arrays.asList(Ftype).contains(OPCode)){
            return "F";
        }
        else{
            return "Error in OPCode - Type";
        }
    }

	public static String returnOP(String[] instruction){
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
                    case '#':
                        return "10010";       
                    case 'r':
                        return "10011";    
                }     

            }
            return "Error in OPCode";
    }
	
	 public static String returnReg(String register){
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
	        return "Error in Reg";
	    }
}


