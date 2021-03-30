import sys, os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pathlib
import time
import unittest
from tests.base_test import BaseTest
from pages.base_page import BasePage
from pages.ProductPage import ProductPage
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage
from utils.test_cases import test_cases

from selenium import webdriver


class TestAddProducts(BaseTest):

    def test_add_ip(self):
        print("\n" + str(test_cases(0)))
        page = LoginPage(self.driver)
        page1 = WelcomePage(self.driver)
        page2 = ProductPage(self.driver)
        page3 = BasePage(self.driver)

        time.sleep(2)
        page.login()

        time.sleep(2)

        time.sleep(2)
        page1.click_ip_and_Products_tab()

        time.sleep(2)

        # time.sleep(2)
        # page2.click_add_new_ip()
        #
        # time.sleep(5)
        # self.driver.switch_to.frame(0)

        time.sleep(2)
        page2.fill_up_add_product()
        time.sleep(2)