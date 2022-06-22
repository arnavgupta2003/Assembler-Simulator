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
}
