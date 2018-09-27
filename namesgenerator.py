import re
import names
import random

class Person:
    def __init__(self, firstName, lastName, birthDate, eMailAddress, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.eMailAddress = eMailAddress
        self.gender = gender

        self.initials = firstName[0] + "."

        if gender == "M":
            self.genderTranslation = "De heer"

        elif gender == "F":
            self.genderTranslation = "Mevrouw"

        elif gender == "U":
            self.genderTranslation = "Onbekend"
        
        else:
            raise ValueError("A gender can only by \'M\', \'F\' or \'U\'")

        pattern = r"[1-2][0-9]{3}-(0[1-9]|1[1-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])"
        
        if re.match(pattern,birthDate):
            birthDateList = birthDate.split("-")
            self.birthDateTranslation = birthDateList[2] + "-" + birthDateList[1] + "-" + birthDateList[0]
        else:
            raise ValueError("A date should be of format \'yyyy-dd-mm\'")

    @classmethod
    def randomDude(cls):
        genderList = ['M', 'F', 'U']
        randomGender = random.choice(genderList)

        if randomGender == 'M':
            randomFirstName = names.get_first_name(gender='male')
        
        elif randomGender == 'F':
            randomFirstName = names.get_first_name(gender='female')
        
        else:
            randomFirstName = names.get_first_name()
            
        randomLastName = names.get_last_name()

        randomYear = "19" + str(random.randint(30,99)) 
        randomMonth = random.randint(1,12)

        maxDays = [1,3,5,7,8,10,12]
        minDays = [4,6,9,11]

        if randomMonth == 2:
            randomDay = random.randint(1,28)
        elif randomMonth in maxDays:
            randomDay = random.randint(1,31)
        elif randomMonth in minDays:
            randomDay = random.randint(1,30)
        else:
            raise ValueError("Month should be of value 1-12")

        if randomMonth < 10:
            randomMonth = "0" + str(randomMonth)
        else:
            randomMonth = str(randomMonth)
        
        if randomDay < 10:
            randomDay = "0" + str(randomDay)
        else:
            randomDay = str(randomDay)

        randomDate = randomYear + "-" + randomMonth + "-" + randomDay

        randomMailAddress = str.lower(randomFirstName) + str.lower(randomLastName) + "@testmail.com"
            
        return cls(randomFirstName, randomLastName, randomDate, randomMailAddress, randomGender)