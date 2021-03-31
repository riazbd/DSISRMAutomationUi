from pages.base_page import BasePage
from utils.locators import WelcomePageLocators


class WelcomePage(BasePage):
    def __init__(self, driver):
        self.locator = WelcomePageLocators
        super(WelcomePage, self).__init__(driver)

    def check_page_loaded(self):
        return self.driver.current_url

    def click_companies_contacts_tab(self):
        return self.find_element(*self.locator.CompaniesAndContactsLocator).click()

    def click_ip_and_Products_tab(self):
        return self.find_element(*self.locator.IPAndProductsLocator).click()
