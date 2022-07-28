import re

print("Welcome to Guvi")
welcome = input("Do you have an acount? y/n: ")
if welcome == "n":
    while True:
        username  = input("Enter a username:")
        # email Validation
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.fullmatch(regex, username):
            print("Valid email")
        else:
            print("Invalid email")
            break

        password  = input("Enter a password:")
        #password validation
        a, b, c, d = 0, 0, 0, 0
        if (len(password) >= 5 and len(password)<=16):
            for i in password:
                if (i.islower()):
                    a+=1           
                if (i.isupper()):
                    b+=1           
 
                if (i.isdigit()):
                     c+=1           
 
                if(i=='@'or i=='$' or i=='_'):
                    d+=1          
        if (a>=1 and b>=1 and c>=1 and d>=1 and a+b+c+d==len(password)):
                print("Valid Password")
        else:
            print("Invalid Password")
            break

        password1 = input("Confirm password:")
        if password == password1:
            file = open(username+".txt", "w")
            file.write(username+":"+password)
            file.close()
            welcome = "y"
            break
        print("Passwords do NOT match!")
 
if welcome == "y":
    while True:
        login1 = input("User name:")
        login2 = input("Password:")
        file = open(login1+".txt", "r")
        data   = file.readline()
        file.close()
        if data == login1+":"+login2:
            print("Welcome")
            break
        print("Incorrect username or password.")