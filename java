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
 // palindrome
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        // Input a number from the user
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        // Check if the number is a palindrome
        if (palin(number)) {
            System.out.println(number + " is a palindrome.");
        } else {
            System.out.println(number + " is not a palindrome.");
        }
    }
    // Method to check if a number is a palindrome
    public static boolean palin(int num) {
        int original = num;
        int reverse = 0;

        while (num > 0) {
            reverse = reverse * 10 + num % 10;
            num /= 10;
        }
        return original == reverse;
    }
}
------------------------------------------------------------------------------------------
 [C] Implement a Java Program to find largest element in a user defined 1D array. 

import java.util.Scanner;

public class LargestElement {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get the size of the array
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        // Declare the array and input its elements
        int[] array = new int[size];
        System.out.println("Enter " + size + " elements:");
        for (int i = 0; i < size; i++) {
            array[i] = scanner.nextInt();
        }

        // Find the largest element
        int largest = array[0];
        for (int i = 1; i < size; i++) {
            if (array[i] > largest) {
                largest = array[i];
            }
        }

        // Display the largest element
        System.out.println("The largest element in the array is: " + largest);
    }
}
________________________________________________________________________________________________________________________________________________________
[ C.2 ]Implement a Java program to accept a line and print how many consonants and vowels are there in line.

import java.util.Scanner;

public class VowelConsonantCounter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input a line of text
        System.out.print("Enter a line of text: ");
        String line = scanner.nextLine();

        // Initialize counters for vowels and consonants
        int vowels = 0, consonants = 0;

        // Convert line to lowercase for simplicity
        line = line.toLowerCase();

        // Loop through each character in the line
        for (char ch : line.toCharArray()) {
            if (ch >= 'a' && ch <= 'z') { // Check if character is a letter
                if ("aeiou".indexOf(ch) != -1) {
                    vowels++; // Increment vowels count
                } else {
                    consonants++; // Increment consonants count
                }
            }
        }

        // Display the counts
        System.out.println("Number of vowels: " + vowels);
        System.out.println("Number of consonants: " + consonants);
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
    int id_no;
    int no_of_subjects_registered;
    String[] subject_code;
    int[] subject_credits;
    char[] grade_obtained;
    double spi;

    // Constructor
    public Student(int id_no, int no_of_subjects_registered) {
        this.id_no = id_no;
        this.no_of_subjects_registered = no_of_subjects_registered;
        subject_code = new String[no_of_subjects_registered];
        subject_credits = new int[no_of_subjects_registered];
        grade_obtained = new char[no_of_subjects_registered];
    }

    // Method to calculate SPI
    public void calculate_spi() {
        int total_credits = 0;
        int total_points = 0;

        // Assign grade points based on grade_obtained
        for (int i = 0; i < no_of_subjects_registered; i++) {
            int grade_point;
            switch (grade_obtained[i]) {
                case 'A': grade_point = 10; break;
                case 'B': grade_point = 8; break;
                case 'C': grade_point = 6; break;
                case 'D': grade_point = 4; break;
                case 'F': grade_point = 0; break;
                default: grade_point = 0; break;
            }

            total_credits += subject_credits[i];
            total_points += grade_point * subject_credits[i];
        }

        if (total_credits != 0) {
            spi = (double) total_points / total_credits;
        } else {
            spi = 0;
        }
    }

    // Display SPI
    public void display_spi() {
        System.out.println("Student ID: " + id_no);
        System.out.println("SPI: " + spi);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter number of students: ");
        int n = sc.nextInt();

        // Create an array of Student objects
        Student[] students = new Student[n];

        for (int i = 0; i < n; i++) {
            System.out.print("\nEnter Student ID: ");
            int id_no = sc.nextInt();
            System.out.print("Enter number of subjects registered: ");
            int no_of_subjects_registered = sc.nextInt();

            // Create new student object
            students[i] = new Student(id_no, no_of_subjects_registered);

            for (int j = 0; j < no_of_subjects_registered; j++) {
                System.out.print("Enter subject code for subject " + (j + 1) + ": ");
                students[i].subject_code[j] = sc.next();
                System.out.print("Enter credits for subject " + (j + 1) + ": ");
                students[i].subject_credits[j] = sc.nextInt();
                System.out.print("Enter grade obtained for subject " + (j + 1) + " (A/B/C/D/F): ");
                students[i].grade_obtained[j] = sc.next().charAt(0);
            }

            // Calculate SPI
            students[i].calculate_spi();
        }

        // Display SPI for each student
        for (int i = 0; i < n; i++) {
            students[i].display_spi();
        }
        
        sc.close();
    }
}
-------------------------------------------------------------------------------------------------------------------
// Parent class (Animal)
class Animal {
    String name;

