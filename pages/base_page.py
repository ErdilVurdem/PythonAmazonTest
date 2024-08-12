from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def find(self, *locator):
        return self.driver.find_element(*locator)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def get_current_url(self):
        return self.driver.current_url

    def get_text(self, locator):
        element = self.find(*locator)
        return element.text

    def send_keys(self, locator, text):
        element = self.find(*locator)
        element.send_keys(text)

    def send_keys_with_enter(self, locator, text):
        element = self.find(*locator)
        element.send_keys(text + Keys.RETURN)

    def find_and_click(self, locator_type, locator_value, timeout, backup_locator_type, backup_locater_value):
        try:
            element = WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((locator_type, locator_value))
            )
            element.click()
            return True
        except Exception as e:
            try:
                element = WebDriverWait(self.driver, timeout).until(
                    EC.presence_of_element_located((backup_locator_type, backup_locater_value))
                )  # ürününe tıklanamadıysa yedek locate ile ürüne tıklanır
                element.click()
                element = WebDriverWait(self.driver, timeout).until(
                    EC.element_to_be_clickable((locator_type, locator_value))
                )
                element.click()
            except NoSuchElementException:
                print("Yedek locate de bulunamadı")

    def find_and_click_with_backup(self, locator_type, locator_value, wait_time, backup_locator_type,
                                   backup_locator_value):
        try:
            element = WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((locator_type, locator_value))
            )
            element.click()
        except NoSuchElementException:
            try:
                element = WebDriverWait(self.driver, wait_time).until(
                    EC.presence_of_element_located((backup_locator_type, backup_locator_value))
                )
                element.click()
            except NoSuchElementException:
                print("Yedek locate de bulunamadı")
