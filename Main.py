import string
from PasswordCreator import PasswordCreator
from PasswordReader import PasswordReader

# Initialize a PasswordReader object to manage passwords
filePasswords = PasswordReader()

# Display a welcome message and program menu
print("Welcome to Kevin's password manager,")
print("You can either create a new password for a service you use with your own requirements")
print("Or you can access your passwords")

# Initialize a flag to control the program flow
programUpkeep = True

# Main program loop
while programUpkeep:
    # Display the program menu
    print("1. Create a new password")
    print("2. Add password")
    print("3. Access passwords")
    print("4. Exit")

    # Accept user input for menu choice
    x = int(input())

    if x == 1:
        while x == 1:
            # Accept user-defined password requirements
            userUppercase = int(input("How many uppercase letters would you like? "))
            userLowercase = int(input("How many lowercase letters would you like? "))
            userNumbers = int(input("How many numbers would you like? "))
            userSpecial = int(input("How many special characters would you like? "))

            # Generate a password based on user requirements
            passwordGenerator = PasswordCreator(userUppercase, userLowercase, userNumbers, userSpecial)
            password = passwordGenerator.generatePassword(userUppercase, userLowercase, userNumbers, userSpecial)

            # Display the generated password and options to assign or generate another
            print("Here is your password:", password)
            print("If you like your password, type 1 to assign the password. If you wish for another password, type 2 to generate another.")
            y = int(input())

            if y == 1:
                x += 1
                passwordLabeling = input("What would you like to label this password as? ")
                userPasswordUnit = passwordLabeling + ":" + password
                
                # Add the labeled password to the passwordEntries list
                filePasswords.passwordEntries.append(userPasswordUnit)
                print("Password has been stored")
                
            elif y == 2:
                x = 1

    elif x == 2:
        # Accept a user-provided password and its associated name
        userPasswordName = input("Input the name of the password: ")
        userPasswordPassword = input("Input the password: ")
        userPasswordUnit = userPasswordName + ":" + userPasswordPassword
        
        # Add the user-provided password to the passwordEntries list
        filePasswords.passwordEntries.append(userPasswordUnit)
        print("Password has been stored")

    elif x == 3:
        # Display all stored passwords
        print("Passwords:")
        for passwordEntriesList in filePasswords.passwordEntries:
            print(passwordEntriesList)

    elif x == 4:
        # Exit the program, perform necessary cleanup and data saving
        programUpkeep = False
        filePasswords.endingProgram()
        print("Exiting the program.")

    else:
        print("Invalid choice. Please try again.")
