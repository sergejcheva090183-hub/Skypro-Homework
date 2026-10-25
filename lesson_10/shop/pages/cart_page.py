from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
import allure


class CartPage:
    """
    PageObject класс для страницы корзины.
    """
    CHECKOUT_BUTTON: tuple[By, str] = (By.ID, "checkout")

    @allure.step("Инициализация страницы корзины")
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы корзины.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    @allure.step("Переход к оформлению заказа")
    def click_checkout(self) -> None:
        """
        Нажимает кнопку перехода к оформлению заказа (Checkout).
        Ожидает, пока кнопка станет кликабельной.
        :return: None
        """
        element: WebElement = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )
        element.click()
