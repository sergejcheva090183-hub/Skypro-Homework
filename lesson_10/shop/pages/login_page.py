from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class LoginPage:
    """
    PageObject для страницы авторизации SauceDemo.
    Представляет страницу авторизации и предоставляет
    методы для работы с её элементами.
    """

    URL = "https://www.saucedemo.com/"

    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    @allure.step("Инициализация страницы авторизации")
    def __init__(self, driver: WebDriver):
        """
        Инициализация страницы авторизации.
        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу авторизации")
    def open(self):
        """
        Открывает страницу авторизации в текущем окне браузера.
        Метод вызывает базовый метод WebDriver.get().
        :return: None
        :rtype: None
        """
        self.driver.get(self.URL)

    @allure.step("Авторизация пользователя: логин='{username}'")
    def login(self, username: str, password: str):
        """
        Выполняет процедуру авторизации:
        вводит учетные данные и нажимает кнопку входа.
        :param username: Логин пользователя (стандартно: "standard_user").
        :param password: Пароль пользователя (стандартно: "secret_sauce").
        :return: None
        """
        with allure.step("Ввести логин"):
            self.wait.until(
                EC.visibility_of_element_located(self.USERNAME_INPUT)
            ).send_keys(username)

        with allure.step("Ввести пароль"):
            self.wait.until(
                EC.visibility_of_element_located(self.PASSWORD_INPUT)
            ).send_keys(password)

        with allure.step("Нажать кнопку входа"):
            self.wait.until(
                EC.element_to_be_clickable(self.LOGIN_BUTTON)
            ).click()
