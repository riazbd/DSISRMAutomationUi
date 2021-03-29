import pathlib #Added This line to skip error
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import ExcelUtils


# I am using python unittest for asserting cases.
# In this module, there should be test cases.
# If you want to run it, you should type: python <module-name.py>

class BaseTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        # options.add_argument("--headless") # Runs Chrome in headless mode.
        # options.add_argument('--no-sandbox')  # # Bypass OS security model
        # options.add_argument('disable-infobars')
        # options.add_argument("--disable-extensions")
        options.add_argument("--start-fullscreen")
        # options.add_argument('--disable-gpu')

        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Firefox(executable_path=pathlib.Path(__file__).parent / "../browser/geckodriver")
        self.driver.set_page_load_timeout(300)
        self.path = pathlib.Path(__file__).parent / "../utils/Client 1 - Activision.xlsx"
        # self.driver.get("https://qareceivables.dsidrm.com/signin")
        self.driver.get(ExcelUtils.readData(self.path, 'LoginData', 2, 3))

    def tearDown(self):
        self.driver.close()


class TestPages(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestPages)
    unittest.TextTestRunner(verbosity=1).run(suite)
