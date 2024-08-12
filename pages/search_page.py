from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class SearchPage(BasePage):
    FIRST_ELEMENT = (By.XPATH, "(//*[@class='a-size-mini a-spacing-none a-color-base s-line-clamp-4'])[1]")
    SECOND_PAGE = (By.CSS_SELECTOR, ".s-pagination-item.s-pagination-button:first-of-type")
    backupProdToClickLocValue = "(//*[@class='a-size-base-plus a-color-base a-text-normal'])[21]"
    productToClickLocatorValue = "[data-index='26']"

    def return_text_first_element(self):
        return self.get_text(self.FIRST_ELEMENT)

    def click_second_page_button(self):
        self.click_element(*self.SECOND_PAGE)

    def click_to_product(self):
        self.find_and_click_with_backup(By.CSS_SELECTOR, self.productToClickLocatorValue, 10, By.XPATH,
                                        self.backupProdToClickLocValue)
