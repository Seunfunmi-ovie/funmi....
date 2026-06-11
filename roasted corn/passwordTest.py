from unittest import TestCase
from password import *

class TestQuestionValidation(TestCase):


     def test_that_function_count(self):
           result = get_word("semicolon") 
           self.assertEqual(result,9)
       
       
     def test_that_function_seperate_word(self):
           word = "Semicolon"
           actual = seperate_word(word)
           expected = "Seon"
           self.assertEqual(expected,actual)
           
           
     def test_that_function_addExtra(self):
           word = "seunfumi"
           actual = add_extra(word)
           expected = "seunfumiing"
           self.assertEqual(expected,actual)
       
      
     def test_that_function_pick_Longest_word(self):
         word = ("welcome", "out","weather", "mobile","breakfast","journey")  
         actual = long_word(word)
         expected = "breakfast"
         self.assertEqual(actual,expected)
      
       
     def test_that_function_remove(self):
           result = remove_word("Semicolon")
           self.assertEqual(result,"eioo")
           
           
           
             
           
           
           
           
                
