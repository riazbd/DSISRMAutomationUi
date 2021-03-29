import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pathlib
import time
import unittest
from tests.base_test import BaseTest
from pages.base_page import BasePage
from pages.cantact_details_page import AddContactsPage
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage
from utils.test_cases import test_cases

from selenium import webdriver

#This Code is from Riaz
class TestAddContacts(BaseTest):
    
    # This section should be under BaseTest Class and you need to extend the BaseTest EveryTime
    # up to this section

    def test_add_contacts(self):
        print("\n" + str(test_cases(0)))
        page = LoginPage(self.driver)
        page1 = WelcomePage(self.driver)
        page2 = AddContactsPage(self.driver)
        # page3 = BasePage(self.driver)
        #
        time.sleep(3)
        page.login()

        time.sleep(2)
        #  this line should be corrected
        page1.click_companies_contacts_tab()

        
        
        # time.sleep(2)
        # self.driver.switch_to.frame("ctl00_MainContent_ifrmCompanyContact")
        # page2 = AddContactsPage(self.driver)

        time.sleep(2)

        # time.sleep(2)
        # page2.click_add_new_contacts()
        #
        # time.sleep(5)
        # self.driver.switch_to_default_content()
        # self.driver.switch_to.frame("ctl00_MainContent_WndHostctrl1_ifrm")

        time.sleep(2)
        page2.fill_up_add_contacts()
        time.sleep(2)
# This section should be under BaseTest Class and you need to extend the BaseTest EveryTime
# up to this section
