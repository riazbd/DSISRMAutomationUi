import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import pathlib

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from utils import ExcelUtils
from utils.locators import ContactsLocator
from pages.welcome_page import WelcomePage
from pages.login_page import LoginPage
from utils.test_cases import test_cases
from utils.testData import TestData


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

    def uploadImage(self):
        # avatarPath = pathlib.Path(__file__).parent / "../photos/avatar.jpg"
        self.find_element(*self.locator.addPhoto).click()
        # self.find_element(*self.locator.fileUpload).clear()
        time.sleep(3)
        self.find_element(*self.locator.fileUpload).send_keys(os.getcwd()+"/photos/avatar.jpg")
        self.find_element(*self.locator.buttonUplaod).click()

    def click_systemUser(self):
        self.find_element(*self.locator.systemUser).click()

    def click_inernalUser(self):
        self.find_element(*self.locator.internalUser).click()

    def click_externalUser(self):
        self.find_element(*self.locator.externalUser).click()

    
    def fill_up_add_contacts(self):
        path = pathlib.Path(__file__).parent / "../utils/testConfig.xlsx"
        client = ExcelUtils.readData(path, 'testConfig', TestData.clientID + 1, 1)
        clientPath = pathlib.Path(__file__).parent / "../utils" / client
        row = ExcelUtils.getRowCount(clientPath, 'AddContacts')
        for r in range(2, row + 1):
                situation = ExcelUtils.readData(clientPath, 'AddContacts', r, 1)
                firstName = ExcelUtils.readData(clientPath, 'AddContacts', r, 2)
                lastName = ExcelUtils.readData(clientPath, 'AddContacts', r, 3)
                email = ExcelUtils.readData(clientPath, 'AddContacts', r, 4)
                role = ExcelUtils.readData(clientPath, 'AddContacts', r, 5)
                SysUser = ExcelUtils.readData(clientPath, 'AddContacts', r, 6)
                ts = str(time.time())

                # page = LoginPage(self.driver)
                # page1 = WelcomePage(self.driver)
                # # page2 = AddContactsPage(self.driver)
                # # page3 = BasePage(self.driver)
                #
                # time.sleep(3)
                # page.login()
                #
                # time.sleep(2)
                # #  this line should be corrected
                # page1.click_companies_contacts_tab()
                self.driver.switch_to_default_content()
                time.sleep(2)
                self.driver.switch_to.frame("ctl00_MainContent_ifrmCompanyContact")

                time.sleep(2)
                self.click_add_new_contacts()

                time.sleep(5)
                self.driver.switch_to_default_content()
                self.driver.switch_to.frame("ctl00_MainContent_WndHostctrl1_ifrm")

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
                self.uploadImage()

                time.sleep(1)
                self.click_systemUser()

                if SysUser == "Internal":
                    time.sleep(1)
                    self.click_inernalUser()
                elif SysUser == "External":
                    time.sleep(1)
                    self.click_externalUser()


                time.sleep(1)
                self.Click_Save_Button()

                time.sleep(3)
                #
                # return AddContactsPage(self.driver)