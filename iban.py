# created by Franke Telgenhof
# version 1.0: 2018-08-16
# version 1.1: 2018-09-24
# version 1.2: 2018-11-14

import random
import pyperclip

class Iban:
    def __init__(self, iban):
        self.iban = iban

    @staticmethod
    def execute_eleven_test(bank_number):
        bank_number_int = int(bank_number)
        if bank_number_int % 11 == 0:
            return 1
        else: 
            return 0

    @staticmethod
    def string_to_int(bank_string):
        bank_array = list(bank_string)
        i = 0
        for x in bank_array:
            if x.isdigit() == False:
                bank_array[i] = ord(x) - 55
            i = i + 1

        i = 0
        for x in bank_array:
            bank_array[i] = str(bank_array[i])
            i = i + 1

        bank_string = ''.join(bank_array)
        return bank_string

    @staticmethod
    def convert_iban_to_int(bank_string):
        control_number = bank_string[4] + bank_string[5]
        control_int = int(control_number)

        if control_int < 2 or control_int > 98: 
            return 0
        else: 
            first_part = bank_string[0:6]
            second_part = bank_string[6:]
            mod97_control_number = second_part + first_part
            mod97_control_number = int(mod97_control_number)
            return mod97_control_number

    @staticmethod
    def define_control_number(bank,bank_account):
        bank = str(Iban.string_to_int(bank))
        bank_account_string = str(bank_account)
        control_number_input = bank_account_string + bank
        control_number_input = int(control_number_input)
        control_number_mod = control_number_input % 97
        control_number = 98 - control_number_mod
        if control_number < 10:
            control_number = str(control_number)
            control_number = '0' + control_number
        else: 
            control_number = str(control_number)
        return control_number

    @staticmethod
    def mod97(mod97_control_number):
        checksum = mod97_control_number % 97
        return checksum == 1

    @staticmethod
    def random_bank():
        bank_array = ['INGB', 'SNSB', 'RABO', 'ABNA', 'TRIO', 'ASNB', 'DEUT', 'AEGO', 'BICK', 'KNAB']
        random_bank = bank_array[random.randint(0,9)]
        return random_bank

    @staticmethod
    def generate_bank_account():
        test = 0

        while test == 0:
            account_array = []

            for _ in range(10):
                account_array.append(str(random.randint(0,9)))
            
            generated_bank_account = ''.join(account_array)
            test = Iban.execute_eleven_test(generated_bank_account)

        bank_string = generated_bank_account
        return bank_string

    @classmethod
    def generate_iban(cls): 
        outcome = False

        while outcome == False:
            country = 'NL'
            bank = Iban.random_bank()
            bank_account = Iban.generate_bank_account()
            control_number = Iban.define_control_number(bank,bank_account)
            generated_iban = country + control_number + bank + bank_account
            int_iban = Iban.string_to_int(generated_iban)
            int_iban = Iban.convert_iban_to_int(int_iban)
            outcome = Iban.mod97(int_iban)

        return cls(generated_iban)

if __name__ == '__main__':
    random_iban = Iban.generate_iban()
    pyperclip.copy(random_iban.iban)
    print(random_iban.iban)