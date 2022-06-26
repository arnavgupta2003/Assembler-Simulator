import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class main {

	public static void main(String[] args) throws FileNotFoundException{
		// TODO Main I/O file
		
		//Local I/O Code (Stdin)
		Scanner sc = new Scanner(System.in);
		String line = sc.nextLine().strip();
		String[] in = line.split("\\s+");
//		for(String h:in) {
//			System.out.print(h+'_');//Debug Code
//		}
		
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
}


