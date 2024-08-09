from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HomePage(BasePage):
    SEARCH_BOX = (By.ID, "twotabsearchtextbox")
    REJECT_COOKIES = (By.CSS_SELECTOR, ".a-button-text.a-text-center.celwidget")
    textToSearch = "Samsung"

    def access_home_page(self):
        while True:
            try:
                self.find_search_box()
                break
            except:
                print("Ana sayfaya erişim sağlanamadı, sayfa yenileniyor")
                self.driver.refresh()

    def reject_cookies(self):
        self.click_element(*self.REJECT_COOKIES)

    def find_search_box(self):
        return self.find(*self.SEARCH_BOX)

    def search_text(self):
        self.send_keys_with_enter(self.SEARCH_BOX, self.textToSearch)
