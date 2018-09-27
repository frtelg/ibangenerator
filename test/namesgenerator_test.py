from namesgenerator import Person

testPerson = Person("Jan", "Janssen", "1990-11-16", "janjanssen@testmail.com", "M")
print(testPerson.birthDateTranslation)
print(testPerson.genderTranslation)

try:
    invalidDate = Person("Jan", "Janssen", "16-11-1990", "janjanssen@testmail.com", "M")
    print(invalidDate.birthDateTranslation)
except ValueError:
    print("Invalid date test successful")

try:
    invalidGender = Person("Jan", "Janssen", "1990-11-16", "janjanssen@testmail.com", "A")
    print(invalidGender.birthDateTranslation)
except ValueError:
    print("Invalid gender test successful")

testDude = Person.randomDude()
print(testDude.firstName)
print(testDude.birthDate)