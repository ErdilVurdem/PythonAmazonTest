from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    FIRST_ELEMENT = (By.XPATH, "//div[1]/div[1]/div/span[1]/div[1]/div[3]//div[2]/div[2]")
    SECOND_PAGE = (By.CSS_SELECTOR, ".s-pagination-item.s-pagination-button:first-of-type")
    PRODUCT_TO_CLICK = (By.CSS_SELECTOR, "[data-index='26']")

    def return_text_first_element(self):
        return self.get_text(self.FIRST_ELEMENT)

    def click_second_page_button(self):
        self.click_element(*self.SECOND_PAGE)

    def click_to_product(self):
        self.click_element(*self.PRODUCT_TO_CLICK)
