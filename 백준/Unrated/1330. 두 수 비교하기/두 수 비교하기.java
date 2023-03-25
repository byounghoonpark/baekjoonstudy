import java.util.Scanner;

public class Main{
    public static void main(String[]args){
        Scanner S = new Scanner(System.in);
        int A = S.nextInt();
        int B = S.nextInt();
        S.close();
        if(A>B)
            System.out.println(">");
        
        else if(A<B)
            System.out.println("<");
        
        else
            System.out.println("==");
        
        
    }
}