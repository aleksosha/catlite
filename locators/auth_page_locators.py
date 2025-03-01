from selenium.webdriver.common.by import By

class AuthPageLocators:
    EMAIL_INPUT = (By.XPATH, '//input[@type="text" and @placeholder="Введите email"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@type="password" and @placeholder="Введите пароль"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit" and contains(@class, "primary")]')

