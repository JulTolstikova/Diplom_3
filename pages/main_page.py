from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
import allure


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке 'Конструктор'")
    def click_on_constructor_btn(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR)

    @allure.step("Клик по кнопке 'Лист заказов'")
    def click_on_orders_list_btn(self):
        self.click_on_element(MainPageLocators.ORDERS_LIST)

    @allure.step("Клик по ингредиенту")
    def click_on_ingredient(self):
        self.click_on_element(MainPageLocators.INGREDIENT_BUN_FIRST)

    @allure.step("Ожидание модалки с информацией об ингридиенте")
    def wait_for_ingredient_modal(self):
        return self.find_element_with_wait(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Клик по кнопке закрытия модального окна")
    def click_on_close_ingredient_modal(self):
        self.click_on_element(MainPageLocators.CLOSE_INGREDIENT_MODAL)

    @allure.step("Проверка, что модальное окно закрыто")
    def check_modal_closed(self):
        return self.element_exist(MainPageLocators.INGREDIENT_MODAL_TITLE)

    @allure.step("Перетаскивание ингредиента в корзину")
    def drag_and_drop_ingredient(self):
        self.drag_and_drop_element(MainPageLocators.INGREDIENT_BUN_FIRST, MainPageLocators.INGREDIENT_CONTAINER)

    @allure.step("Счетчик ингридиентов")
    def get_ingredient_counter(self):
        return self.get_text_from_element(MainPageLocators.INGREDIENT_COUNT)
