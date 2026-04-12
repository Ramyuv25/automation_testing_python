from selenium.webdriver.common.action_chains import ActionChains

from pages.New_user_signup_page import New_user_page
from pages.Enter_Account_information_page import Enter_account_page
from utils.excel_reader import Excel_reader
def test_account_created(browser):
    excel_r=Excel_reader(r"C:\Users\tiwari.ram\PycharmProjects\Automation_exercise\test_data\Ram_address.xlsx")
    browser.get("https://automationexercise.com/login")
    all_data=excel_r.get_all_rows()
    page=New_user_page(browser)
    page2=Enter_account_page(browser)

    for row in all_data:

        page.signup(row['Name'],row['email'])
        page2.check_the_mr_radio_button()
        page2.enter_pasword(row['passoword'])
        page2.enter_firstname(row['firstname'])
        page2.enter_lastname(row['lastname'])
        page2.enter_D_O_B(row['day'],row['month'],row['year'])
        page2.click_on_newsletter_check_box()
        page2.enter_address(row['address'])
        page2.select_country(row['country'])
        page2.enter_zipcode(row['zipcode'])
        page2.enter_your_city(row['city'])
        page2.enter_your_mob_no(row['mobileno'])
        page2.enter_state(row['state'])

        # act=ActionChains(browser)
        # act.scroll_by_amount(0,500)
        page2.click_on_create_button()