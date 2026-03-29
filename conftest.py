from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture(scope="module")
def browser():
    options = Options()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
