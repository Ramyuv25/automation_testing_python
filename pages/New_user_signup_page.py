from pages.Base_page import BasePage
from locators.New_user_locators import New_user_locators


class New_user_page(BasePage):
    def __init__(self, driver):
        self.driver = driver

        super().__init__(driver)
        self.locator =New_user_locators()


    def signup(self,first_name,email):
        self.clear(self.locator.Name_field)
        self.send_keys(self.locator.Name_field, first_name)
        self.send_keys(self.locator.Email_field, email)
        self.click(self.locator.Singup_button)