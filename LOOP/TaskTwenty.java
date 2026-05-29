import java.util.Scanner;

public class TaskTwenty {

    public static void main(String[] args) {

        Scanner input = new Scanner(System.in);

        System.out.print("Enter number input: ");
        int totalTimes = input.nextInt(); 
        
        int largest = 0; 

        for (int count = 1; count <= totalTimes; count++) {
            System.out.print("Enter number: ");
            int num = input.nextInt(); 
            
           
            if (count == 1) {
                largest = num;
            } 
        
            else if (num > largest) { 
                largest = num;
            }
        }
        
        System.out.println("Largest: " + largest);
        
    }
