from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

driver = Chrome()
driver.get("http://localhost:8000/first.html")

# Знаходження елемента за ID
user_field = driver.find_element(By.ID, "username")
user_field = driver.find_element(By.XPATH, "//input[@id='username']")
pass_field = driver.find_element(By.ID, "password")
login_button = driver.find_element(By.ID, "login_button")


# Знаходження всіх елементів з тегом <li>
li_elements = driver.find_elements(By.TAG_NAME, "li")

texts_of_elements = set()

# Пошук конкретного елемента серед отриманих
for li in li_elements:

    assert li.text not in texts_of_elements, f'text {li.text} is duplicated.\nelement_id={li.get_attribute("id")}'
    texts_of_elements.add(li.text)

    # # пошук може бути повiльним якщо елементiв багато
    # if li.text == "Елемент списку 2":
    #     # Знайдено потрібний елемент
    #     print("Знайдено елемент:", li.text)
    #     break

driver.quit()