import pytest
from selenium import webdriver
from Pages.LoginPage import LoginPage


@pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    web_driver = None
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    web_driver.implicitly_wait(10)
    request.cls.loginPage = LoginPage(web_driver)

    yield
    web_driver.close()
