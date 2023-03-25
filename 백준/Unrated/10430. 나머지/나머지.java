import java.util.Scanner;

public class Main{
    public static void main(String[]args){
        Scanner S = new Scanner(System.in);
        int A = S.nextInt();
        int B = S.nextInt();
        int C = S.nextInt();
        S.close();
        System.out.println((A+B)%C);
        System.out.println(((A%C) + (B%C))%C);
        System.out.println((A*B)%C);
        System.out.println(((A%C) * (B%C))%C);
        
    }
}