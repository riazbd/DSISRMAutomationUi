import pathlib #Added This line to skip error
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.testData import TestData

from utils import ExcelUtils

class BaseTest(unittest.TestCase):
    path = pathlib.Path(__file__).parent / "../utils/testConfig.xlsx"
    client = ExcelUtils.readData(path, 'testConfig', TestData.clientID+1, 1)
    clientPath = pathlib.Path(__file__).parent / "../utils" / client

    def setUp(self):
            options = Options()
            options.add_argument("--start-fullscreen")
            self.driver = webdriver.Firefox(executable_path=pathlib.Path(__file__).parent / "../browser/geckodriver")
            self.driver.set_page_load_timeout(300)
            self.driver.get(ExcelUtils.readData(self.clientPath, 'LoginData', 2, 3))

    def tearDown(self):
            self.driver.close()


class TestCase(object):
    pass


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=1).run(suite)
