import pathlib
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import time

from pages.base_page import BasePage
from pages.welcome_page import WelcomePage
from utils import ExcelUtils
from utils.locators import *


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)  # Python2 version

    def enter_email(self, username):
        time.sleep(1)
        self.find_element(*self.locator.input_username).send_keys(username)

    def enter_password(self, password):
        time.sleep(1)
        self.find_element(*self.locator.input_password).send_keys(password)

    def click_login_button(self):
        time.sleep(1)
        self.find_element(*self.locator.login_button).click()

    def login(self):
        path = pathlib.Path(__file__).parent / "../utils/TestData_riaz.xlsx"
        client = ExcelUtils.readData(path, 'config', 2, 2)
        row = ExcelUtils.getRowCount(path, client)

        for r in range(2, row + 1):
            username = ExcelUtils.readData(path, client, r, 1)
            password = ExcelUtils.readData(path, client, r, 2)
            time.sleep(1)
            self.enter_email(username)
            time.sleep(1)
            self.enter_password(password)
            time.sleep(1)
            self.click_login_button()
            return WelcomePage(self.driver)

    def login_with_valid_user(self, user):
        self.login(user)
        return WelcomePage(self.driver)

    def login_with_in_valid_user(self, user):
        self.login(user)
        return self.find_element(*self.locator.ERROR_MESSAGE).text
