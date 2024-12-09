from pages.forgot_password_page import ForgotPasswordPage
import allure
import data
from pages.login_page import LoginPage


class TestForgotPasswordPage:

    @allure.title("Проверка перехода на страницу Восстановление пароля")
    def test_click_on_new_password(self, driver):
        login_page = LoginPage(driver)
        login_page.go_to_login_page()
        login_page.click_on_new_password_btn()
        password_url = login_page.get_url_for_page_for_test
        assert data.FORGOT_PASSWORD_URL in password_url
    @allure.title("Проверка перехода на страницу восстановления пароля")
    def test_send_email_for_recover(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.go_to_recover_password_page()
        forgot_password_page.input_email()
        forgot_password_page.click_on_recover_button()
        forgot_password_page.wait_for_input_code()
        reset_url = forgot_password_page.get_url_for_page_for_test
        assert data.RESET_PASSWORD_URL in reset_url

    @allure.title("Проверка отображения поля с открытым глазом ")
    def test_password_show(self, driver):
        forgot_password_page = ForgotPasswordPage(driver)
        forgot_password_page.go_to_recover_password_page()
        forgot_password_page.input_email()
        forgot_password_page.click_on_recover_button()
        forgot_password_page.wait_for_input_code()
        forgot_password_page.input_new_password()
        forgot_password_page.click_on_eye()
        assert forgot_password_page.find_closed_eye()
