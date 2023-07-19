import random
import string

upperAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
        "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

lowerAlphabet = ["a", "b", "c",
        "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y", "z"]

numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

specialCharacterList = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "_", "=", ":", ";", "?"]
        
upperCaseCount = 0
lowerCaseCount = 0
numbersCount = 0
specialCharactersCount = 0
passwordChars = []
a = True

while a == True:
    for x in range(20):
            chance = random.randint(1,4)
            if chance == 1:
                passwordChars.append(random.choice(upperAlphabet))
                upperCaseCount += 1
            elif chance == 2:
                passwordChars.append(random.choice(lowerAlphabet))
                lowerCaseCount += 1
            elif chance == 3:
                passwordChars.append(str(random.choice(numberList)))
                numbersCount += 1
            elif chance == 4:
                passwordChars.append(random.choice(specialCharacterList))
                specialCharactersCount += 1
    passwordString = ''.join(passwordChars)
    print()
    print(passwordString)
    
    if(upperCaseCount == 5 and specialCharactersCount == 5 and numbersCount == 5 and lowerCaseCount == 5):
        a = False

    upperCaseCount = 0
    lowerCaseCount = 0
    numbersCount = 0
    specialCharactersCount = 0
    passwordChars = []
