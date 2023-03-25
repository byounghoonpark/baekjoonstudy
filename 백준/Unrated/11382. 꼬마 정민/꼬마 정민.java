import java.util.Scanner;

public class Main{
    public static void main(String[]args){
        Scanner S = new Scanner(System.in);
        long A = S.nextLong();
        long B = S.nextLong();
        long C = S.nextLong();
        S.close();
        System.out.println(A+B+C);
    }
}