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
from utils.cases import cases

class TestAddContacts(BaseTest):

    def test_add_contacts(self):
        print("\n" + str(cases(0)))
        page = LoginPage(self.driver)
        page1 = WelcomePage(self.driver)
        page2 = AddContactsPage(self.driver)
        time.sleep(3)
        page.login()

        time.sleep(2)
        page1.click_companies_contacts_tab()

        time.sleep(2)
        page2.fill_up_add_contacts()
        time.sleep(2)

