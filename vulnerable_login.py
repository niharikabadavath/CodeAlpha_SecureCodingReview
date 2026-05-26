# Vulnerable Login System

username = input("Enter username: ")
password = input("Enter password: ")

# Hardcoded credentials
if username == "niharika" and password == "Niharika@123":
    print("Login Successful")
else:
    print("Invalid Credentials")