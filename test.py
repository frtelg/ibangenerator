import unittest
import random
import re
from iban import Iban
from namesgenerator import Person

class GenerateIbanTestCase(unittest.TestCase):
    def runTest(self):
        iban = Iban.generate_iban()
        assert re.match(r"^NL[0-9]{2}[A-Z]{4}[0-9]{10}$", iban.iban)

class GeneratePersonTestCase(unittest.TestCase):
    def runTest(self):
        person = Person.random_dude()
        assert person != None

def suite():
    testSuite = unittest.TestSuite()
    testSuite.addTest(GenerateIbanTestCase("test IBAN"))
    testSuite.addTest(GeneratePersonTestCase("test Person"))
    return testSuite

if __name__ == "__main__":
    unittest.main()