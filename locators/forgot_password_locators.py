from selenium.webdriver.common.by import By


class ForgotPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH,".//input[@class = 'text input__textfield text_type_main-default']")
    RECOVER_BTN = (By.XPATH, './/button[text() = "Восстановить"]')
    INPUT_CODE = (By.XPATH,'.//label[text() = "Введите код из письма"]')
    INPUT_PASSWORD = (By.XPATH, './/input[@type = "password"]')
    EYE_OPEN = (By.XPATH, './/div[@class = "input__icon input__icon-action"]')
    EYE_CLOSED = (By.XPATH, ".//div[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")