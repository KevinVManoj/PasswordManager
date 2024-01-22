import tkinter as tk
from tkinter import simpledialog
from PasswordCreator import PasswordCreator
from PasswordReader import PasswordReader

class PasswordManagerApp:
    def __init__(self, master):
        # These 2 lines basically make the window
        self.master = master
        self.master.title("Password Manager")

        # Initialize a PasswordReader object to manage passwords
        self.filePasswords = PasswordReader()

        # Create GUI elements
        # Labels are basically just text while buttons are buttons
        tk.Label(master, text="Welcome to Kevin's password manager").pack()
        tk.Label(master, text="Select an option:").pack()
        tk.Button(master, text="Create a new password", command=self.createPassword).pack()
        tk.Button(master, text="Add password", command=self.add_password).pack()
        tk.Button(master, text="Access passwords", command=self.access_passwords).pack()
        tk.Button(master, text="Exit", command=self.exitProgram).pack()

    def createPassword(self):
        # Create a new window for password creation
        createPasswordWindow = tk.Toplevel(self.master)
        createPasswordWindow.title("Create Password")

        # Create password entry fields and labels
        tk.Label(createPasswordWindow, text="Uppercase letters:").pack()
        uppercaseEntry = tk.Entry(createPasswordWindow)
        uppercaseEntry.pack()

        tk.Label(createPasswordWindow, text="Lowercase letters:").pack()
        lowercaseEntry = tk.Entry(createPasswordWindow)
        lowercaseEntry.pack()

        tk.Label(createPasswordWindow, text="Numbers:").pack()
        numbersEntry = tk.Entry(createPasswordWindow)
        numbersEntry.pack()

        tk.Label(createPasswordWindow, text="Special characters:").pack()
        specialEntry = tk.Entry(createPasswordWindow)
        specialEntry.pack()

        # Button to generate password
        generateButton = tk.Button(createPasswordWindow, text="Generate Password",
                                    command=lambda: self.generateAndDisplayPassword(
                                        uppercaseEntry.get(), lowercaseEntry.get(),
                                        numbersEntry.get(), specialEntry.get(), createPasswordWindow)).pack()

    def generateAndDisplayPassword(self, uppercase, lowercase, numbers, special, createPasswordWindow):
        generateAndDisplayPassword = tk.Toplevel(self.master)
        generateAndDisplayPassword.title("Assign Password")

        # Generate a password based on user requirements
        passwordGenerator = PasswordCreator(int(uppercase), int(lowercase), int(numbers), int(special))
        password = passwordGenerator.generatePassword()

        # Display the generated password
        tk.Label(generateAndDisplayPassword, text="Generated Password: " + password).pack()

        # Button to assign the password
        assignButton = tk.Button(generateAndDisplayPassword, text="Assign Password",
                                command=lambda: self.assignPassword(password, generateAndDisplayPassword)).pack()
        remakePasswordButton = tk.Button(generateAndDisplayPassword, text="Remake Password",
                                command=lambda: self.createPassword()).pack()


    def assignPassword(self, password, createPasswordWindow):
        # Get the password label from the user
        passwordLabeling = tk.simpledialog.askstring("Assign Password", "What would you like to label this password as?")
        userPasswordUnit = passwordLabeling + ":" + password

        # Add the labeled password to the passwordEntries list
        self.filePasswords.passwordEntries.append(userPasswordUnit)
        print("Password has been stored")

        createPasswordWindow.destroy()  # Close the password creation window

    def add_password(self):
        # Create a new window for adding passwords
        addPasswordWindow = tk.Toplevel(self.master)
        addPasswordWindow.title("Add Password")

        # Create name and password entry fields
        tk.Label(addPasswordWindow, text="Name:").pack()
        nameEntry = tk.Entry(addPasswordWindow)
        nameEntry.pack()

        tk.Label(addPasswordWindow, text="Password:").pack()
        passwordEntry = tk.Entry(addPasswordWindow)
        passwordEntry.pack()

        # Button to add the password
        addButton = tk.Button(addPasswordWindow, text="Add Password",
                               command=lambda: self.addUserPassword(nameEntry.get(), passwordEntry.get(),
                                                                      addPasswordWindow)).pack()

    def addUserPassword(self, name, password, window):
        userPasswordUnit = name + ":" + password

        # Add the user-provided password to the passwordEntries list
        self.filePasswords.passwordEntries.append(userPasswordUnit)
        print("Password has been stored")

        window.destroy()  # Close the add password window

    def access_passwords(self):
        # Create a new window for accessing passwords
        accessPasswordsWindow = tk.Toplevel(self.master)
        accessPasswordsWindow.title("Access Passwords")

        # Display all stored passwords
        passwordsLabel = tk.Label(accessPasswordsWindow, text="Passwords:").pack()

        for passwordEntriesList in self.filePasswords.passwordEntries:
            tk.Label(accessPasswordsWindow, text=passwordEntriesList).pack()

        self.eliminatePassword = tk.Label(accessPasswordsWindow, text="Would you like to delete a password?").pack()

       # self.deleteButton = tk.Button(accessPasswordsWindow, text="Delete Password", command=self.deletePassword).pack()

    #def deletePassword(self):
    #    deletePasswordWindow = tk.Toplevel(self.master)
    #    deletePasswordWindow.title("Delete Password")
    #
    #    self.destroyPassword = tk.Label(deletePasswordWindow, text="Which password would you like to delete?").pack()

     #   for passwordEntriesList in self.filePasswords.passwordEntries:
      #      tk.Button(deletePasswordWindow, text=passwordEntriesList command=self.dele).pack()
            ##Look into how to figure out the index of the button you hit, then delete that password in the passwordEntries list

        

    def exitProgram(self):
        # Exit the program, perform necessary cleanup and data saving
        self.filePasswords.endingProgram()
        print("Exiting the program.")
        self.master.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordManagerApp(root)
    root.mainloop()
