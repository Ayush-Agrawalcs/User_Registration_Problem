import re
class User:
    '''
    Add valid User'''
    def __init__(self,First_name,Last_name):
        self.First_name=First_name
        self.Last_name=Last_name
    
    def __str__(self):
        return f"{self.First_name} {self.Last_name}"
    

def isvalid_first_name(First_name):
        '''
        validation of the First Name
        '''
        try:
            pattern="[A-Z]{1}[a-zA-z]{3,}"
            mat=re.match(pattern,First_name)
            if not mat:
                raise ValueError("First Name should start with capital letter and length should be 3 characters minimum")
            return True
        except ValueError as e:
            print(e)
        

def isvalid_Last_name(Last_name):
        '''
        validation of the Last Name
        '''
        try:
            pattern="[A-Z]{1}[a-zA-z]{3,}"
            mat=re.match(pattern,Last_name)
            if not mat:
                raise ValueError("Last Name should start with capital letter and length should be 3 characters minimum")
            return True
        except ValueError as e:
            print(e)

    

def main():
    while(True):
        First_name=input("Enter the first name:")
        Last_name=input("Enter the Last name:")
        valid_first=isvalid_first_name(First_name)
        valid_Last=isvalid_Last_name(Last_name)
        if(valid_first==True and valid_Last==True):
            user=User(First_name,Last_name)
            print(user)
            break


if __name__=="__main__":
    main()
     
