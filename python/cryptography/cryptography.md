# install
    pip install cryptography

# import 
    from cryptography.fernet import Fernet

# generate a 32 bit security key

    def generate_key():
        return Fernet.generate_key()

# SECURITY KEY
    ecoded_SECRET_KEY = SECRET_KEY.encode()


# encode an data
    def encode_text(plain_password):
        cipher_suite = Fernet(ecoded_SECRET_KEY)
        encrypted_text = cipher_suite.encrypt(plain_password.encode())
        return encrypted_text

# decode a data
    def decode_text(encrypted_text):
        cipher_suite = Fernet(ecoded_SECRET_KEY)
        decrypted_text = cipher_suite.decrypt(encrypted_text).decode()
        return decrypted_text