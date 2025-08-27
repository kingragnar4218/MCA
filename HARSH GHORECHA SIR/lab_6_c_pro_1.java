import java.util.Scanner;

public class lab_6_c_pro_1 {
    public static void main(String[] args) {
        try (Scanner sc = new Scanner(System.in)) {
            System.out.println("Enter three numbers:");
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            int second;

            if ((a > b && a < c) || (a > c && a < b)) {
                second = a;
            } else if ((b > a && b < c) || (b > c && b < a)) {
                second = b;
            } else {
                second = c;
            }

            System.out.println(" second largest number is: " + second);
        }

        
    }
}
