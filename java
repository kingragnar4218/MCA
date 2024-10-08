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

 =======================================================================================================


  //leb 3 no A 

  import java.util.Scanner;

public class stud {
    public static void main(String[] args) {
        // Create a Scanner object for input
        Scanner scanner = new Scanner(System.in);

        // Create an array to store marks for 5 subjects
        int[] marks = new int[5];

        // Ask the user to input marks for 5 subjects
        System.out.println("Enter the marks obtained in 5 subjects:");
        int totalMarks = 0;
        for (int i = 0; i < 5; i++) {
            System.out.print("Subject " + (i + 1) + ": ");
            marks[i] = scanner.nextInt();
            totalMarks += marks[i];  // Calculate the total marks
        }

        // Calculate the percentage
        float percentage = (float) totalMarks / 5;

        // Display the percentage
        System.out.println("Percentage: " + percentage + "%");

        // Determine the division based on the percentage
        if (percentage >= 60) {
            System.out.println("Division: First");
        } else if (percentage >= 50 && percentage <= 59) {
            System.out.println("Division: Second");
        } else if (percentage >= 40 && percentage <= 49) {
            System.out.println("Division: Third");
        } else {
            System.out.println("Division: Fail");
        }

        // Close the scanner
        scanner.close();
    }
}
==================================================================================

 // leb 3 no b 

 import java.util.Scanner;

public class oddeven {
    public static void main(String[] args) {
        // Create a Scanner object for input
        Scanner scanner = new Scanner(System.in);

        // Ask the user to input a number
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();

        // Check if the number is even or odd
        if (number % 2 == 0) {
            System.out.println(number + " is even.");
        } else {
            System.out.println(number + " is odd.");
        }

        // Close the scanner
        scanner.close();
    }
}
========================================================================================================================

 // prime number 

 import java.util.Scanner;
public class prime {
    public static void main(String[] args) {
        int number = new Scanner(System.in).nextInt(); 
        boolean isPrime = number > 1;

        for (int i = 2; i <= Math.sqrt(number) && isPrime; i++) {
            isPrime = number % i != 0;  
        }
        System.out.println(number + (isPrime ? " is a prime number." : " is not a prime number."));
    }
}

// import java.util.Scanner;

// public class prime  {
//     public static void main(String[] args) {
//         Scanner scanner = new Scanner(System.in);

//         int start = scanner.nextInt();
//         int  end = scanner.nextInt();

//         for (int i = start; i <= end; i++) {
//             if (i > 1) {  
//                 boolean isPrime = true;               
                
//                 for (int j = 2; j <= Math.sqrt(i); j++) {
//                     if (i % j == 0) {
//                         isPrime = false;
//                         break;
//                     }
//                 }                
                
//                 if (isPrime) System.out.println(i);
//             }
//         }
//         scanner.close();
//     }
// }
=============================================================================================================

 //leb 3  no 6
 import java.util.Scanner;

public class year {
    public static void main(String[] args) {
        // Create a Scanner object for input
        Scanner scanner = new Scanner(System.in);

        // Ask the user to input a year
        System.out.print("Enter a year: ");
        int year = scanner.nextInt();

        // Check if the year is a leap year
        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            System.out.println(year + " is a leap year.");
        } else {
            System.out.println(year + " is not a leap year.");
        }

        // Close the scanner
        scanner.close();
    }
}
=============================================================================================================
 
 leb 4  pro 1 to 3 
 //  1
 import java.util.Scanner;
public class Vowels{
    public static void main(String[] args) {
     
     Scanner scanner = new Scanner(System.in);


        System.out.print("Enter string : ");
        String  str = scanner.nextLine();

        int vcount = 0;
        int ccount = 0;

        for(int i = 0 ; i<str.length() ; i++){
            if(str.charAt(i)== 'a' || str.charAt(i)== 'e'||str.charAt(i)== 'i'||str.charAt(i)== 'o'||str.charAt(i)== 'u'||
                str.charAt(i)== 'A' || str.charAt(i)== 'E'||str.charAt(i)== 'I'||str.charAt(i)== 'O'||str.charAt(i)== 'U')
            {
                vcount++;

            }
            else{
                ccount++;
            }

           
        }
         System.out.println("vcount" + vcount );
            System.out.println("ccount" + ccount);
 }
}
=============================================================================================================
 //   2
 import java.util.Scanner;
