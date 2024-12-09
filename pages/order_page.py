from pages.base_page import BasePage
import data
from locators.order_page_locators import OrderPageLocators
from locators.account_page_locators import AccountPageLocators
import allure


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по заказу")
    def click_on_order(self):
        self.click_on_element(OrderPageLocators.FIRST_ORDER)

    @allure.step("Поиск модалки с информацией о заказе")
    def find_order_info_modal(self):
        return self.find_element_with_wait(OrderPageLocators.ORDER_INFO_MODAL)

    @allure.step("Переход на страницу с заказами")
    def go_to_order_page(self):
        self.driver.get(data.MAIN_URL + data.ORDER_URL)

    @allure.step("Поиск информации о заказе")
    def wait_for_order_info(self):
        return self.find_element_with_wait(AccountPageLocators.ORDER_INFO)

    @allure.step("Создание заказа")
    def create_order(self):
        self.driver.get(data.MAIN_URL)
        self.drag_and_drop_element(OrderPageLocators.INGREDIENT_BUN_FIRST, OrderPageLocators.INGREDIENT_CONTAINER)
        self.click_on_element(OrderPageLocators.ORDER_BTN)
        self.wait_for_order_info()
        self.wait_until_missing_element(OrderPageLocators.STANDART_ORDER_ID)

    @allure.step("Закрыть окно заказа")
    def close_order_modal(self):
        self.find_element_with_wait(OrderPageLocators.EXIT_ORDER_MODAL_BTN)
        self.wait_until_clickable(OrderPageLocators.EXIT_ORDER_MODAL_BTN)
        self.click_on_element(OrderPageLocators.EXIT_ORDER_MODAL_BTN)

    @allure.step("Найти номер заказа в истории")
    def search_order_number(self):
        self.wait_until_clickable(AccountPageLocators.PERSONAL_ACCOUNT_BTN)
        self.click_on_element(AccountPageLocators.PERSONAL_ACCOUNT_BTN)
        self.find_element_with_wait(AccountPageLocators.PROFILE)
        self.click_on_element(AccountPageLocators.ORDERS_HISTORY)
        self.find_element_with_wait(OrderPageLocators.FIRST_ORDER)
        self.scroll_to_element(OrderPageLocators.NUMBER_OF_LAST_ORDER_IN_HISTORY)
        return self.get_text_from_element(OrderPageLocators.NUMBER_OF_LAST_ORDER_IN_HISTORY)

    @allure.step("Получение id заказа")
    def return_order_id(self):
        self.wait_until_missing_element(OrderPageLocators.STANDART_ORDER_ID)
        return self.get_text_from_element(OrderPageLocators.ORDER_NUMBER_FROM_INFO_MODAL)

    @allure.step("Получение номера из последнего заказа в листе заказов")
    def number_of_last_order_in_order_list_from_history(self):
        self.go_to_order_page()
        return self.get_text_from_element(OrderPageLocators.NUMBER_OF_FIRST_ORDER_IN_ORDER_LIST)

    @allure.step("Получение номера заказа в модальном окне")
    def number_of_last_order(self):
        return self.get_text_from_element(OrderPageLocators.ORDER_NUMBER_FROM_INFO_MODAL)

    @allure.step("Получение количества всех выполненных заказов")
    def return_orders_count(self):
        return self.get_text_from_element(OrderPageLocators.ALL_COUNT_ORDERS)

    @allure.step("Получение количества всех заказов за день")
    def return_day_orders_count(self):
        return self.get_text_from_element(OrderPageLocators.DAY_COUNT_ORDERS)

    @allure.step("Получение заказа в работе")
    def return_now_order(self):
        self.find_element_with_wait(OrderPageLocators.NOW_ORDER)
        return self.get_text_from_element(OrderPageLocators.NOW_ORDER)
