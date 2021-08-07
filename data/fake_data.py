from faker import Faker
import random

fake = Faker()

class DataToTest:

    def getName(self):
        return fake.name()

    def getEmail(self):
        return fake.email()

    def getPassword(self):
        return fake.password()

    def getYear(self):
        return random.randint(1970, 2000)

    def getMonth(self):
        return random.randint(1, 12)

    def getDay(self):
        return random.randint(1, 28)

    def getGender(self):
        choose = random.randint(1, 3)
        if choose == 1:
            return 'male'
        elif choose == 2:
            return 'female'
        else:
            return 'unknown'

    def getCountry(self):
        return random.randint(1, 163)


