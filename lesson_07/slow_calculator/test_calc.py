import pytest
from selenium import webdriver
from calc_page import CalculatorPage

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window() 
    yield driver
    driver.quit()

def test_calc(browser):
    page = CalculatorPage(browser)
    page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    page.set_delay(45) 

    for button in ["7", "+", "8", "="]:
        page.click_button(button)

    result = page.get_result("15")
    assert result is True 
