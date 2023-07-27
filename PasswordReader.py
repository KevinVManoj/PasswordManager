import csv

class PasswordReader:
    def __init__(self):
        self.passwordEntries = []
        self.startUp("Passwords.csv")

    def startUp(self, filename):
        try:
            with open(filename, 'r') as file:
                csv_reader = csv.reader(file, delimiter=':')
                # Check if there is data available before calling next()
                first_row = next(csv_reader, None)
                if first_row is not None:
                    for row in csv_reader:
                        if len(row) >= 2:
                            # Join the elements of the row using the delimiter ':'
                            # and append the resulting string to the list
                            row_str = ':'.join(row)
                            self.passwordEntries.append(row_str)
        except FileNotFoundError:
            print("File not found :(")

    def endingProgram(self, filename):
        try:
            with open(filename, mode='w', newline='') as file:
                csv_writer = csv.writer(file)  # Specify the delimiter as ':'
                csv_writer.writerow(["Unit:Password"])
                for row in self.passwordEntries:
                    csv_writer.writerow([row])
        except FileNotFoundError:
            print("File not found :(")

# Rest of your code (not shown in this example)


        
