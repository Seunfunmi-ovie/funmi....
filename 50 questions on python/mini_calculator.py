num1  = int(input("Enter number: "))
num2 = int(input("Enter number: "))

choice = input("Enter choice if + or -:  ")

if choice == "+":
     result = num1 + num2
     print(f"{num1} + {num2} = {result}")
elif choice == "-":
     result = num1 - num2
     print(f"{num1} + {num2} = {result}") 
else:
     print("Invalid input")
