import secrets

def generate_otp():
    return str(secrets.randbelow(900000) + 100000)