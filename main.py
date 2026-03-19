import re
class User:
    def __init__(self,First_name):
        self.First_name=First_name
    
    def __str__(self):
        return f"{self.First_name}"
    

def isvalid_first_name(First_name):
        try:
            pattern="[A-Z]{1}[a-zA-z]{3,}"
            mat=re.match(pattern,First_name)
            valid=True if mat else "First Name should start with capital letter and length should be 3 characters minimum"
            return valid
        except ValueError as e:
            return e

    

def main():
    while(True):
        First_name=input("Enter the first name:")
        valid_first=isvalid_first_name(First_name)
        if(valid_first==True):
            user=User(First_name)
            print(user)
        else:
            print(valid_first)

if __name__=="__main__":
    main()
     
