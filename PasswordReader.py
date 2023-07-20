import string
import csv

class PasswordList:
    def __init__(self):
        self.passwordEntries = []
        startUp()

    def startUp(self, Passwords.csv):
        try:
            with open("Passwords.csv", 'r') as file:
                csv_reader = csv.reader(file)

                for row in csv_reader:
                    aPasswordEntry = passwordEntries()
    
        
