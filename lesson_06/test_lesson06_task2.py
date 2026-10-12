import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 15)

    user1_cookies = [{
        'name': 'SESSION',
        'value': 'WVlNzUxM2ItYWI3Ny00MTk1LWE3M2MtMTZhZGM1OWE5ODE4',
        'domain': '.gitflic.ru'
    }]

    user2_cookies = [{
        'name': 'SESSION',
        'value': 'Yjc2M2RiNTAtY2U0MC00NzhlLTk4ZTQtOTc1ZDEzOGE0OGIw',
        'domain': '.gitflic.ru'
    }]

    # 1. Откройте страницу https://gitflic.ru
    driver.get("https://gitflic.ru/")

    # 2. Установите cookie пользователя 1
    for cookie in user1_cookies:
        driver.add_cookie(cookie)

    # 3. Обновите страницу
    driver.refresh()
    time.sleep(2)

    # 4. Перейдите на страницу пользователя 1
    driver.get("https://gitflic.ru/user/shelena2010")

    # 5. Сохраните текущий URL
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    user1_url = driver.current_url
    print(f"https://gitflic.ru/user/shelena2010: {user1_url}")

    # 6. Разлогиньтесь (очистите куки)
    driver.delete_all_cookies()

    # 7. Установите cookie пользователя 2
    for cookie in user2_cookies:
        driver.add_cookie(cookie)

    # 8. Обновите страницу
    driver.refresh()
    time.sleep(2)

    # 9. Перейдите на страницу пользователя 2
    driver.get("https://gitflic.ru/user/shelena2012")

    # 10. Сохраните текущий URL
    wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
    user2_url = driver.current_url
    print(f"https://gitflic.ru/user/shelena2012 : {user2_url}")

    # 11. Проверьте, что URL для пользователя 1 и пользователя 2 различаются
    assert user1_url != user2_url, (
        f"Ошибка: URL совпали. User1: {user1_url}, User2: {user2_url}"
    )
    print("Проверка пройдена: URL пользователей различаются.")
    driver.quit()