public class Arrarg{
    public static void main(String[] args) {
     
     Scanner sc = new Scanner(System.in);


        System.out.print("Enter array size : ");
        int n = sc.nextInt();

        int arr[] = new int[n];
        double sum =0;

        for(int i=0;i<n;i++){
            arr[i] = sc.nextInt();
            sum += arr[i];
        }

        double avg = sum / n;

        System.out.print("avg : "+ avg);
}
}
=============================================================================================================
 //  3
 import java.util.Scanner;
public class Rev{
    public static void main(String[] args) {
     
     Scanner sc = new Scanner(System.in);


        System.out.print("Enter array size : ");
        int n = sc.nextInt();

        int arr[] = new int[n];
        int p=0;

   for(int i = 0; i<n ; i++){
        
            arr[i] = sc.nextInt();
            
    }
        for(int i=n-1;i >= 0;i--){
        System.out.print("array : " + arr[i]);
        }
}
}
__________________________________________________________
 // Parent class
class Animal {
    String name;

    // Constructor of the parent class
    public Animal(String name) {
        this.name = name;
    }

    // Method in the parent class
    public void displayInfo() {
        System.out.println("Animal name: " + name);
    }
}

// Child class
class Dog extends Animal {
    String breed;

    // Constructor of the child class
    public Dog(String name, String breed) {
        super(name);  // Calling the parent class constructor
        this.breed = breed;
    }

    // Method in the child class
    public void displayDetails() {
        super.displayInfo();  // Calling the parent class method
        System.out.println("Dog breed: " + breed);
    }
}

public class Main {
    public static void main(String[] args) {
        // Creating a Dog object
        Dog dog = new Dog("Buddy", "Golden Retriever");

        // Displaying details of the dog
        dog.displayDetails();
    }
}



_________________________________________________________
 import java.util.Scanner;

class Student {
    private int id_no;
    private int no_of_subjects_registered;
    private String[] subject_code;
    private int[] subject_credits;
    private char[] grade_obtained;
    private double spi;

    // Constructor
    public Student(int id_no, int no_of_subjects_registered, String[] subject_code, int[] subject_credits, char[] grade_obtained) {
        this.id_no = id_no;
        this.no_of_subjects_registered = no_of_subjects_registered;
        this.subject_code = subject_code;
        this.subject_credits = subject_credits;
        this.grade_obtained = grade_obtained;
        this.spi = calculateSPI();
    }

    // Method to calculate SPI
    private double calculateSPI() {
        int totalCredits = 0;
        double totalPoints = 0;

        for (int i = 0; i < no_of_subjects_registered; i++) {
            totalCredits += subject_credits[i];
            totalPoints += gradeToPoints(grade_obtained[i]) * subject_credits[i];
        }

        return totalPoints / totalCredits;
    }

    // Convert grade to points
    private double gradeToPoints(char grade) {
        switch (grade) {
            case 'A': return 10.0;
            case 'B': return 8.0;
            case 'C': return 6.0;
            case 'D': return 4.0;
            case 'E': return 2.0;
            case 'F': return 0.0;
            default: return 0.0;
        }
    }

