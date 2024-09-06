# from selenium import webdriver
# from selenium.webdriver.common.alert import Alert
# from selenium.webdriver.common.by import By
# import time
#
# # Ініціалізація драйвера
# driver = webdriver.Chrome()
# driver.get("http://localhost:8000/dialogs.html")
#
# # Показати Alert і отримати текст з нього
# show_alert = driver.find_element(By.XPATH, "//button[text()='Показати Alert']")
# show_alert.click()
# alert = Alert(driver)
# print("Текст Alert:", alert.text)
# alert.accept()
#
# # Показати Confirm і підтвердити його
# driver.find_element(By.XPATH, "//button[text()='Показати Confirm']").click()
# alert = Alert(driver)
# print("Текст Confirm:", alert.text)
# alert.accept()
#
# # Показати Prompt, ввести текст і підтвердити його
# driver.find_element(By.XPATH, "//button[text()='Показати Prompt']").click()
# alert = Alert(driver)
# print("Текст Prompt:", alert.text)
# alert.send_keys("John123")
# alert.accept()
#
# # Зачекати 2 секунди перед завершенням
# time.sleep(2)
#
# # Закрити браузер
# driver.quit()