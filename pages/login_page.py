import pathlib
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
import time

from pages.base_page import BasePage
from pages.welcome_page import WelcomePage
from utils import ExcelUtils
from utils.locators import *
from utils.testData import TestData


class LoginPage(BasePage):
    def __init__(self, driver):
        self.locator = LoginPageLocators
        super(LoginPage, self).__init__(driver)

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
        path = pathlib.Path(__file__).parent / "../utils/testConfig.xlsx"
        client = ExcelUtils.readData(path, 'testConfig', TestData.clientID + 1, 1)
        clientPath = pathlib.Path(__file__).parent / "../utils" / client
        row = ExcelUtils.getRowCount(clientPath, 'LoginData')
        for r in range(2, row + 1):
                username = ExcelUtils.readData(clientPath, 'LoginData', r, 1)
                password = ExcelUtils.readData(clientPath, 'LoginData', r, 2)
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
