from PasswordCreator import PasswordCreator

print("Welcome to Kevin's password manager,")
print("You can either create a new password for a service you use with your own requirements")
print("Or you can access your passwords")

print("1. Create a new password")
print("2. Access passwords")

x = int(input())
if x == 1:
    userUppercase = int(input("How many uppercase letters would you like? "))
    userLowercase = int(input("How many lowercase letters would you like? "))
    userNumbers = int(input("How many numbers would you like? "))
    userSpecial = int(input("How many special characters would you like? "))

    password_generator = PasswordCreator(userUppercase, userLowercase, userNumbers, userSpecial)
    password = password_generator.generatePassword(userUppercase, userLowercase, userNumbers, userSpecial)
    
    print("If you like your password, type 1 to assign the password. If you wish for another password, type 2 to generate another.")
    #MAKE THE OPTION BABABABABABABABA
    
