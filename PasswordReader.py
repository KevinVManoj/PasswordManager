import csv

class PasswordReader:
    def __init__(self):
        self.passwordEntries = []
        self.startUp("Passwords.csv")

    def startUp(self, filename):
        try:
            with open(filename, 'r') as file:
                csv_reader = csv.reader(file, delimiter=':')
                next(csv_reader)
                for row in csv_reader:
                    if len(row) >= 2:
                        unit, password = row[:2]
                        self.passwordEntries.append((unit.strip(), password.strip()))
        except FileNotFoundError:
            print("File not found :(")
    
        
