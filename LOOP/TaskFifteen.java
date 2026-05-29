import java.util.Scanner;

public class TaskFifteen{

public static void main(String[] args){

Scanner input = new Scanner(System.in);
String correctPassword = "Password123";
String userInput = " ";

 while(!userInput.equals(correctPassword)){
 
    System.out.print("Enter a password: ");
    userInput = input.nextLine();
    
    if(!userInput.equals(correctPassword)){
    System.out.print("Incorrect password");
    }
    else{
    System.out.print("Correct Password");
    }
 }
}
}

