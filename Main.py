import string

from PasswordCreator import PasswordCreator
from PasswordReader import PasswordReader

filePasswords = PasswordReader()

print("Welcome to Kevin's password manager,")
print("You can either create a new password for a service you use with your own requirements")
print("Or you can access your passwords")

programUpkeep = True
while programUpkeep == True:
    print("1. Create a new password")
    print("2. Add password")
    print("3. Access passwords")
    print("4. Exit")

    x = int(input())
    if x == 1:
        while x == 1:
                userUppercase = int(input("How many uppercase letters would you like? "))
                userLowercase = int(input("How many lowercase letters would you like? "))
                userNumbers = int(input("How many numbers would you like? "))
                userSpecial = int(input("How many special characters would you like? "))

                password_generator = PasswordCreator(userUppercase, userLowercase, userNumbers, userSpecial)
                password = password_generator.generatePassword(userUppercase, userLowercase, userNumbers, userSpecial)
                
                print("Here is your password:", password)
                print("If you like your password, type 1 to assign the password. If you wish for another password, type 2 to generate another.")
                y = int(input())
                if y == 1:
                    x += 1
                    passwordLabeling = input("What would you like to label this password as? ")
                    userPasswordUnit = passwordLabeling + ":" + password
                    filePasswords.passwordEntries.append(userPasswordUnit)
                    print("Password has been stored")
                    
                elif y == 2:
                    x == 1
    elif x == 2:
        userPasswordName = input("Input the name of the password: ")
        userPasswordPassword = input("Input the password: ")
        userPasswordUnit = userPasswordName + ":" + userPasswordPassword
        filePasswords.passwordEntries.append(userPasswordUnit)
        print("Password has been stored")
        pass
    elif x == 3:
        print("Passwords:")
        for oj in filePasswords.passwordEntries:
            print(oj)
    elif x == 4:
        programUpkeep = False
        filePasswords.endingProgram("Passwords.csv")
        print("Exiting the program.")
    else:
        print("Invalid choice. Please try again.")