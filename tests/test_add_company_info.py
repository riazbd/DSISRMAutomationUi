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
from utils.cases import cases

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestAddCompanyInfo(BaseTest):
    
    def test_sign_in(self):
        print("\n" + str(cases(0)))
        page = LoginPage(self.driver)
        page1 = WelcomePage(self.driver)
        page2 = CompaniesAndContactPage(self.driver)
        time.sleep(2)
        page.login()
        #
        # time.sleep(2)
        # search_result = page1.check_page_loaded()
        time.sleep(2)
        page1.click_companies_contacts_tab()

        time.sleep(2)
        self.assertIn("Find/View", page1.get_title())
        time.sleep(2)
        page2.fill_up_company_info()
        time.sleep(2)



