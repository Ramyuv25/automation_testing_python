from pages.Base_page import BasePage
from locators.Enter_account_information_locators import EnterAccountInformationLocators
class Enter_account_page(BasePage):
    def __init__(self, driver):
        self.driver = driver
        super().__init__(driver)

        self.locators = EnterAccountInformationLocators()

    def check_the_mr_radio_button(self):
        self.click(self.locators.Title_Mr)

    def enter_pasword(self, pasw):
     self.send_keys(self.locators.Password_field,pasw)

    def enter_D_O_B(self,day,month,year):
        self.send_keys(self.locators.Day,day)
        self.send_keys(self.locators.Month,month)
        self.send_keys(self.locators.Year,year)

    def click_on_newsletter_check_box(self):
        self.click(self.locators.News_letter_checkbox)

    def enter_firstname(self,firstname):
        self.send_keys(self.locators.First_name_field,firstname)

    def enter_lastname(self,lastname):
        self.send_keys(self.locators.Last_name_field, lastname)

    def enter_address(self, address):
        self.send_keys(self.locators.Address_field, address)

    def select_country(self,country):
        self.send_keys(self.locators.Country_dropdown,country)
    def enter_state(self,state):
        self.send_keys(self.locators.State, state)

    def enter_your_city(self,city):
        self.send_keys(self.locators.City, city)
    def enter_zipcode(self,zipcode):
        self.send_keys(self.locators.Zip, zipcode)

    def enter_your_mob_no(self,mob_no):
        self.send_keys(self.locators.Mobile_number, mob_no)

    def click_on_create_button(self):
        self.click(self.locators.Create_Account_button)