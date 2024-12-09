import data
from pages.base_page import BasePage
from pages.account_page import AccountPage
import allure

from pages.login_page import LoginPage

class TestAccountPage:

    @allure.title("Проверка перехода в Личный кабинет")
    def test_click_on_personal_account(self, driver):
        account_page = AccountPage(driver)
        account_page.click_on_personal_account_btn()
        new_url = account_page.get_url_for_page_for_test
        assert data.LOGIN_URL in new_url

    @allure.title("Проверка  перехода к Истории заказов")
    def test_click_on_order_history(self, driver):
        login_page = LoginPage(driver)
        login_page.auth()
        account_page = AccountPage(driver)
        account_page.click_on_personal_account_btn()
        account_page.go_to_orders_history()
        new_url = account_page.get_url_for_page_for_test
        assert data.ORDER_HISTORY_URL in new_url

    @allure.title("Проверка выхода из аккаунта")
    def test_click_on_exit(self, driver):
        login_page = LoginPage(driver)
        login_page.auth()
        account_page = AccountPage(driver)
        account_page.click_on_personal_account_btn()
        account_page.click_on_exit_btn()
        login_page.wait_for_auth_btn()
        new_url = account_page.get_url_for_page_for_test
        assert data.LOGIN_URL in new_url

    @allure.title("Проверка создания заказа")
    def test_create_order_for_login_user(self, driver):
        login_page = LoginPage(driver)
        login_page.auth()
        account_page = AccountPage(driver)
        account_page.create_order()
        assert account_page.wait_for_order_info()
