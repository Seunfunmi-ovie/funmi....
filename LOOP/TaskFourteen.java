import java.util.Scanner;

    public class TaskFourteen{

        public static void main(String [] args){
        
        Scanner input = new Scanner(System.in);
        
       int sum = 0;
       
       for(int count = 1; count <= 5; count++){
       
        System.out.print("Enter Number: ");
        int num = input.nextInt();
        
        sum += num; 
       }
           System.out.print("Sum: " + sum);
        }

}
