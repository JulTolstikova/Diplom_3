from selenium.webdriver.common.by import By


class LoginPageLocators:
    NEW_PASSWORD = (By.XPATH, ".//a[text() = 'Восстановить пароль']")
    NEW_PASSWORD_TITLE = (By.XPATH, './/h2[text()="Восстановление пароля"]')
    EMAIL_AUTH_INPUT = (By.XPATH, ".//input[@class = 'text input__textfield text_type_main-default' and  @name = 'name']")
    PASSWORD_AUTH_INPUT = (By.XPATH, ".//input[@name = 'Пароль']")
    AUTH_BTN = (By.XPATH, ".//button[text() = 'Войти']")
    CREATE_BURGER_TITLE = (By.XPATH, ".//h1[text() = 'Соберите бургер']")
