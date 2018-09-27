import re

class Person:
    def __init__(self, firstName, lastName, birthDate, eMailAddress, gender):
        self.firstName = firstName
        self.lastName = lastName
        self.birthDate = birthDate
        self.eMailAddress = eMailAddress
        self.gender = gender

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