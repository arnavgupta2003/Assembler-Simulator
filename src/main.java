import java.util.Scanner;

public class main {

	public static void main(String[] args) {
		// TODO Main I/O file
		Scanner sc = new Scanner(System.in);
		String line = sc.nextLine().strip();
		String[] in = line.split(" ");
		System.out.println(in[0]);

	}

}
