from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import data.fake_data


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver
        self.nick = (By.NAME, "nickname")
        self.email = (By.NAME, "email")
        self.password = (By.NAME, "subject_password")
        self.password2 = (By.NAME, "subject_password_for_confirmation")
        self.year = (By.NAME, "birth_year")
        self.month = (By.NAME, "birth_month")
        self.day = (By.NAME, "birth_day")
        self.gender = (By.ID, "register-form_pc_select_0")
        self.country = (By.ID, "country-field")
        self.checkbox = (By.CLASS_NAME, "c-checkbox")
        self.complete_button = (By.ID, "register-form_pc_button_5")
        self.complete_button2 = (By.ID, "register-email-opt-in-form_pc_button_2")
        self.unfinished_form = (By.CLASS_NAME, "c-attention_inner")
        self.data = data.fake_data.DataToTest()




    def fillRegisterForm(self):

        self.driver.find_element(*self.nick).send_keys(self.data.getName())
        self.driver.find_element(*self.email).send_keys(self.data.getEmail())


        pass_to_use = self.data.getPassword()
        self.driver.find_element(*self.password).send_keys(pass_to_use)
        self.driver.find_element(*self.password2).send_keys(pass_to_use)

        year = Select(self.driver.find_element(*self.year))
        year.select_by_value(str(self.data.getYear()))

        month = Select(self.driver.find_element(*self.month))
        month.select_by_value(str(self.data.getMonth()))

        day = Select(self.driver.find_element(*self.day))
        day.select_by_value(str(self.data.getDay()))

        gender = Select(self.driver.find_element(*self.gender))
        gender.select_by_value(self.data.getGender())

        country = Select(self.driver.find_element(*self.country))
        country.select_by_value(str(self.data.getCountry()))

        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.complete_button).click()

        self.driver.find_element(*self.complete_button2).click()

        finish = self.driver.find_element(*self.unfinished_form).text

        if finish == "Account creation is not complete.":
            print("This is the end of automation.")