    // Method to display student details
    public void displayDetails() {
        System.out.println("ID No: " + id_no);
        System.out.println("SPI: " + spi);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter the number of students:");
        int n = scanner.nextInt();
        
        Student[] students = new Student[n];
        
        for (int i = 0; i < n; i++) {
            System.out.println("Enter details for student " + (i + 1) + ":");
            
            System.out.print("ID No: ");
            int id_no = scanner.nextInt();
            
            System.out.print("Number of subjects registered: ");
            int no_of_subjects_registered = scanner.nextInt();
            
            String[] subject_code = new String[no_of_subjects_registered];
            int[] subject_credits = new int[no_of_subjects_registered];
            char[] grade_obtained = new char[no_of_subjects_registered];
            
            for (int j = 0; j < no_of_subjects_registered; j++) {
                System.out.print("Enter subject code " + (j + 1) + ": ");
                subject_code[j] = scanner.next();
                
                System.out.print("Enter subject credits " + (j + 1) + ": ");
                subject_credits[j] = scanner.nextInt();
                
                System.out.print("Enter grade obtained " + (j + 1) + ": ");
                grade_obtained[j] = scanner.next().charAt(0);
            }
            
            // Creating the student object
            students[i] = new Student(id_no, no_of_subjects_registered, subject_code, subject_credits, grade_obtained);
        }
        
        // Display the SPI of each student
        for (int i = 0; i < n; i++) {
            System.out.println("\nDetails for student " + (i + 1) + ":");
            students[i].displayDetails();
        }

        scanner.close();
    }
}import java.util.Scanner;

class Student {
    private int id_no;
    private int no_of_subjects_registered;
    private String[] subject_code;
    private int[] subject_credits;
    private char[] grade_obtained;
    private double spi;

    // Constructor
    public Student(int id_no, int no_of_subjects_registered, String[] subject_code, int[] subject_credits, char[] grade_obtained) {
        this.id_no = id_no;
        this.no_of_subjects_registered = no_of_subjects_registered;
        this.subject_code = subject_code;
        this.subject_credits = subject_credits;
        this.grade_obtained = grade_obtained;
        this.spi = calculateSPI();
    }

    // Method to calculate SPI
    private double calculateSPI() {
        int totalCredits = 0;
        double totalPoints = 0;

        for (int i = 0; i < no_of_subjects_registered; i++) {
            totalCredits += subject_credits[i];
            totalPoints += gradeToPoints(grade_obtained[i]) * subject_credits[i];
        }

        return totalPoints / totalCredits;
    }

    // Convert grade to points
    private double gradeToPoints(char grade) {
        switch (grade) {
            case 'A': return 10.0;
            case 'B': return 8.0;
            case 'C': return 6.0;
            case 'D': return 4.0;
            case 'E': return 2.0;
            case 'F': return 0.0;
            default: return 0.0;
        }
    }

    // Method to display student details
    public void displayDetails() {
        System.out.println("ID No: " + id_no);
        System.out.println("SPI: " + spi);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Enter the number of students:");
        int n = scanner.nextInt();
        
        Student[] students = new Student[n];
        
        for (int i = 0; i < n; i++) {
            System.out.println("Enter details for student " + (i + 1) + ":");
            
            System.out.print("ID No: ");
            int id_no = scanner.nextInt();
            
            System.out.print("Number of subjects registered: ");
            int no_of_subjects_registered = scanner.nextInt();
            
            String[] subject_code = new String[no_of_subjects_registered];
            int[] subject_credits = new int[no_of_subjects_registered];
            char[] grade_obtained = new char[no_of_subjects_registered];
            
            for (int j = 0; j < no_of_subjects_registered; j++) {
                System.out.print("Enter subject code " + (j + 1) + ": ");
                subject_code[j] = scanner.next();
                
                System.out.print("Enter subject credits " + (j + 1) + ": ");
                subject_credits[j] = scanner.nextInt();
                
                System.out.print("Enter grade obtained " + (j + 1) + ": ");
                grade_obtained[j] = scanner.next().charAt(0);
            }
            
            // Creating the student object
            students[i] = new Student(id_no, no_of_subjects_registered, subject_code, subject_credits, grade_obtained);
        }
        
        // Display the SPI of each student
        for (int i = 0; i < n; i++) {
            System.out.println("\nDetails for student " + (i + 1) + ":");
            students[i].displayDetails();
        }

        scanner.close();
    }
}
