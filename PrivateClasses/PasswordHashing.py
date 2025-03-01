import re

import bcrypt
import sys

USER_DETAILS = 'user_details.txt'

def hash_password(password):
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

def save_to_file(email_address, password):
    with open(USER_DETAILS, 'a') as file:
        file.write(f'{email_address}:{password.decode("utf-8")}\n')

def validate_email(email_address):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,3}$'
    return re.match(pattern, email_address)

def register_user():
    while True:
        email_address = input("Enter your email address: :")
        if not validate_email(email_address):
            print("Please enter a valid email address {example@gmail.com}")
            continue
        break
    while True:
        password = input("Enter your password :")
        if not password:
            print("password cannot be empty")
            continue
        break
    save_to_file(email_address,hash_password(password))
    print(f"{email_address} registered successfully")



def validate_duplicate_user_email(email_address):
    with open(USER_DETAILS, 'r') as file:
        details = file.read()
        for line in details.split("\n"):
            if line:
                stored_email, stored_password = line.split(":")
                if stored_email == email_address:
                    return False
    return True




def validate_user(email_address,password):
    with open(USER_DETAILS, 'r') as file:
        details = file.read()
        for line in details.split("\n"):
            if line:
                stored_email, stored_password = line.split(":")
                if stored_email == email_address:
                    return bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8"))
    return False

def login_user():
    email_address = input("Enter your email Address :")
    password = input("Enter your password :")

    if validate_user(email_address,password):
        print("logged in successfully")
    else:
        print("invalid username or password")



def main():
    while True:
        menu = """ 
            1 -> Register
            2 -> Login User
            3 -> Logout
        """
        choice = input(menu)
        match choice:
            case '1':register_user()
            case '2':login_user()
            case '3':sys.exit(0)


main()