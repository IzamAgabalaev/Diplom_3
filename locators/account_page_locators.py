from selenium.webdriver.common.by import By


class AccountPageLocators:

    PROFILE = (By.XPATH, '//a[@href = "/account/profile"]')

    ORDER_HISTORY = (By.XPATH, '//a[@href = "/account/order-history"]')

    BUTTON_LOGOUT = (By.XPATH, '//button[@type = "button"]')

    BUTTON_REGISTER = By.XPATH, '//a[text() = "Зарегистрироваться"]'

    DESCRIPTION_OF_SECTION = (By.XPATH, '//p[contains(@class, "Account_text")]')