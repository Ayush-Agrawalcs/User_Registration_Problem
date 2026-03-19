import re
class User:
    '''
    Add valid User'''
    def __init__(self,First_name,Last_name,email,phone_no,password):
        self.First_name=First_name
        self.Last_name=Last_name
        self.email=email
        self.phone_no=phone_no
        self.password=password
    
    def __str__(self):
        return f"{self.First_name} {self.Last_name} {self.email} {self.phone_no} {self.password}"
    

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

def isvalid_email(email):
        '''
        validation of the email address
        '''
        try:
            pattern="^[a-zA-Z0-9]+(\\.[a-zA-Z0-9]+)*@[a-zA-Z]+(\\.[a-zA-Z0-9]+)+$"
            mat=re.match(pattern,email)
            if not mat:
                raise ValueError("Invalid Email")
            return True
        except ValueError as e:
            print(e)

def isvalid_Phone_no(phone_no):
        '''
        validation of the Phone Number
        '''
        try:
            pattern=r"^\d{1,2}\s\d{10}$"
            mat=re.match(pattern,phone_no)
            if not mat:
                raise ValueError("Invalid phone_no")
            return True
        except ValueError as e:
            print(e)


def isvalid_password(password):
        '''
        Validate password minimum 8 character
        Should have atleast 1 Uppercase Letter
        Should have atleast 1 nUMERIC Value
        '''
        try:
            pattern="(?=.*[A-Z])(?=.*[0-9])[a-zA-Z0-9+&^%$#@*]{8,}"
            mat=re.match(pattern,password)
            if not mat:
                raise ValueError("Invalid password")
            return True
        except ValueError as e:
            print(e)

     

    

def main():
    while(True):
        First_name=input("Enter the first name: ")
        Last_name=input("Enter the Last name: ")
        email=input("Enter the email: ")
        phone_no=input("Enter the phone no.: ")
        password=input("Enter the password: ")
        valid_first=isvalid_first_name(First_name)
        valid_Last=isvalid_Last_name(Last_name)
        valid_email=isvalid_email(email)
        valid_phone_no=isvalid_Phone_no(phone_no)
        valid_password=isvalid_password(password)

        if(valid_first==True and valid_Last==True and valid_email==True and valid_phone_no==True and valid_password==True) :
            user=User(First_name,Last_name,email,phone_no,password)
            print(user)
            break


if __name__=="__main__":
    main()

     
