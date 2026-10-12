import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(browser):
    url = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
    browser.get(url)

    wait = WebDriverWait(browser, 60)

    # 2. В поле ввода #delay введите значение 45
    delay_input = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#delay"))
    )
    delay_input.clear()
    delay_input.send_keys("45")

    # 3. Нажмите на кнопки: 7 + 8 =
    buttons = ["7", "+", "8", "="]
    for button in buttons:
        btn = wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//span[text()='{button}']"))
        )
        btn.click()

    # 4. Проверьте (assert), что в окне отобразится результат 15 через 45 секунд.
    result = WebDriverWait(browser, 45).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )

    assert result
