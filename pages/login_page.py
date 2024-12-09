import allure
import data
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке восстановления пароля")
    def click_on_new_password_btn(self):
        self.click_on_element(LoginPageLocators.NEW_PASSWORD)

    @allure.step("Переход на страницу авторизации")
    def go_to_login_page(self):
        self.driver.get(data.MAIN_URL + data.LOGIN_URL)

    @allure.step("Авторизация на сайте")
    def auth(self):
        self.driver.get(data.MAIN_URL + data.LOGIN_URL)
        self.set_text_to_element(LoginPageLocators.EMAIL_AUTH_INPUT, data.TEST_EMAIL)
        self.set_text_to_element(LoginPageLocators.PASSWORD_AUTH_INPUT, data.TEST_PASSWORD)
        self.click_on_element(LoginPageLocators.AUTH_BTN)
        self.find_element_with_wait(LoginPageLocators.CREATE_BURGER_TITLE)

    @allure.step("Ожидание появления кнопки Войти")
    def wait_for_auth_btn(self):
        self.find_element_with_wait(LoginPageLocators.AUTH_BTN)