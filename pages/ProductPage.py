import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import pathlib

from selenium.webdriver.support.select import Select

from pages.base_page import BasePage
from utils import ExcelUtils
from utils.locators import AddProductsLocator
from utils.testData import TestData


class ProductPage(BasePage):
    def __init__(self, driver):
        self.locator = AddProductsLocator
        super(ProductPage, self).__init__(driver)  # Python2 version

    def click_product(self):
        self.find_element(*self.locator.productsMenuLocator).click()

    def click_add_new(self):
        self.find_element(*self.locator.addNewLocator).click()

    def click_addNew2(self):
        self.find_element(*self.locator.aDDnewLocator).click()

    def input_productName(self, productName):
        self.find_element(*self.locator.productNameLocator).send_keys(productName)


    def input_primaryNumber(self, primaryNumber):
        self.find_element(*self.locator.primaryNumber).send_keys(primaryNumber)

    def Click_Save_Button(self):
        self.find_element(*self.locator.buttonSaveLocatorforProducts).click()

    def click_cancel_btn(self):
        self.find_element(*self.locator.buttonCancelLocatorProducts).click()

    def click_category(self):
        self.find_element(*self.locator.productCategoryLocator).click()

    def input_category(self, cat):
        self.find_element(*self.locator.categoryName).send_keys(cat)

    def input_catDescription(self, catdesc):
        self.find_element(*self.locator.categoryDescription).send_keys(catdesc)

    def click_showAll(self):
        self.find_element(*self.locator.showAll).click()

    def check_box(self):
        self.find_element(*self.locator.linkedToProductLocator).click()

    def click_subcategory(self):
        self.find_element(*self.locator.productSubCategoryLocator).click()

    def input_subcategory(self, subcat):
        self.find_element(*self.locator.subCategoryNameLocator).send_keys(subcat)

    def input_subcatDescription(self, subcatdesc):
        self.find_element(*self.locator.subCategoryDescriptionLocator).send_keys(subcatdesc)

    def click_article(self):
        self.find_element(*self.locator.productArticlesLocator).click()

    def input_article(self, article):
        self.find_element(*self.locator.articleNameLocator).send_keys(article)

    def input_articledesc(self, articledesc):
        self.find_element(*self.locator.articleDesciptionLocator).send_keys(articledesc)






    def fill_up_add_product(self):
        path = pathlib.Path(__file__).parent / "../utils/testConfig.xlsx"
        client = ExcelUtils.readData(path, 'testConfig', TestData.clientID + 1, 1)
        clientPath = pathlib.Path(__file__).parent / "../utils" / client
        row = ExcelUtils.getRowCount(clientPath, 'AddProduct')
        for r in range(2, row + 1):
            productName = ExcelUtils.readData(clientPath, 'AddProduct', r, 1)
            primaryNumber = ExcelUtils.readData(clientPath, 'AddProduct', r, 2)
            catName = ExcelUtils.readData(clientPath, 'AddProduct', r, 3)
            catDesc = ExcelUtils.readData(clientPath, 'AddProduct', r, 4)
            linkedToProduct = ExcelUtils.readData(clientPath, 'AddProduct', r, 5)
            subCat = ExcelUtils.readData(clientPath, 'AddProduct', r, 6)
            subCatDesc = ExcelUtils.readData(clientPath, 'AddProduct', r, 7)
            linkedToCat = ExcelUtils.readData(clientPath, 'AddProduct', r, 8)
            article = ExcelUtils.readData(clientPath, 'AddProduct', r, 9)
            articleDesc = ExcelUtils.readData(clientPath, 'AddProduct', r, 10)
            linkedTosubCat = ExcelUtils.readData(clientPath, 'AddProduct', r, 11)
            page2 = ProductPage(self.driver)
            ts = str(time.time())

            time.sleep(2)
            self.driver.switch_to_default_content()

            time.sleep(2)
            self.click_product()

            time.sleep(2)
            self.click_add_new()

            time.sleep(2)
            self.driver.switch_to_default_content()

            time.sleep(5)
            self.driver.switch_to.frame(0)

            time.sleep(2)
            self.input_productName(productName+ts)

            time.sleep(2)
            self.input_primaryNumber(primaryNumber+ts)

            time.sleep(2)
            self.Click_Save_Button()

            time.sleep(2)
            self.click_cancel_btn()

            time.sleep(2)
            self.driver.switch_to_default_content()

            time.sleep(2)
            self.click_category()

            time.sleep(2)
            self.click_addNew2()

            time.sleep(2)
            self.driver.switch_to_default_content()

            time.sleep(5)
            self.driver.switch_to.frame(0)

            time.sleep(2)
            self.input_category(catName+ts)

            time.sleep(2)
            self.input_catDescription(catDesc+ts)

            time.sleep(2)
            self.click_showAll()

            time.sleep(2)
            self.check_box()

            time.sleep(2)
            self.Click_Save_Button()

            time.sleep(2)
            self.click_cancel_btn()

            time.sleep(2)
            self.driver.switch_to_default_content()

            time.sleep(2)
            self.click_subcategory()

            time.sleep(2)
            self.click_addNew2()

            time.sleep(2)
            self.driver.switch_to_default_content()

            time.sleep(5)
            self.driver.switch_to.frame(0)

            time.sleep(2)
            self.input_subcategory(subCat+ts)

            time.sleep(2)
            self.input_subcatDescription(subCatDesc+ts)

            time.sleep(2)
            self.click_showAll()

            time.sleep(2)
            self.check_box()

            time.sleep(2)
            self.Click_Save_Button()

            time.sleep(2)
            self.click_cancel_btn()

            time.sleep(2)
            self.driver.switch_to_default_content()

            time.sleep(2)
            self.click_article()

            time.sleep(2)
            self.click_addNew2()

            time.sleep(2)
            self.driver.switch_to_default_content()

            time.sleep(5)
            self.driver.switch_to.frame(0)

            time.sleep(2)
            self.input_article(article+ts)

            time.sleep(2)
            self.input_articledesc(articleDesc+ts)

            time.sleep(2)
            self.click_showAll()

            time.sleep(2)
            self.check_box()

            time.sleep(2)
            self.Click_Save_Button()

            time.sleep(2)
            self.click_cancel_btn()

