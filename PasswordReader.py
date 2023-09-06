import json
from cryptography.fernet import Fernet

class PasswordReader:
    def __init__(self):
        """
        Initializes the PasswordReader class.

        Attributes:
            passwordEntries (list): A list to store decrypted passwords.
            key (str): The current Fernet key in string format.
            keyF (str): The future Fernet key in string format.
        """
        self.passwordEntries = []  # A list to store decrypted passwords
        self.key = None  # The Fernet key in string format
        self.keyF = None # The Fernet key for the next sun in strong format
        self.startUp() # Start up method 

    def encryptData(self, data):
        """
        Encrypts the provided data using Fernet encryption.

        Args:
            data (str): The data to be encrypted as a string.

        Returns:
            bytes: The encrypted data as bytes.
        """
        # Initialize Fernet with the provided key
        fernet = Fernet(self.key)
        
        # Encrypt the data and return it as bytes
        encryptedData = fernet.encrypt(data.encode())
        return encryptedData

    def decryptData(self, encryptedData):
        """
        Decrypts the provided encrypted data using Fernet decryption.

        Args:
            encrypted_data (bytes): The encrypted data to be decrypted as bytes.

        Returns:
            str: The decrypted data as a string.
        """
        # Initialize Fernet with the provided key
        fernet = Fernet(self.key)
        
        # Decrypt the data, decode it to a string, and return
        decryptedData = fernet.decrypt(encryptedData).decode()
        return decryptedData


    def startUp(self):
        """
        This method is responsible for initializing the program by loading essential data from JSON files.
        
        It performs the following steps:
        1. Loads the encryption keys from 'Keys.json' and sets the current key (self.key) and future key (self.keyF).
        2. Loads encrypted passwords from 'Passwords.json', decrypts them, and populates the 'passwordEntries' list.

        If any of the required files ('Keys.json' or 'Passwords.json') is not found during the process,
        it prints an error message.

        Args:
            self: The instance of the class where this method is defined.

        Returns:
            None
        """
        try:
            # Load encryption keys from 'Keys.json' file
            with open('Keys.json', 'r') as file:
                keyListData = json.load(file)
                self.key = keyListData["keyInUse"].encode()
                self.keyF = keyListData["keyToBeUsed"].encode()
        except FileNotFoundError:
            # If 'Keys.json' file is not found, print an error message
            print("File 'Keys.json' not found :(")
        except Exception as e:
            # Handle other exceptions during key loading
            print(f"An error occurred during loading keys: {e}")

        try:
            # Load encrypted passwords from 'Passwords.json' file
            with open('Passwords.json', 'r') as file:
                passwordsDataList = json.load(file)
                for passwordsData in passwordsDataList:
                    encryptedPasswords = passwordsData.get("password", [])
                    if encryptedPasswords:
                        decryptedPassword = self.decrypt_data(encryptedPasswords.encode())
                        self.passwordEntries.append(decryptedPassword)
        except FileNotFoundError:
            # If 'Passwords.json' file is not found, print an error message
            print("File 'Passwords.json' not found :(")
        except Exception as e:
            # Handle other exceptions during password loading
            print(f"An error occurred during loading passwords: {e}")
        
        # Set the current key to the future key (self.key = self.keyF)
        self.key = self.keyF


    def endingProgram(self):
        """
        This method is responsible for finalizing the program and saving important data to JSON files.
        
        It performs the following steps:
        1. Generates a new encryption key using Fernet and converts it to a UTF-8 encoded string.
        2. Writes the current encryption key (self.key) and the new key to a 'Keys.json' file.
        3. Encrypts and saves all the passwords in the 'passwordEntries' list to a 'Passwords.json' file.

        If any of the required files ('Keys.json' or 'Passwords.json') is not found during the process,
        it prints an error message.

        Args:
            self: The instance of the class where this method is defined.

        Returns:
            None
        """
        # Generate a new encryption key
        newKey = Fernet.generateKey().decode('utf-8')

        try:
            # Create a dictionary containing the current key and the new key
            keyJsonRewrite = {
                "keyInUse": self.key.decode(),
                "keyToBeUsed": newKey
            }
            # Write the key data to 'Keys.json' file
            with open('Keys.json', mode='w') as file:
                json.dump(keyJsonRewrite, file, indent=4)
        except FileNotFoundError:
            # If 'Keys.json' file is not found, print an error message
            print("File 'Keys.json' not found :(")

        try:
            # Encrypt all the passwords in the 'passwordEntries' list and prepare them for saving
            passwordsData = [{"password": self.encryptData(password).decode()} for password in self.passwordEntries]
            # Write the encrypted passwords to 'Passwords.json' file
            with open('Passwords.json', mode='w') as file:
                json.dump(passwordsData, file, indent=4)
        except FileNotFoundError:
            # If 'Passwords.json' file is not found, print an error message
            print("File 'Passwords.json' not found :(")