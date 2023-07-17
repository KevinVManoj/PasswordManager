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

        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        
        specialCharacters = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "_", "=", ":", ";", "?"]

        totalLength = upperCase + lowerCase + numbers + specialCharacters

        a = False
        passwordChars = []

        while a == False:
            for x in totalLength:
                chance = random.randint(1,4)
                if chance == 1:
                    passwordChars.append(upperAlphabet[(int)(random() * (upperAlphabet.length - 1))])
                    upperCaseCount += 1
                elif chance == 2:
                    passwordChars.append(lowerAlphabet[(int)(random() * (lowerAlphabet.length - 1))])
                    lowerCaseCount += 1
                elif chance == 3:
                    passwordChars.append(numbers[(int)(random() * (numbers.length - 1))])
                    numbersCount += 1
                elif chance == 4:
                    passwordChars.append(specialCharacters[(int)(random() * (specialCharacters.length - 1))])
                    specialCharactersCount += 1
                passwordString = ''.join(passwordChars)

            if upperCaseCount == upperCase and lowerCaseCount == lowerCase and numbersCount == numbers and specialCharactersCount == specialCharacters:
                return passwordString
            