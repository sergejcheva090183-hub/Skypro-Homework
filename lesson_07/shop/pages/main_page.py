from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:

    BACKPACK_BUTTON = (By.NAME, "add-to-cart-sauce-labs-backpack")
    BOLT_SHIRT_BUTTON = (By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE_BUTTON = (By.NAME, "add-to-cart-sauce-labs-onesie")
    CART_LINK = (By.ID, "shopping_cart_container") 

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        self.wait.until(
            EC.element_to_be_clickable(self.BACKPACK_BUTTON)
        ).click()

    def add_bolt_shirt(self):
        self.driver.find_element(*self.BOLT_SHIRT_BUTTON).click()

    def add_onesie(self):
        self.driver.find_element(*self.ONESIE_BUTTON).click()

    def open_cart(self):
        self.driver.find_element(*self.CART_LINK).click()
