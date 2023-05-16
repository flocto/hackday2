import java.util.*;
import java.io.*;

public class Eduardo {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(new File("eduardo.dat"));
        int N = Integer.parseInt(sc.nextLine());

        for(int I = 0; I < N; I++){
            char[] msg = sc.nextLine().toCharArray();
            boolean first = true;

            for(char c : msg){
                String enc = Integer.toBinaryString(c);
                while (enc.length() < 8) enc = "0" + enc;
                enc = enc.substring(4) + enc.substring(0, 4);
                enc = enc.replace("0", "A").replace("1", "B");
                if(first) first = false;
                else System.out.print(" ");
                System.out.print(enc);
            }
            System.out.println();
        }
    }
}