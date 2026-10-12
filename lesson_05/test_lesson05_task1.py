from selenium import webdriver
from selenium.webdriver.common.by import By

def test_navigation():
    driver = webdriver.Chrome()
    
    # Открываем главную страницу 
    driver.get("https://httpbin.qa-territory.online")
    initial_url = driver.current_url
    
    # Находим и кликаем на ссылку с текстом "HTML Form"
    html_form_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_form_link.click()
    
    # Проверяем, что URL изменился на /forms/post
    current_url = driver.current_url
    assert "/forms/post" in current_url, f"Ожидался URL с /forms/post, но получен: {current_url}"
    
    # Возвращаемся назад на главную страницу
    driver.back()
    
    # Проверяем, что вернулись на исходный URL
    back_url = driver.current_url
    assert back_url == initial_url, f"Ожидался исходный URL: {initial_url}, но получен: {back_url}"
    
    driver.quit()
