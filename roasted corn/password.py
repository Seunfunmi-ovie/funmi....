def get_word(word):
    
    return len(word)  


def seperate_word(word):
    first_part = word[0:2]
    last_part = word[-2:]         
    return (first_part + last_part)
    
def add_extra(word):
    new_word = word + "ing"
    return new_word
     


def long_word(word):
    data = ["welcome", "out", "weather", "mobile", "breakfast","journey"]
    actual_word = data[4]
    word_length = len(actual_word)
    return (actual_word,word_length)    


def remove_word(word):
    actual_word = "eioo"
    if word != actual_word:
     return (actual_word)
  
    


def minimuim_value(number):

     lowest = number[0]
     for count in  number:
       if count < lowest:
           lowest = count
     return lowest
           
numbers= [23,56,78,56]  
#print(minimuim_value(numbers))         
        

def maximuim_value(number):
    
      maximum = number[0]
      for count in number:
          if count > maximum:
             maximum = count        
        
      return maximum
numbers = [23,56,78,56]
#print(maximuim_value(numbers))     
            

#
#
#def add_extra_word(word,number,times):
#    
#    combine_word = f"{word}{number}"
#    return combine_word * times
#print(add_extra("hello",5,4))
#    

def get_square(number):
    squared_num = []
    for count in number:
    
       square_number = count * count
       squared_num.append(square_number)
    return squared_num   
    
numbers = [2,3,4,5,6]        
    


def get_square(number):
    squared_num = []
    total = 0
    for count in number:
    
       square_number = count * count
       
       total += square_number  
   
    return total

    















  
  
  
  
  
  
  
  
    
   
