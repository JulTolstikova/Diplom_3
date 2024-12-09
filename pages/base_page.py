from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.time = 10

    @allure.step("Поиск элемента с задержкой")
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, self.time).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step("Ожидание пока элемент не станет кликабельным")
    def wait_until_clickable(self, locator):
        WebDriverWait(self.driver, self.time).until(EC.element_to_be_clickable(locator))

    @allure.step("Клик по элементу")
    def click_on_element(self, locator):
        filter_field = WebDriverWait(self.driver, self.time).until(expected_conditions.element_to_be_clickable(locator))
        return filter_field.click()

    @allure.step("Поиск элемента")
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Получение текста элемента")
    def get_text_from_element(self, locator):
        element = self.find_element_with_wait(locator)
        return element.text

    @allure.step("Добавление текста в элемент")
    def set_text_to_element(self, locator, text):
        element = self.find_element_with_wait(locator)
        element.send_keys(text)

    @property
    def get_url_for_page_for_test(self):
        return self.driver.current_url

    @allure.step("Скролл до элемента")
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    @allure.step("Проверка поиска элемента с ожиданием")
    def element_exist(self, locator):
        try:
            self.driver.find_element_with_wait(locator)
            return True
        finally:
            return False

    @allure.step("Зажать элемент и перенести на нужное место")
    def drag_and_drop_element(self, source_locator, target_locator):
        source_element = self.find_element_with_wait(source_locator)
        target_element = self.find_element_with_wait(target_locator)

        action = ActionChains(self.driver)
        action.drag_and_drop(source_element, target_element)
        action.perform()

    @allure.step("Ожидание исчезновения элемента")
    def wait_until_missing_element(self, locator):
        WebDriverWait(self.driver, self.time).until(EC.invisibility_of_element_located(locator))
