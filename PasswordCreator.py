import random
import string
from PasswordReader import PasswordReader

class PasswordCreator:
    def __init__(self, upperCase, lowerCase, numbers, specialCharacters):
        """
        Initializes the PasswordCreator class with password generation requirements.

        Args:
            upperCase (int): The number of uppercase letters in the generated password.
            lowerCase (int): The number of lowercase letters in the generated password.
            numbers (int): The number of numbers in the generated password.
            specialCharacters (int): The number of special characters in the generated password.
        """
        self.upperCase = upperCase
        self.lowerCase = lowerCase
        self.numbers = numbers
        self.specialCharacters = specialCharacters

    def generatePassword(self, upperCase, lowerCase, numbers, specialCharacters):
        """
        Generates a password based on specified requirements.

        Args:
            upperCase (int): The number of uppercase letters in the generated password.
            lowerCase (int): The number of lowercase letters in the generated password.
            numbers (int): The number of numbers in the generated password.
            specialCharacters (int): The number of special characters in the generated password.

        Returns:
            str: The generated password.
        """
        specialCharacterList = list("!@#$%^&*()-+_=;?")
        
        totalLength = self.upperCase + self.lowerCase + self.numbers + self.specialCharacters

        upperCaseCount = 0
        lowerCaseCount = 0
        numbersCount = 0
        specialCharactersCount = 0
        passwordChars = []

        a = False
        while a == False:
            for x in range(totalLength):
                chance = random.randint(1,4)
                if chance == 1:
                    passwordChars.append(random.choice(string.ascii_uppercase))
                    upperCaseCount += 1
                elif chance == 2:
                    passwordChars.append(random.choice(string.ascii_lowercase))
                    lowerCaseCount += 1 
                elif chance == 3:
                    passwordChars.append(str(random.choice(string.digits)))
                    numbersCount += 1
                elif chance == 4:
                    passwordChars.append(random.choice(specialCharacterList))
                    specialCharactersCount += 1

            passwordString = ''.join(passwordChars)

            if (upperCaseCount == self.upperCase and lowerCaseCount == self.lowerCase and numbersCount == self.numbers and specialCharactersCount == self.specialCharacters):
                return passwordString
                a = True
            else:
                a = False
            
            upperCaseCount = 0
            lowerCaseCount = 0
            numbersCount = 0
            specialCharactersCount = 0
            passwordChars = []
