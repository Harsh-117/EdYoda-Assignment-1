import re
def run(string):
 
    
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
     
      
    if(regex.search(string) == None):
        print("String is accepted")
         
    else:
        print("String is not accepted.")
     
 
if __name__ == '__main__' :
     
   
    string = "Python is a high level programming language"
     
    
    run(string)