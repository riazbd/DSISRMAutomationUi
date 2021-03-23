import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import pathlib

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from utils import ExcelUtils
from utils.locators import CompaniesAndContactPageLocators


class CompaniesAndContactPage(BasePage):
    def __init__(self, driver):
        self.locator = CompaniesAndContactPageLocators
        super(CompaniesAndContactPage, self).__init__(driver)  # Python2 version

    def click_add_new_company(self):
        self.find_element(*self.locator.addNewCompanyLocator).click()

    def get_window_handle(self, num):
        return self.driver.window_handles[num]
    # def window_selection(self):
    #     p = self.driver.current_window_handle
    #     # get first child window
    #     chwnd = self.driver.window_handles
    #     for w in chwnd:
    #     #switch focus to child window
    #         if (w != p):
    #             self.driver.switch_to.window(w)
    #         break

    def switch_window(self, win):
        return self.driver.switch_to_window(win)


    def enter_company_name(self, companyName):
        self.find_element(*self.locator.CompanyName).send_keys(companyName)

    def add_business_category(self):
        self.find_element(*self.locator.BusinessCategory).click()

    def search_business_category(self, businessCategory):
        self.find_element(*self.locator.SearchBusinessCategory).send_keys(businessCategory)

    def check_business_category(self):
        self.find_element(*self.locator.BusinessCategoryCheckBox).click()

    def done_check_business_category(self):
        self.find_element(*self.locator.BusinessCategoryDone).click()

    def enter_address(self, address):
        self.find_element(*self.locator.AddressField1).send_keys(address)

    def enter_city(self, city):
        self.find_element(*self.locator.cityInput).send_keys(city)

    def enter_zipcode(self, zipcode):
        self.find_element(*self.locator.zipCode).send_keys(zipcode)

    def select_country(self, country):
        select = Select(self.find_element(*self.locator.CountrySelect))
        select.select_by_visible_text(country)
        # select.select_by_index(4)

    def Click_Save_Button(self):
        self.find_element(*self.locator.saveButton).click()


    def fill_up_company_info(self):
        path = pathlib.Path(__file__).parent / "../utils/TestData_riaz.xlsx"
        client = ExcelUtils.readData(path, 'config', 2, 2)
        row = ExcelUtils.getRowCount(path, 'testData')

        for r in range(2, row + 1):
            companyName = ExcelUtils.readData(path, client, r, 3)
            businessCategory = ExcelUtils.readData(path, client, r, 4)
            address = ExcelUtils.readData(path, client, r, 5)
            city = ExcelUtils.readData(path, client, r, 6)
            country = ExcelUtils.readData(path, client, r, 7)
            ts = str(time.time())
            time.sleep(1)
            self.enter_company_name(companyName + " "+ts)

            time.sleep(1)
            self.add_business_category()

            time.sleep(1)
            self.search_business_category(businessCategory)

            time.sleep(1)
            self.check_business_category()

            time.sleep(1)
            self.done_check_business_category()

            time.sleep(1)
            self.enter_address(address)

            time.sleep(1)
            self.enter_city(city)

            time.sleep(1)
            self.select_country(country)

            time.sleep(1)
            self.Click_Save_Button()


            return CompaniesAndContactPage(self.driver)