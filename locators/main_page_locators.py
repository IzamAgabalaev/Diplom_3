from selenium.webdriver.common.by import By

class MainPageLocators:

    OVERLAY = By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div"

    BUTTON_LOGIN_IN_MAIN = By.XPATH, './/button[text() = "Войти в аккаунт"]'

    BUTTON_PERSONAL_ACCOUNT = (By.XPATH, '//p[text()="Личный Кабинет"]/parent::a')

    BUTTON_MAKE_THE_ORDER = (By.XPATH, '//button[text()="Оформить заказ"]')

    HEADER_OF_PAGE_CONSTRUCTOR = (By.XPATH, '//p[text() = "Конструктор"]')

    SELECTED_BUTTON = (By.XPATH, ('//div[@class = '
                                  '"tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]'))

    CONSTRUCTOR_TITLE = (By.XPATH, '//section[contains(@class, "BurgerIngredients_ingredients")]/h1')

    BUNS_BLOCK = (By.XPATH, '//span[text() = "Булки"]')

    SAUCES_BLOCK = (By.XPATH, '//span[text() = "Соусы"]')

    FILLINGS_BLOCK = (By.XPATH, '//span[text() = "Начинки"]')

    BUTTON_ORDER_FEED_IN_HEADER = (By.XPATH, '//p[text()="Лента Заказов"]/parent::a/parent::li')

    INGREDIENT_1 = (By.XPATH, '(.//p[@class="BurgerIngredient_ingredient__text__yp3dH"])[1]')

    HEADER_OF_MODAL_DETAILS = (By.XPATH, '//h2[contains(@class, "Modal_modal__title") and contains(text(), "Детали")]')

    BUTTON_CLOSE_MODAL = (By.XPATH, '//section[contains(@class, '
                                    '"Modal_modal_opened")]//button[contains(@class, "close")]')

    BURGER_INGREDIENT = (By.XPATH, './/*[@alt="Флюоресцентная булка R2-D3"]')

    PLACE_FOR_INGREDIENTS = (By.XPATH, '//section[contains(@class, "BurgerConstructor_basket")]')

    CONTENT_OF_ORDER = (By.CSS_SELECTOR, '.constructor-element_pos_top .constructor-element__row')

    BUTTON_MAKE_ORDER = (By.CLASS_NAME, 'button_button__33qZ0')

    COUNT_OF_INGREDIENT = (By.XPATH, './/a[@class="BurgerIngredient_ingredient__1TVf6 ml-4 mr-4 mb-8"]//p['
                                     '@class="counter_counter__num__3nue1"][1]')

    CONFIRMATION_MODAL_OF_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]/div[contains'
                                             '(@class, "Modal_modal__container")]')

    NUMBER_OF_ORDER_IN_MODAL_CONFIRMATION = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//h2')

    BUTTON_CLOSE_CONFIRMATION = (By.CSS_SELECTOR, 'button.Modal_modal__close_modified__3V5XS.Modal_modal__close__TnseK')
