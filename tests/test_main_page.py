from pages.main_page import MainPage
import allure
import data


class TestMainPage:

    @allure.title("Проверка перехода в Конструктор")
    def test_click_on_constructor_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_constructor_btn()
        new_url = main_page.get_url_for_page_for_test
        assert new_url == data.MAIN_URL

    @allure.title("Проверка перехода в Лента заказов")
    def test_click_on_orders_list_button(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_orders_list_btn()
        new_url = main_page.get_url_for_page_for_test
        assert data.ORDER_URL in new_url

    @allure.title("Проверка модального окна с информацией об ингредиенте")
    def test_click_on_ingredient_and_get_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        assert main_page.wait_for_ingredient_modal()

    @allure.title("Проверка закрытия модального окна ")
    def test_click_on_ingredient_window_exit(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_ingredient()
        main_page.click_on_close_ingredient_modal()
        assert main_page.check_modal_closed() is False

    @allure.title("Проверка увеличения количества ингредиентов при добавлении ингредиента в заказ")
    def test_ingredient_count(self, driver):
        main_page = MainPage(driver)
        main_page.drag_and_drop_ingredient()
        assert main_page.get_ingredient_counter() == '2'
