from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self,locator):
        self.wait.until(ec.presence_of_element_located(locator)).click()

    def send_keys(self, locator, text):
        self.wait.until(ec.presence_of_element_located(locator)).send_keys(text)

    def text(self,locator):
        return self.wait.until(ec.presence_of_element_located(locator)).text

    def clear(self,locator):
        self.wait.until(ec.presence_of_element_located(locator)).clear()