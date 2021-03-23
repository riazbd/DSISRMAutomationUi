import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import pathlib

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from utils import ExcelUtils
from utils.locators import ContactsLocator


class AddContactsPage(BasePage):
    def __init__(self, driver):
        self.locator = ContactsLocator
        super(AddContactsPage, self).__init__(driver)  # Python2 version

    def click_add_new_contacts(self):
        self.find_element(*self.locator.addContactsLocator).click()

    
    def select_situation(self, situation):
        select = Select(self.find_element(*self.locator.situation))
        select.select_by_visible_text(situation)

    def add_firstName(self, firstName):
        self.find_element(*self.locator.firstName).send_keys(firstName)

    def add_lastname(self, lastName):
        self.find_element(*self.locator.LastName).send_keys(lastName)

    def add_email(self, email):
        self.find_element(*self.locator.email).send_keys(email)

    
    def add_role(self):
        self.find_element(*self.locator.addRoles).click()

    def search_role(self, role):
        self.find_element(*self.locator.searchRole).send_keys(role)

    def check_role(self):
        self.find_element(*self.locator.checkRole).click()

    def check_role_done(self):
        self.find_element(*self.locator.checkRoleDone).click()

    def Click_Save_Button(self):
        self.find_element(*self.locator.saveBtn3).click() 

    
    def fill_up_add_contacts(self):
        path = pathlib.Path(__file__).parent / "../utils/TestData_riaz.xlsx"
        client = ExcelUtils.readData(path, 'config', 2, 2)
        row = ExcelUtils.getRowCount(path, client)

        for r in range(2, row + 1):
            situation = ExcelUtils.readData(path, client, r, 14)
            firstName = ExcelUtils.readData(path, client, r, 15)
            lastName = ExcelUtils.readData(path, client, r, 16)
            email = ExcelUtils.readData(path, client, r, 17)
            role = ExcelUtils.readData(path, client, r, 18)
            ts = str(time.time())

            time.sleep(1)
            self.select_situation(situation)

            time.sleep(1)
            self.add_firstName(firstName)

            time.sleep(1)
            self.add_lastname(lastName + " " + ts)

            time.sleep(1)
            self.add_email(email)

            time.sleep(1)
            self.add_role()

            time.sleep(1)
            self.search_role(role)

            time.sleep(1)
            self.check_role()

            time.sleep(1)
            self.check_role_done()

            time.sleep(1)
            self.Click_Save_Button()

            return AddContactsPage(self.driver)