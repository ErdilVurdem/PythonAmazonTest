from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    AMAZON_LOGO = (By.ID, "nav-logo-sprites")

    def click_amazon_logo(self):
        self.click_element(*self.AMAZON_LOGO)
