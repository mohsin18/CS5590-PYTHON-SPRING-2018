import re #using regular expression to match stings
p=input("Enter your password : ")#input
if len(p) in range(6,16):#using loops to to validate the password
    if re.search("[a-z]",p) and re.search("[A-Z]",p) and re.search("[0-9]",p) and re.search("[!@*$]",p) :
        print("password id validated")
    else:
        print("password is not complex")
else:
    print("Enter password between 6 to 16 characters")