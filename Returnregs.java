public class Returnregs {
    public static String returnregisters(String regs){
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
