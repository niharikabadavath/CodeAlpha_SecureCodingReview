# Secure Login Example

stored_username = "niharika"

# Simulated hashed password

stored_password = "Niharika@123"

username = input("Enter username: ")
password = input("Enter password: ")

if username == stored_username and password == stored_password:
    print("Secure Login Successful")
else:
    print("Invalid Credentials")