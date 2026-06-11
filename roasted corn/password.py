def get_word(word):
    return len(word)
print(get_word("Semicolon"))    


def seperate_word(word):
    first_part = word[0:2]
    last_part = word[-2:]         
    print(first_part + last_part)

seperate_word("Semicolon")



def add_extra(word):
    new_word = word + "ing"
    print(new_word)
add_extra("seunfunmi")      


def long_word(word):
    data = ["welcome", "out", "weather", "mobile", "breakfast","journey"]
    actual_word = data[4]
    word_length = len(actual_word)
    print(actual_word,word_length)    
long_word("breakfast")    


def remove_word(word):
    actual_word = "eioo"
    if word != actual_word:
    
        print(actual_word)
remove_word("Semicolon")    
    


def minimuim_value(number):

     lowest = number[0]
     for count in  number:
       if count < lowest:
           lowest = count
     return lowest
           
numbers= [23,56,78,56]  
print(minimuim_value(numbers))         
        

def maximuim_value(number):
    
      maximum = number[0]
      for count in number:
          if count > maximum:
             maximum = count        
        
      return maximum
numbers = [23,56,78,56]
print(maximuim_value(numbers))     
            



def add_extra(word,number,times):
    
    combine_word = f"{word}{number}"
    return combine_word * times
print(add_extra("hello",5,4))
    

def get_square(number):
    squared_num = []
    for count in number:
    
       square_number = count * count
       squared_num.append(square_number)
    return squared_num   
    
numbers = [2,3,4,5,6]    
print(get_square(numbers))    
    


def get_square(number):
    squared_num = []
    total = 0
    for count in number:
    
       square_number = count * count
       
       total += square_number  
   
    return total
numbers = [2,3,4,5,7]    
print(get_square(numbers))    
    















  
  
  
  
  
  
  
  
    
   
