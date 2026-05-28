import java.util.Scanner;

public class GradingSystem {
    public static void main(String[] args) {
        
        Scanner input = new Scanner(String.in);
        
        System.out.print("Enter the student's score (0-100): ");
        int score = input.nextInt();
        
        char grade;
        
      
        if (score < 0 || score > 100) {
            System.out.println("Invalid score! Please enter a number between 0 and 100.");
           
            return;
        } else if (score >= 90) {
            grade = 'A';
        } else if (score >= 75) {
            grade = 'B';
        } else if (score >= 60) {
            grade = 'C';
        } else if (score >= 45) {
            grade = 'D';
        } else {
            grade = 'F';
        }
        
        
        System.out.println("The student's grade is: " + grade);
     
      
    }
}

