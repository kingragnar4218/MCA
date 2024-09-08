 //13-8-2024 first java program  
public class first{

  public static void main(String a[]) {

 //   System.out.println("Hello World");
  	System.out.print("harsh ");

  }
}

-----------------------------------------------------------
  public class sum{
  public static void main(String a[]) {  
    
  /*  int a1=5;
    int b=5;
    int c=a1+b;
    System.out.print(c);*/

    int i=Integer.parseInt(a[0]); 
    int j=Integer.parseInt(a[1]);

    int s=i+j;
    System.out.print(s);

    /* 
    int i=Integer.parseInt(a[0]); 
    int j=Integer.parseInt(a[1]); 

    int s1=i+j;
    int s2=i-j;
    int s3=i*j;
    int s4=i/j;

    System.out.println(s1);
    System.out.println(s2);
    System.out.println(s3);
    System.out.println(s4);

    */
   
  }
}


------------------------------------------------------------------------------------------
 //date 20-8-2024
 // leb A part program 3 no 2 
 import java.util.Scanner;  

public class user {

  public static void main(String[] args) {

    Scanner harsh = new Scanner(System.in);  

      System.out.println("entr number a");
      System.out.println("entr number b");

      String name = harsh.nextLine(); 

    System.out.println("name is: " + name);
  }
}
------------------------------------------------------------------------------------------
 //date 20-8-2024
// leb A part program 4

 import java.util.Scanner;  

public class Sumscanner {

  public static void main(String[] args) {

    Scanner sc= new Scanner(System.in); 
    

      System.out.println("Enter a ");
      int a=sc.nextInt();

      System.out.println("Enter b");
      int b=sc.nextInt();

      int  s1=a+b;

      //String name = harsh.nextLine(); 

    System.out.println("sum is: " + s1);
  }
}
------------------------------------------------------------------------------------------
 //date 20-8-2024
//pre leb a pro 5

 import java.util.Scanner;  

public class feet {

  public static void main(String[] args) {

    Scanner sc= new Scanner(System.in); 
    
    double m=sc.nextDouble();
    double f=m*3.28084;
    System.out.println("enter number"+f);

  }
}
------------------------------------------------------------------------------------------

   *
  ***
 *****
*******

 import java.util.Scanner;

public class looping {
    public static void main(String[] args) {
        Scanner sss = new Scanner(System.in);

        // Prompt user for input
        System.out.println("Enter number of rows: ");
        int row = sss.nextInt();

        // Loop for each row
        for (int i = 1; i <= row; i++) {

            // Print spaces before stars
            for (int j = i; j < row; j++) {
                System.out.print(" ");  // Use print instead of println to stay on the same line
            }

            // Print stars
            for (int j = 1; j <= (2 * i - 1); j++) {
                System.out.print("*");  // Print stars in the same row
            }

            // Move to the next line after printing stars
            System.out.println();
        }

        sss.close();  // Close the scanner
    }
}

 
