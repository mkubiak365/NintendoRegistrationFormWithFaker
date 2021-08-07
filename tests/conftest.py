from selenium import webdriver
import pytest
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup(request):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get("https://accounts.nintendo.com/register")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()