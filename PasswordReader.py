import json
from cryptography.fernet import Fernet

class PasswordReader:
    def __init__(self):
        # Initialize the PasswordReader class
        self.passwordEntries = []  # A list to store decrypted passwords
        self.key = b'P1EFF6GUanZQgv0SbZcTCOHFLpN2XqyNrb6KHw94EzQ='  # The Fernet key in string format
        self.startUp("Passwords.json")  # Call the startUp method to read passwords from the file

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

    def startUp(self, filename):
        try:
            # Load passwords data from the JSON file
            with open(filename, 'r') as file:
                passwords_data_list = json.load(file)  # Load the JSON data as a list of dictionaries
                if len(passwords_data_list) > 0:
                    passwords_data = passwords_data_list[0]  # Access the first dictionary in the list
                    encrypted_passwords = passwords_data.get("passwords", [])  # Get the list of encrypted passwords
                    for encrypted_password in encrypted_passwords:
                        # Decrypt each encrypted password and add it to the passwordEntries list
                        decrypted_password = self.decrypt_data(encrypted_password.encode())
                        self.passwordEntries.append(decrypted_password)
                else:
                    # If no passwords found in the file, print a message
                    print("No passwords found in the file.")
        except FileNotFoundError:
            # If the file is not found, print an error message
            print("File not found :(")

    def endingProgram(self, filename):
        try:
            # Encrypt all the passwords in the passwordEntries list and save to the JSON file
            passwords_data = [{"password": self.encrypt_data(password).decode()} for password in self.passwordEntries]
            with open(filename, mode='w') as file:
                empty_data = []
                json.dump(empty_data, file, indent=4)
                json.dump(passwords_data, file, indent=4)
        except FileNotFoundError:
            # If the file is not found, print an error message
            print("File not found :(")




        
