import bcrypt

password = input ("Enter your password :")

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())



print(hash_password(password))