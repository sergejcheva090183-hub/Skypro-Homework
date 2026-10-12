from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()

    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
    start_button = driver.find_element(By.CSS_SELECTOR, "#start button")
    start_button.click()

    hello_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "finish"))
    )

    driver.save_screenshot("screenshot_lesson06_task1.png")
    assert hello_element.text == "Hello World!", (
        f"Текст не совпадает. Получено: {hello_element.text}"
    )
    driver.quit()
