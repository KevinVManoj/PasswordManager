import random
import string

class PasswordCreator:
    def __init__(self, upperCase, lowerCase, numbers, specialCharacters):
        self.upperCase = upperCase
        self.lowerCase = lowerCase
        self.numbers = numbers
        self.specialCharacters = specialCharacters

    def generatePassword(self, upperCase, lowerCase, numbers, specialCharacters):
        specialCharacterList = list("!@#$%^&*()-+_=:;?")
        
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
            #print()
            passwordString = ''.join(passwordChars)

            if (upperCaseCount == self.upperCase and lowerCaseCount == self.lowerCase and numbersCount == self.numbers and specialCharactersCount == self.specialCharacters):
                print(passwordString)
                a = True
            else:
                a = False
            
            upperCaseCount = 0
            lowerCaseCount = 0
            numbersCount = 0
            specialCharactersCount = 0
            passwordChars = []
        return passwordString