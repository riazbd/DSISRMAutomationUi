import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import pathlib
import time
import unittest
from tests.base_test import BaseTest
from pages.base_page import BasePage
from pages.IP_and_products_page import IPandProductsPage
from pages.login_page import LoginPage
from pages.welcome_page import WelcomePage
from utils.cases import cases

from selenium import webdriver


class TestAddIp(BaseTest):
    
    def test_add_ip(self):
        print("\n" + str(cases(0)))
        page = LoginPage(self.driver)
        page1 = WelcomePage(self.driver)
        page2 = IPandProductsPage(self.driver)

        time.sleep(2)
        page.login()

        time.sleep(2)
        page1.click_ip_and_Products_tab()
        time.sleep(2)
        page2.fill_up_add_ip()
        time.sleep(2)
