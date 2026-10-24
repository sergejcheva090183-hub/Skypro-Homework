from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class MainPage:
    """
    Page Object для главной страницы интернет-магазина (Inventory Page)
     в тестовом приложении Sauce Labs.
    Предоставляет методы для добавления товаров в корзину и перехода к корзине.
    """

    # Локаторы элементов на странице (кортежи (By, value))
    BACKPACK_BUTTON = (By.NAME, "add-to-cart-sauce-labs-backpack")
    """Локатор кнопки «Добавить в корзину» для товара Sauce Labs Backpack."""

    BOLT_SHIRT_BUTTON = [
        By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt"
    ]
    """Локатор кнопки «Добавить в корзину» для товара
     Sauce Labs Bolt T‑Shirt."""

    ONESIE_BUTTON = (By.NAME, "add-to-cart-sauce-labs-onesie")
    """Локатор кнопки «Добавить в корзину» для товара Sauce Labs Onesie."""

    CART_LINK = (By.ID, "shopping_cart_container")
    """Локатор ссылки/кнопки перехода к корзине (иконка корзины)."""

    @allure.step("Инициализация главной страницы (Main Page)")
    def __init__(self, driver: WebDriver):
        """
        Инициализирует экземпляр MainPage.

        :param driver: WebDriver — объект драйвера Selenium.
        """
        self.driver: WebDriver = driver
        self.wait: WebDriverWait = WebDriverWait(driver, 10)

    @allure.step("Добавить товар 'Sauce Labs Backpack' в корзину")
    def add_backpack(self):
        """
        Добавляет товар «Sauce Labs Backpack» в корзину.
        """
        self._click_add_to_cart(self.BACKPACK_BUTTON, "Sauce Labs Backpack")

    @allure.step("Добавить товар 'Sauce Labs Bolt T-Shirt' в корзину")
    def add_bolt_shirt(self):
        """
        Добавляет товар «Sauce Labs Bolt T‑Shirt» в корзину.
        """
        self._click_add_to_cart(
            self.BOLT_SHIRT_BUTTON, "Sauce Labs Bolt T-Shirt"
        )

    @allure.step("Добавить товар 'Sauce Labs Onesie' в корзину")
    def add_onesie(self):
        """
        Добавляет товар «Sauce Labs Onesie» в корзину.
        """
        self._click_add_to_cart(self.ONESIE_BUTTON, "Sauce Labs Onesie")

    @allure.step("Перейти в корзину")
    def open_cart(self):
        """
        Открывает страницу корзины, кликая по иконке корзины.
        """
        self.wait.until(
            EC.element_to_be_clickable(self.CART_LINK)
        ).click()

    def _click_add_to_cart(self, locator: tuple, item_name: str):
        add_button = self.wait.until(EC.element_to_be_clickable(locator))
        if add_button.get_attribute("aria-disabled") == "true":
            raise AssertionError(
                f"Кнопка '{item_name}' заблокирована (aria-disabled=true)"
            )
        add_button.click()
