import json
from cryptography.fernet import Fernet

class PasswordReader:
    def __init__(self):
        # Initialize the PasswordReader class
        self.passwordEntries = []  # A list to store decrypted passwords
        self.key = b'P1EFF6GUanZQgv0SbZcTCOHFLpN2XqyNrb6KHw94EzQ='  # The Fernet key in string format
        self.startUp()

    def encrypt_data(self, data):
        # Encrypt the provided data using Fernet encryption
        fernet = Fernet(self.key)  # Initialize Fernet with the provided key
        encrypted_data = fernet.encrypt(data.encode())  # Encrypt the data
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        # Decrypt the provided encrypted data using Fernet decryption
        fernet = Fernet(self.key)  # Initialize Fernet with the provided key
        decrypted_data = fernet.decrypt(encrypted_data).decode()  # Decrypt the data and decode to string
        return decrypted_data

    def startUp(self):
        try:
            with open('Passwords.json', 'r') as file:
                passwords_data_list = json.load(file)
                for passwords_data in passwords_data_list:
                    encrypted_passwords = passwords_data.get("password", [])
                    if encrypted_passwords:
                        decrypted_password = self.decrypt_data(encrypted_passwords.encode())
                        self.passwordEntries.append(decrypted_password)
        except FileNotFoundError:
            print("File not found :(")
        except Exception as e:
            print(f"An error occurred during loading passwords: {e}")


    def endingProgram(self):
        try:
            # Encrypt all the passwords in the passwordEntries list and save to the JSON file
            passwords_data = [{"password": self.encrypt_data(password).decode()} for password in self.passwordEntries]
            with open('Passwords.json', mode='w') as file:
                json.dump(passwords_data, file, indent=4)  # Write the encrypted passwords to the file
        except FileNotFoundError:
            # If the file is not found, print an error message
            print("File not found :(")




        
