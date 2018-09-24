import random
import pyperclip

def elevenTest(bankNumber):
    bankNumber = int(bankNumber)
    if bankNumber % 11 == 0:
        return 1
    else: 
        return 0

def stringToInt(bankString):
    bankArray = list(bankString)
    i = 0
    for x in bankArray:
        if x.isdigit() == False:
            bankArray[i] = ord(x) - 55
        i = i + 1
    
    i = 0
    for x in bankArray:
        bankArray[i] = str(bankArray[i])
        i = i + 1
    
    bankString = ''.join(bankArray)
    return bankString

def convertIbanToInt(bankString):
    controlNumber = bankString[4] + bankString[5]
    controlInt = int(controlNumber)

    if controlInt < 2 or controlInt > 98: 
        return 0
    else: 
        firstPart = bankString[0:6]
        secondPart = bankString[6:]
        mod97ControlNumber = secondPart + firstPart
        mod97ControlNumber = int(mod97ControlNumber)
        return mod97ControlNumber

def defineControlNumber(bank,bankAccount):
    bank = str(stringToInt(bank))
    bankAccountString = str(bankAccount)
    controlNumberInput = bankAccountString + bank
    controlNumberInput = int(controlNumberInput)
    controlNumberMod = controlNumberInput % 97
    controlNumber = 98 - controlNumberMod
    if controlNumber < 10:
        controlNumber = str(controlNumber)
        controlNumber = '0' + controlNumber
    else: 
        controlNumber = str(controlNumber)
    return controlNumber

def mod97(mod97ControlNumber):
    checkSum = mod97ControlNumber % 97
    if checkSum == 1:
        return True
    else: 
        return False

def randomBank():
    bankArray = ['INGB', 'SNSB', 'RABO', 'ABNA', 'TRIO', 'ASNB', 'DEUT', 'AEGO', 'BICK', 'KNAB']
    randomBank = bankArray[random.randint(0,9)]
    return randomBank

def generateBankAccount():
    accountArray = [0,0,0,0,0,0,0,0,0,0]
    test = 0
    
    while test == 0:
        i = 0
        for x in accountArray:
            accountArray[i] = str(random.randint(1,9))
            i = i + 1
        
        generatedBankAccount = ''.join(accountArray)
        test = elevenTest(generatedBankAccount)
    
    bankString = generatedBankAccount
    return bankString

def generateIban(): 
    outcome = False

    while outcome == False:
        country = 'NL'
        bank = randomBank()
        bankAccount = generateBankAccount()
        controlNumber = defineControlNumber(bank,bankAccount)
        generatedIban = country + controlNumber + bank + bankAccount
        intIban = stringToInt(generatedIban)
        intIban = convertIbanToInt(intIban)
        outcome = mod97(intIban)

    return generatedIban

randomIban = generateIban()
pyperclip.copy(randomIban)
print(randomIban)