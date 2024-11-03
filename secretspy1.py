import secrets
import string

from Sofawiki_RCE import password


def generate_password(length = 12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ' '.join(secrets.choice(characters) for _ in range(length))
    return  password
print("Generated password" , generate_password())