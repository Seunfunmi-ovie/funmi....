
total_score = 0

print("Welcome to Class! Let's calculate your grade average.")


for count in range(1, 6):
    
    
    while True:
        score = float(input(f"Enter score for Test {count} (0-100): "))
        
        
        if 0 <= score <= 100:
            total_score += score  
            break                 
        else:
            print("Invalid score! Please enter a number between 0 and 100.")


average = total_score / 5


print(f"Average: {average:.0f}")

