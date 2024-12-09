from selenium.webdriver.common.by import By


class OrderPageLocators:
    FIRST_ORDER = (By.XPATH, '(.//a[contains(@class, "OrderHistory_link__1iNby")])[1]')
    ORDER_INFO_MODAL = (By.XPATH, './/div[contains(@class, "Modal_orderBox__1xWdi")]/parent::div/parent::section')
    INGREDIENT_BUN_FIRST = (By.XPATH,"//a[contains(@class, 'BurgerIngredient_ingredient_')][1]")
    INGREDIENT_CONTAINER = (By.XPATH,".//div[@class = 'constructor-element constructor-element_pos_top']")
    ORDER_BTN = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    EXIT_ORDER_MODAL_BTN = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]/div[contains(@class, 'Modal_modal__container')]/button[@type='button']")
    ORDER_NUMBER_FROM_INFO_MODAL = (By.XPATH, './/h2[@class = "Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]')
    ALL_COUNT_ORDERS = (By.XPATH, '(.//p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"])[1]')
    DAY_COUNT_ORDERS = (By.XPATH, '(.//p[@class = "OrderFeed_number__2MbrQ text text_type_digits-large"])[2]')
    NOW_ORDER = (By.XPATH, '(.//li[@class = "text text_type_digits-default mb-2"])[6]')
    NUMBER_OF_LAST_ORDER_IN_HISTORY = (By.XPATH, '(.//p[@class = "text text_type_digits-default"])[last()]')
    NUMBER_OF_FIRST_ORDER_IN_ORDER_LIST = (By.XPATH, '(.//p[@class = "text text_type_digits-default"])[1]')
    STANDART_ORDER_ID = (By.XPATH, "//h2[text()='9999']")