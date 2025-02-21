from pages.base_page import BasePage
from locators.password_recovery_locators import PasswordRecoveryLocators
from helpers import *
import allure


class PasswdRecoveryPage(BasePage):
    @allure.step('Открыть страницу восстановления пароля')
    def navigate_to_recovery_passwd_page(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.BUTTON_FORGOT_PASSWORD)
        self.click_on_element(PasswordRecoveryLocators.BUTTON_FORGOT_PASSWORD)

    @allure.step('Проверить отображение поля email')
    def check_displaying_of_input_email(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.INPUT_EMAIL)

    @allure.step('Ввести email')
    def send_email(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.INPUT_EMAIL)
        email = create_random_email()
        self.send_keys_to_input(PasswordRecoveryLocators.INPUT_EMAIL, email)

    @allure.step('Кликнуть на кнопку "Восстановить"')
    def click_on_recovery_button(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.BUTTON_RECOVER)
        self.click_on_element(PasswordRecoveryLocators.BUTTON_RECOVER)

    @allure.step('Проверить отображение поля password')
    def check_displaying_of_input_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.INPUT_PASSWORD)
        return self.check_displaying_of_element(PasswordRecoveryLocators.INPUT_PASSWORD)

    @allure.step('Ввести password')
    def send_password(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.INPUT_PASSWORD)
        passwd = create_random_password()
        self.send_keys_to_input(PasswordRecoveryLocators.INPUT_PASSWORD, passwd)

    @allure.step('Кликнуть на иконку глаза в поле ввода пароля')
    def click_on_eye_icon(self):
        self.wait_visibility_of_element(PasswordRecoveryLocators.EYE_ICON)
        self.click_on_element(PasswordRecoveryLocators.EYE_ICON)

    @allure.step('Проверить, что значение поля password отображается')
    def check_displaying_password_value(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.VALUE_PASSWORD_IS_VISIBLE)

    @allure.step('Проверить, что значение поля password не отображается')
    def check_not_displaying_password_value(self):
        return self.check_displaying_of_element(PasswordRecoveryLocators.VALUE_PASSWORD_IS_INVISIBLE)