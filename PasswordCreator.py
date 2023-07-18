import random
import string

class PasswordCreator:
    def __init__(self, upperCase, lowerCase, numbers, specialCharacters):
        self.upperCase = upperCase
        self.lowerCase = lowerCase
        self.numbers = numbers
        self.specialCharacters = specialCharacters

    def generatePassword(self, upperCase, lowerCase, numbers, specialCharacters):
        upperAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        lowerAlphabet = ["a", "b", "c",
            "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
            "u", "v", "w", "x", "y", "z"]

        numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        
        specialCharacterList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "_", "=", ":", ";", "?"]
        
        totalLength = 0
        totalLength += upperCase
        totalLength += lowerCase  
        totalLength += numbers
        totalLength += specialCharacters

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
                    passwordChars.append(upperAlphabet[(int)(random() * (upperAlphabet.length - 1))])
                    upperCaseCount += 1
                elif chance == 2:
                    passwordChars.append(lowerAlphabet[(int)(random() * (lowerAlphabet.length - 1))])
                    lowerCaseCount += 1
                elif chance == 3:
                    passwordChars.append(numberList[(int)(random() * (numberList.length - 1))])
                    numbersCount += 1
                elif chance == 4:
                    passwordChars.append(specialCharacterList[(int)(random() * (specialCharacterList.length - 1))])
                    specialCharactersCount += 1
                passwordString = ''.join(passwordChars)

            if upperCaseCount == upperCase and lowerCaseCount == lowerCase and numbersCount == numbers and specialCharactersCount == specialCharacters:
                return passwordString
                a = True
            