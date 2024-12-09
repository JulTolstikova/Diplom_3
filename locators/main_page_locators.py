from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR = (By.XPATH, ".//p[text() = 'Конструктор']")
    ORDERS_LIST = (By.XPATH, ".//p[text() = 'Лента Заказов']")
    INGREDIENT_BUN_FIRST = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]")
    INGREDIENT_MODAL_TITLE = (By.XPATH, ".//h2[text() = 'Детали ингредиента']")
    CLOSE_INGREDIENT_MODAL = (By.XPATH, ".//button[@class = 'Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    INGREDIENT_CONTAINER = (By.XPATH,".//div[@class = 'constructor-element constructor-element_pos_top']")
    INGREDIENT_COUNT = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")