import re
import names
import random

class Person:
    def __init__(self, first_name, last_name, birth_date, email_address, gender):
        self.firstName = first_name
        self.lastName = last_name
        self.birthDate = birth_date
        self.emailAddress = email_address
        self.gender = gender

        self.initials = first_name[0] + "."

        if gender == "M":
            self.genderTranslation = "De heer"

        elif gender == "F":
            self.genderTranslation = "Mevrouw"

        elif gender == "U":
            self.genderTranslation = "Onbekend"
        
        else:
            raise ValueError("A gender can only by \'M\', \'F\' or \'U\'")

        pattern = r"[1-2][0-9]{3}-(0[1-9]|1[1-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])"
        
        if re.match(pattern,birth_date):
            birthdate_list = birth_date.split("-")
            self.birthdateTranslation = birthdate_list[2] + "-" + birthdate_list[1] + "-" + birthdate_list[0]
        else:
            raise ValueError("A date should be of format \'yyyy-dd-mm\'")

    @classmethod
    def random_dude(cls):
        gender_list = ['M', 'F', 'U']
        random_gender = random.choice(gender_list)

        if random_gender == 'M':
            random_first_name = names.get_first_name(gender='male')
        
        elif random_gender == 'F':
            random_first_name = names.get_first_name(gender='female')
        
        else:
            random_first_name = names.get_first_name()
            
        random_last_name = names.get_last_name()

        random_year = "19" + str(random.randint(30,99)) 
        random_month = random.randint(1,12)

        max_days = [1,3,5,7,8,10,12]
        min_days = [4,6,9,11]

        if random_month == 2:
            random_day = random.randint(1,28)
        elif random_month in max_days:
            random_day = random.randint(1,31)
        elif random_month in min_days:
            random_day = random.randint(1,30)
        else:
            raise ValueError("Month should be of value 1-12")

        if random_month < 10:
            random_month = "0" + str(random_month)
        else:
            random_month = str(random_month)
        
        if random_day < 10:
            random_day = "0" + str(random_day)
        else:
            random_day = str(random_day)

        random_date = random_year + "-" + random_month + "-" + random_day

        random_mail_address = str.lower(random_first_name) + str.lower(random_last_name) + "@testmail.com"
            
        return cls(random_first_name, random_last_name, random_date, random_mail_address, random_gender)