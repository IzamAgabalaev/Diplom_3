from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    BUTTON_FORGOT_PASSWORD = By.XPATH, '//a[text() = "Восстановить пароль"]'

    INPUT_EMAIL = (By.CLASS_NAME, 'input__textfield')

    BUTTON_RECOVER = (By.CLASS_NAME, 'button_button__33qZ0')

    INPUT_PASSWORD = (By.CSS_SELECTOR, '.input_type_password .input__textfield')

    EYE_ICON = (By.XPATH, '//div[@class="input__icon input__icon-action"]/*[local-name() = "svg"]')

    VALUE_PASSWORD_IS_VISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                           '"input_status_active")]')

    VALUE_PASSWORD_IS_INVISIBLE = (By.XPATH, '//label[text()="Пароль"]/parent::div[contains(@class, '
                                             '"input_type_password")]')