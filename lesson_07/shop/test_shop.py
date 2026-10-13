import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="function")
def driver():
    # Инициализация FireFox
    _driver = webdriver.Firefox()
    _driver.maximize_window()
    yield _driver
    # 10. Закрываем браузер
    _driver.quit() 

def test_shop_flow(driver):
    # 1. Открыть сайт
    login_page = LoginPage(driver)
    login_page.open()

    # 2. Авторизоваться
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавить товары
    main_page = MainPage(driver)
    main_page.add_backpack()
    main_page.add_bolt_shirt()
    main_page.add_onesie()

    # 4. Перейти в корзину
    main_page.open_cart()

    # 5. Нажать Checkout
    cart_page = CartPage(driver)
    cart_page.click_checkout()

    # 6. Заполнить форму
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_form("Elena", "Temnikova", "160210")

    # 8. Прочитать итоговую стоимость
    total_text = checkout_page.get_total_price()
    print(f"Получена итоговая стоимость: {total_text}")

    # 9. Проверить сумму
    expected_total = "Total: $58.29"
    assert total_text == expected_total, f"Ошибка! Итоговая сумма не совпадает. Ожидалось: {expected_total}, Получено: {total_text}"
    print("Проверка пройдена: итоговая сумма = $58.29") 
