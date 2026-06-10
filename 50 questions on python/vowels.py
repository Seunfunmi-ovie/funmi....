vowel = input("Enter a word: ")
vowels = "aeiou"
vowelCount = 0
for letters in vowel:
    if letters in vowels:
      vowelCount += 1
print(f"vowels: {vowelCount}")    
     
