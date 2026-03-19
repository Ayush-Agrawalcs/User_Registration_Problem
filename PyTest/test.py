import re
import pytest

pattern = r"^[A-Z][a-zA-Z]{2,}$"
pattern1="^[a-zA-Z0-9][a-zA-Z0-9-_+]+(\\.[a-zA-Z0-9_-]+)*@[a-zA-Z0-9]+(\\.[a-zA-Z0-9]{2,}){1,2}$"
pattern2=r"^\d{1,2}\s\d{10}$"
pattern3="(?=.*[A-Z])(?=.*[0-9])(?=.*[+&^%$#@*])[a-zA-Z0-9+&^%$#@*]{8,}"

@pytest.mark.parametrize("name,expected", [
    ("Ayush", True),
    ("An", False),       
    ("ayush", False),     
    ("AYUSH", True),      
    ("Ayu1h", False),    
])
def test_first_name(name, expected):
    result = bool(re.match(pattern, name))
    assert result == expected

@pytest.mark.parametrize("name,expected", [
    ("Agrawal", True),
    ("An", False),       
    ("agrawal", False),     
    ("AGRAWAL", True),      
    ("Agraw2a", False),    
])
def test_Last_name(name, expected):
    result = bool(re.match(pattern, name))
    assert result == expected


@pytest.mark.parametrize("email,expected", [
    ("abc-5@yahoo.com", True),
    ("abc123@.com.com", False),       
    (".abc@abc.com", False),     
    ("abc@gmail.com.com", True),      
    ("abc+100@gmail.com", True),
    ("abc-100@abc.net",True),
    ("abc_100@abc.net",True),
    ("abx@1.com",True)

])
def test_email(email, expected):
    result = bool(re.fullmatch(pattern1, email))  
    assert result == expected

@pytest.mark.parametrize("phone_no,expected", [
   ("91 8393872897", True),
   ("+91 8393872897", False),
    ("8756369875", False),       
    ("91 123456", False), 
    ("91-8393-872-897", False),

])
def test_phone_no(phone_no, expected):
    result = bool(re.fullmatch(pattern2, phone_no))  
    assert result == expected

@pytest.mark.parametrize("password,expected", [
   ("Ayush1234@", True),
   ("Ayush!234@#$", False),
    ("ayush12345@", False),       
    ("AyusA1@", False), 
    ("AyushAgraw@", False),
    ("Ayush1234@", True),
    ("Ayush123Ag",False)


])
def test_password(password, expected):
    result = bool(re.fullmatch(pattern3,password))  
    assert result == expected

