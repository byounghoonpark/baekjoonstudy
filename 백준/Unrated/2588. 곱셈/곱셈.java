import java.util.Scanner;

public class Main{
    public static void main(String[]args){
        Scanner S = new Scanner(System.in);
        int A = S.nextInt();
        int B = S.nextInt();
        S.close();
        System.out.println(A*(B%10));
        System.out.println(A*(B%100/10));
        System.out.println(A*(B/100));
        System.out.println(A*B);
    }
}