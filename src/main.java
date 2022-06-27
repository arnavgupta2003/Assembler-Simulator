import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class main {

	public static void main(String[] args) throws FileNotFoundException{
		// TODO Main I/O file
		
		//Local I/O Code (Stdin)
		Scanner sc = new Scanner(System.in);
		int cnt=0;
		while(sc.hasNextLine()) {
			String line = sc.nextLine().strip();
			String[] in = line.split("\\s+");
			cnt++;
			boolean isLabel=false;
			if(in[0].charAt(in[0].length()-1)==':') {
				isLabel=true;
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
            return "Error";
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
	        return "Error";
	    }
}


