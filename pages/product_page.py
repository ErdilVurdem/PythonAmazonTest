from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_NAME = (By.ID, "titleSection")
    addToCartButtonLocaterValue = "#add-to-cart-button"
    backupProdToClickLocValue = "(//*[@class='a-size-base-plus a-color-base a-text-normal'])[21]"

    def is_product_present(self):
        try:
            return self.find(*self.PRODUCT_NAME)
        except NoSuchElementException as e:
            print(f"Ürün bulunamadı: {e}")
            return False

    def click_add_to_cart_button(self):
        self.find_and_click(By.CSS_SELECTOR, self.addToCartButtonLocaterValue, 10, By.XPATH,
                            self.backupProdToClickLocValue)
