import pytest
from selenium import webdriver

from Pages.AddRemovePage import AddRemovePage
from Pages.AuthPage import AuthPage
from Pages.ContextMenuPage import ContextMenuPage
from Pages.DropdownPage import DropdownPage
from Pages.HomePage import HomePage
from Pages.ImgPage import ImgPage
from Pages.LoginPage import LoginPage


@pytest.fixture(params=["chrome"], scope="class")
def driver_init(request):
    web_driver = None
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    web_driver.maximize_window()
    web_driver.implicitly_wait(10)
    request.cls.homePage = HomePage(web_driver)
    request.cls.loginPage = LoginPage(web_driver)
    request.cls.authPage = AuthPage(web_driver)
    request.cls.imgPage = ImgPage(web_driver)
    request.cls.addRemove = AddRemovePage(web_driver)
    request.cls.contextMenu = ContextMenuPage(web_driver)
    request.cls.Dropdown = DropdownPage(web_driver)

    yield
    web_driver.close()
