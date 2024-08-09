from selenium.webdriver import ActionChains, Keys


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
