from selenium.webdriver.common.by import By


class EnterAccountInformationLocators:

    Title_Mr=(By.ID,"id_gender1")
    Password_field=(By.NAME,"password")
    Day=(By.ID,"days")
    Month=(By.ID,"months")
    Year=(By.ID,"years")
    News_letter_checkbox=(By.ID,"newsletter")
    First_name_field=(By.NAME,"first_name")
    Last_name_field=(By.NAME,"last_name")

    Company_name_field=(By.NAME,"company")
    Address_field=(By.ID,"address1")
    Country_dropdown=(By.ID,"country")
    State=(By.ID,"state")
    City=(By.ID,"city")
    Zip=(By.ID,"zipcode")
    Mobile_number=(By.ID,"mobile_number")
    Create_Account_button=(By.XPATH,"//button[text()='Create Account']")