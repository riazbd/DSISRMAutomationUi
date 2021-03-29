import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pathlib
import time
import unittest
from pages.base_page import BasePage
from pages.companies_contact_page import CompaniesAndContactPage
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage
from tests.base_test import BaseTest
from utils.test_cases import test_cases

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestAddCompanyInfo(BaseTest):
    
    def test_sign_in(self):
        print("\n" + str(test_cases(0)))
        page = LoginPage(self.driver)
        page1 = WelcomePage(self.driver)
        page2 = CompaniesAndContactPage(self.driver)
        # page3 = BasePage(self.driver)

        time.sleep(2)
        page.login()

        time.sleep(2)
        search_result = page1.check_page_loaded()
        # time.sleep(2)
        # self.assertIn("https://qareceivables.dsidrm.com/WelcomePage.aspx", search_result)

        time.sleep(2)
        page1.click_companies_contacts_tab()

        time.sleep(2)
        self.assertIn("Find/View", page1.get_title())
        # time.sleep(2)
        # self.assertIn("Find/View", page1.get_title())
        #
        # time.sleep(2)
        # page2.click_add_new_company()
        #
        # time.sleep(2)
        #
        # self.driver.switch_to.frame(1)

        time.sleep(2)
        page2.fill_up_company_info()
        time.sleep(2)



