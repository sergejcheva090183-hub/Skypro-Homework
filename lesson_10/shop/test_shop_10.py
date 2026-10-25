import pytest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
import allure


@pytest.fixture(scope="function")
def driver():
    """
    Фикстура для создания и управления экземпляром браузера Firefox.
    """
    with allure.step("Инициализация драйвера Firefox"):
        _driver = webdriver.Firefox()
        _driver.maximize_window()

    yield _driver

    with allure.step("Завершение сессии и закрытие браузера"):
        _driver.quit()


@allure.title("Успешное прохождение полного цикла покупки")
@allure.description(
    """
    Тест проверяет полный пользовательский сценарий
     в интернет-магазине Sauce Demo:
    1. Открытие сайта и переход на страницу авторизации.
    2. Успешный вход в систему под стандартным пользователем.
    3. Добавление трех различных товаров
     (Backpack, Bolt T-Shirt, Onesie) в корзину.
    4. Переход в корзину и проверка возможности оформления.
    5. Заполнение формы доставки валидными данными.
    6. Верификация итоговой стоимости заказа на странице подтверждения.
    """
)
@allure.feature("E2E: Покупки в Sauce Demo")
@allure.severity(allure.severity_level.CRITICAL)
def test_shop_flow(driver: WebDriver):
    """
    Тестовый сценарий полного потока покупок
     в интернет-магазине (Sauce Labs Demo App).
    """
    # 1. Открыть сайт и перейти на страницу авторизации
    with allure.step("Открыть главную страницу и перейти к авторизации"):
        login_page = LoginPage(driver)
        login_page.open()

    # 2. Авторизоваться под тестовым пользователем
    with allure.step("Авторизация под пользователем"):
        login_page.login("standard_user", "secret_sauce")

    # 3. Добавить товары в корзину с главной страницы
    main_page = MainPage(driver)
    with allure.step("Добавить товары в корзину"):
        main_page.add_backpack()
        main_page.add_bolt_shirt()
        main_page.add_onesie()

    # 4. Перейти в корзину для проверки выбранных товаров
    with allure.step("Перейти в корзину"):
        main_page.open_cart()

    # 5. Нажать кнопку Checkout на странице корзины
    cart_page = CartPage(driver)
    with allure.step("Перейти к оформлению заказа"):
        cart_page.click_checkout()

    # 6. Заполнить форму оформления заказа
    checkout_page = CheckoutPage(driver)
    with allure.step("Заполнить форму оформления заказа"):
        checkout_page.fill_form("Elena", "Temnikova", "160210")

    # 7. Прочитать  итоговую стоимость заказа
    with allure.step("Получить итоговую стоимость заказа"):
        total_text = checkout_page.get_total_price()
        allure.attach(
            total_text,
            name="Итоговая стоимость",
            attachment_type=allure.attachment_type.TEXT
        )

    # 8. Проверить соответствие итоговой суммы ожидаемому значению
    with allure.step("Проверить соответствие итоговой суммы"):
        expected_total = "Total: $58.29"
        assert total_text == expected_total, (
            f"Ошибка! Итоговая сумма не совпадает. "
            f"Ожидалось: {expected_total}, Получено: {total_text}"
        )
