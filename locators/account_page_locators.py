from selenium.webdriver.common.by import By


class AccountPageLocators:
    PERSONAL_ACCOUNT_BTN = (By.XPATH, ".//p[text() = 'Личный Кабинет']")
    PROFILE = (By.XPATH, ".//a[text() = 'Профиль']")
    ORDERS_HISTORY = (By.XPATH, ".//a[text() = 'История заказов']")
    EXIT = (By.XPATH, ".//button[text() = 'Выход']")
    ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    ORDER_INFO = (By.XPATH, ".//p[text() = 'Ваш заказ начали готовить']")
