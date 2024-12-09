from time import sleep

from pages.login_page import LoginPage
from pages.order_page import OrderPage
import allure


class TestOrderPage:

    @allure.title("Проверка отображения модального окна при клике на заказ в ленте")
    def test_open_window_with_information_about_order(self, driver):
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        order_page.click_on_order()
        assert order_page.find_order_info_modal()

    @allure.title("Проверка отображения номера заказа в листе заказов")
    def test_put_user_order_to_order_list(self, driver):
        login_page = LoginPage(driver)
        login_page.auth()
        order_page = OrderPage(driver)
        order_page.create_order()
        sleep(5)
        order_page.close_order_modal()
        number_of_user_order = order_page.search_order_number()
        number_in_number_list = order_page.number_of_last_order_in_order_list_from_history()
        assert number_of_user_order == number_in_number_list

    @allure.title("Проверка счетчика всех заказов")
    def test_count_of_all_orders(self, driver):
        login_page = LoginPage(driver)
        login_page.auth()
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        before_order = order_page.return_orders_count()
        order_page.create_order()
        order_page.number_of_last_order()
        order_page.go_to_order_page()
        after_order = order_page.return_orders_count()
        assert int(after_order) > int(before_order)

    @allure.title("Проверка счетчика заказов за день")
    def test_count_of_day_orders(self, driver):
        login_page = LoginPage(driver)
        login_page.auth()
        order_page = OrderPage(driver)
        order_page.go_to_order_page()
        before_order = order_page.return_day_orders_count()
        order_page.create_order()
        order_page.go_to_order_page()
        after_order = order_page.return_day_orders_count()
        assert int(after_order) > int(before_order)

    @allure.title("Проверка отображения заказа 'В работе' в листе заказов")
    def test_count_now_order(self, driver):
        login_page = LoginPage(driver)
        login_page.auth()
        order_page = OrderPage(driver)
        order_page.create_order()
        order_number = order_page.return_order_id()
        order_page.go_to_order_page()
        order_number_in_order_list = order_page.return_now_order()
        assert order_number in order_number_in_order_list
