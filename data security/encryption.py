import hashlib
import os

def generate_salt():
    return os.urandom(16)

def generate_password_hash(password, salt):
    hash_object = hashlib.pbkdf2_hmac('sha256', password.encode(), salt, 100000)
    return hash_object

def verify_password(password, salt, stored_password_hash):
    new_password_hash = generate_password_hash(password, salt)
    return new_password_hash == stored_password_hash
