from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.ID, "titleSection")
    ADD_TO_CART_BUTTON = (By.ID, "add-to-cart-button")

    def is_product_present(self):
        try:
            return self.find(*self.PRODUCT_NAME)
        except NoSuchElementException as e:
            print(f"Ürün bulunamadı: {e}")
            return False

    def click_add_to_cart_button(self):
        self.click_element(*self.ADD_TO_CART_BUTTON)
