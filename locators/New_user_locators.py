from selenium.webdriver.common.by import By


class New_user_locators:
    Name_field = (By.NAME,'name')
    Email_field=(By.XPATH,"(//input[@placeholder='Email Address'])[2]")
    Singup_button= (By.XPATH,"//button[normalize-space()='Signup']")