    // Constructor of Animal class
    public Animal(String name) {
        this.name = name;
    }

    // Method of Animal class
    public void displayInfo() {
        System.out.println("Animal Name: " + name);
    }
}

// Subclass (Dog) extending Animal class
class Dog extends Animal {
    String breed;

    // Constructor of Dog class
    public Dog(String name, String breed) {
        // Calling parent class constructor using super
        super(name);
        this.breed = breed;
    }

    // Method of Dog class
    public void displayDetails() {
        // Calling parent class method using super
        super.displayInfo();
        System.out.println("Breed: " + breed);
    }
}

// Main class to demonstrate super keyword
public class SuperKeywordDemo {
    public static void main(String[] args) {
        // Creating Dog object
        Dog myDog = new Dog("Buddy", "Golden Retriever");

        // Calling method of Dog class
        myDog.displayDetails();
    }
}
-----------------------------------------------------------------------------------------------------------------------------------------
 // Final variable example
class FinalVariableExample {
    // Final variable (constant) - its value cannot be changed once assigned
    final int MAX_VALUE = 100;

    // Method to demonstrate final variable
    public void displayMaxValue() {
        // Uncommenting the below line will give an error because final variables cannot be modified
        // MAX_VALUE = 200;  // This will cause a compilation error
        System.out.println("Max Value: " + MAX_VALUE);
    }
}

// Final method and class example
final class FinalClass {
    // Final method - it cannot be overridden by subclasses
    public final void showMessage() {
        System.out.println("This is a final method inside a final class.");
    }
}

// This will cause an error because FinalClass is final and cannot be inherited
// class SubClass extends FinalClass {}

public class FinalKeywordDemo {
    public static void main(String[] args) {
        // Creating object of class with final variable
        FinalVariableExample example = new FinalVariableExample();
        example.displayMaxValue();

        // Creating object of final class
        FinalClass finalClassObj = new FinalClass();
        finalClassObj.showMessage();
    }
}
==========================================================================================================================
 class myRunnable implements Runnable {
    Thread t;

    myRunnable() {
        System.out.println("Thread Is Created");
        t = new Thread(this); 
        t.start();
    }

    public void run() {
        try {
            for (int i = 0; i <= 5; i++) {
                System.out.println("Child Thread " + i);
                Thread.sleep(500);
            }
        } catch (InterruptedException e) {
            System.out.println(e.toString());
        }
    }
}

public class treadrunneble {
    public static void main(String[] args) {
        new myRunnable();

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            System.out.println(e.toString());
        }
    }
}
=================================================================================================================================
 class myThread1 extends Thread {
    myThread1() {
        System.out.println("Thread Is Created");
        start();
    }

    public void run() {
        try {
            for (int i = 0; i <= 5; i++) {
                System.out.println("Child Thread " + i);
                Thread.sleep(500);
            }
        } catch (InterruptedException e) {
            System.out.println(e.toString());
        }
    }
}

public class myThread {
    public static void main(String[] args) {
        new myThread1();

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            System.out.println(e.toString());
        }
    }
}
===============================================================================================================================================
 class myRunnable extends Thread {
    Thread t;

    myRunnable() {
        System.out.println("Thread Is Created");
        t = new Thread(this); 
        t.start();
    }

    public void run() {
        try {
            for (int i = 0; i <= 20; i++) {
                if(i % 2 == 0 ){
                    System.out.println("Child Thread " + i);
                    Thread.sleep(500);
                }
                
            }
        } catch (InterruptedException e) {
            System.out.println(e.toString());
        }
    }
}

public class odd {
    public static void main(String[] args) {
        new myRunnable();

        try {
            Thread.sleep(1000);
        } catch (InterruptedException e) {
            System.out.println(e.toString());
        }
    }
}
