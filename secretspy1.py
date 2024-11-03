import secrets
import string

# Import the module under a different name if it's needed for other purposes.
from Sofawiki_RCE import password as sofawiki_password

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generating password without spaces
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

print("Generated password:", generate_password())
