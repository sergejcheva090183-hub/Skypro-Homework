from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class CheckoutPage:
    """
    PageObject для страницы оформления заказа (Checkout).
    Содержит локаторы элементов и методы для взаимодействия с формой.
    """

    # Локаторы
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Инициализация страницы оформления заказа")
    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Исправлено: длинная строка перенесена с использованием скобок (PEP 8)
    @allure.step(
        "Заполнение формы оформления заказа: "
        "имя='{first_name}', фамилия='{last_name}', индекс='{postal_code}'"
    )
    def fill_form(self, first_name: str, last_name: str, postal_code: str):
        """
        Заполняет форму оформления заказа данными пользователя
         и переходит к следующему шагу.
        :param first_name: Имя (строка).
        :param last_name: Фамилия (строка).
        :param postal_code: Почтовый индекс (строка).
        """
        with allure.step("Ввести имя"):
            self.wait.until(
                EC.visibility_of_element_located(self.FIRST_NAME_INPUT)
            ).send_keys(first_name)

        with allure.step("Ввести фамилию"):
            self.wait.until(
                EC.visibility_of_element_located(self.LAST_NAME_INPUT)
            ).send_keys(last_name)

        with allure.step("Ввести почтовый индекс"):
            self.wait.until(
                EC.visibility_of_element_located(self.POSTAL_CODE_INPUT)
            ).send_keys(postal_code)

        with allure.step("Нажать кнопку 'Continue'"):
            self.wait.until(
                EC.element_to_be_clickable(self.CONTINUE_BUTTON)
            ).click()

    @allure.step("Получение итоговой стоимости заказа")
    def get_total_price(self) -> str:
        """
        Возвращает текст итоговой стоимости заказа.

        :return: Строка с итоговой суммой (например, "Total: $32.39").
        :rtype: str
        """
        return self.wait.until(
            EC.visibility_of_element_located(self.TOTAL_LABEL)
        ).text
