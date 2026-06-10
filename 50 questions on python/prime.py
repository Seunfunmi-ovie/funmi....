while True:
    
    user_input = input("Enter a number to check: ")
    number = int(user_input)
    

    is_prime = True 
    if number < 2:
        is_prime = False
    else:
    
        for count in range(2, number):
            
            if number % count == 0:
                is_prime = False
                break
   
    if is_prime:
        print("Prime!")
    else:
        print("Not prime!")
    
    
    choice = input("Do you want to check another number? (yes/no): ")
    if choice != "yes" and choice != "y":
        print("Goodbye!")
        break

