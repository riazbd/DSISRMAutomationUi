import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import pathlib

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from utils import ExcelUtils
from utils.locators import IPandProductsPageLocators


class IPandProductsPage(BasePage):
    def __init__(self, driver):
        self.locator = IPandProductsPageLocators
        super(IPandProductsPage, self).__init__(driver)  # Python2 version

    def click_add_new_ip(self):
        self.find_element(*self.locator.addNewIP).click()

    def add_licensor(self):
        self.find_element(*self.locator.Addlicensor).click()

    def search_licensor(self, licensor):
        self.find_element(*self.locator.searchLicensor).send_keys(licensor)

    def check_licensor(self):
        self.find_element(*self.locator.checkLicensor).click()

    def done_check_licensor(self):
        self.find_element(*self.locator.LicensorCheckDone).click()

    def enter_intel_prop(self, intel):
        self.find_element(*self.locator.intellectualProperty).send_keys(intel)

    def enter_primary_id(self, id):
        self.find_element(*self.locator.primaryID).send_keys(id)

    def enter_owner(self, owner):
        self.find_element(*self.locator.owner).send_keys(owner)



    def add_ip_type(self):
        self.find_element(*self.locator.addIPType).click()

    def search_ip_type(self, ipType):
        self.find_element(*self.locator.searchIPType).send_keys(ipType)

    def check_ip_type(self):
        self.find_element(*self.locator.checkIPType).click()

    def done_check_ip_type(self):
        self.find_element(*self.locator.checkIPTypeDone).click()





    def select_language(self, language):
        select = Select(self.find_element(*self.locator.Language))
        select.select_by_visible_text(language)
        # select.select_by_index(4)

    def Click_Save_Button(self):
        self.find_element(*self.locator.saveButton2).click()


    def fill_up_add_ip(self):
        path = pathlib.Path(__file__).parent / "../utils/TestData_riaz.xlsx"
        client = ExcelUtils.readData(path, 'config', 2, 2)
        row = ExcelUtils.getRowCount(path, client)

        for r in range(2, row + 1):
            licensor = ExcelUtils.readData(path, client, r, 8)
            intel = ExcelUtils.readData(path, client, r, 9)
            primaryId = ExcelUtils.readData(path, client, r, 10)
            owner = ExcelUtils.readData(path, client, r, 11)
            lang = ExcelUtils.readData(path, client, r, 12)
            ipType = ExcelUtils.readData(path, client, r, 13)
            ts = str(time.time())
            time.sleep(1)
            self.add_licensor()

            time.sleep(1)
            self.search_licensor(licensor)

            time.sleep(1)
            self.check_licensor()

            time.sleep(1)
            self.done_check_licensor()

            time.sleep(1)
            self.enter_intel_prop(intel + " " + ts)

            time.sleep(1)
            self.enter_primary_id(primaryId + " " + ts)

            time.sleep(1)
            self.enter_owner(owner)

            time.sleep(1)
            self.add_ip_type()

            time.sleep(1)
            self.search_ip_type(ipType)

            time.sleep(1)
            self.check_ip_type()

            time.sleep(1)
            self.done_check_ip_type()

            # time.sleep(1)
            # self.select_language(lang)

            time.sleep(1)
            self.Click_Save_Button()


            return IPandProductsPage(self.driver)