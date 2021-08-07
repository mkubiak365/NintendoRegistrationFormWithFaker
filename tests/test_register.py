import pytest
from pageObjects.register_page import RegisterPage

@pytest.mark.usefixtures("setup")
class TestRegisterForm:

    def test_register(self):
        register = RegisterPage(self.driver)
        register.fillRegisterForm()