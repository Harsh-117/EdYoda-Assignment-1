def vowel_count(str):
      
    
    count = 0
      
    
    vowel = set("aeiouAEIOU")
      
   
    for alphabet in str:
      
        if alphabet in vowel:
            count = count + 1
      
    print("No. of vowels :", count)
      

str = "Python is a high level programming language"

vowel_count(str)
