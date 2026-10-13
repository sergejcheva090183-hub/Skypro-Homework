from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 

class CalculatorPage:

    DELAY_INPUT = (By.CSS_SELECTOR, "#delay")
    SCREEN = (By.CSS_SELECTOR, ".screen")
    BUTTON_TEMPLATE = "//span[text()='{}']"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

    def open(self, url):
        self.driver.get(url)

    def set_delay(self, seconds: int):
        delay_input = self.wait.until(
            EC.element_to_be_clickable(self.DELAY_INPUT)
        )
        delay_input.clear()
        delay_input.send_keys(str(seconds))

    def click_button(self, button_text: str):
        button_locator = (By.XPATH, self.BUTTON_TEMPLATE.format(button_text))
        btn = self.wait.until(EC.element_to_be_clickable(button_locator)) 
        btn.click()

    def get_result(self, expected_text: str, timeout: int = 45):

        return self.wait.until(
            EC.text_to_be_present_in_element(self.SCREEN, expected_text)
        ) 
    
