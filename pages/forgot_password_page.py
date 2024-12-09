from pages.base_page import BasePage
import data
from locators.forgot_password_locators import ForgotPasswordPageLocators
import allure


class ForgotPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход на страницу восстановления пароля")
    def go_to_recover_password_page(self):
        self.driver.get(data.MAIN_URL + data.FORGOT_PASSWORD_URL)

    @allure.step("Ввод почты на странице восстановления пароля")
    def input_email(self):
        self.set_text_to_element(ForgotPasswordPageLocators.EMAIL_INPUT, data.TEST_EMAIL)

    @allure.step("Ввод пароля в поле восстановления пароля")
    def input_new_password(self):
        self.set_text_to_element(ForgotPasswordPageLocators.INPUT_PASSWORD, data.TEST_NEW_PASSWORD)

    @allure.step("Нажать на кнопку Восстановить")
    def click_on_recover_button(self):
        self.click_on_element(ForgotPasswordPageLocators.RECOVER_BTN)

    @allure.step("Ожидание поля Введите код из письма")
    def wait_for_input_code(self):
        self.find_element_with_wait(ForgotPasswordPageLocators.INPUT_CODE)

    @allure.step("Клик по кнопке глаза")
    def click_on_eye(self):
        self.click_on_element(ForgotPasswordPageLocators.EYE_OPEN)

    @allure.step("Поиск неактивного глаза")
    def find_closed_eye(self):
        return self.find_element_with_wait(ForgotPasswordPageLocators.EYE_CLOSED)
