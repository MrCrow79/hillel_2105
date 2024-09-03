from selenium.webdriver.common.by import By


class LoginPageElements():
    USER_NAME_INPUT = (By.XPATH, "//*[@data-test='username']")

    USER_PASSWORD_INPUT = (By.XPATH, "//*[@data-test='password']")
    LOGIN_BUTTON = (By.ID, "login-button")