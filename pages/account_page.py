from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from locators.account_page_locators import AccountPageLocators
import allure


class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Переход по кнопке История заказов")
    def go_to_orders_history(self):
        self.find_elements(AccountPageLocators.PROFILE)
        self.click_on_element(AccountPageLocators.ORDERS_HISTORY)

    @allure.step("Клик по кнопке 'Личный кабинет'")
    def click_on_personal_account_btn(self):
        self.click_on_element(AccountPageLocators.PERSONAL_ACCOUNT_BTN)

    @allure.step("Клик по кнопке Выйти")
    def click_on_exit_btn(self):
        self.click_on_element(AccountPageLocators.EXIT)

    @allure.step("Клик по кнопке Сделать заказ")
    def click_on_order_btn(self):
        self.click_on_element(AccountPageLocators.ORDER_BUTTON)

    @allure.step("Создание заказа")
    def create_order(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN_FIRST, MainPageLocators.INGREDIENT_CONTAINER)
        self.click_on_order_btn()

    @allure.step("Ожидание статуса заказа")
    def wait_for_order_info(self):
        return self.find_element_with_wait(AccountPageLocators.ORDER_INFO)

    @allure.step("Ожидание отображения главной страницы")
    def wait_for_main_title(self):
        self.find_element_with_wait(AccountPageLocators.CREATE_BURGER_TITLE)
