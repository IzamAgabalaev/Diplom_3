from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.order_history_page import OrderHistoryPage
from conftest import *
import allure

class TestAccountPage:
    @allure.title('Переход через хедер в профиль через кнопку "Личный кабинет".')
    def test_navigate_to_account_page(self, driver, get_token_in_browser):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        main_page.click_on_personal_account_in_header()
        account_page.wait_visibility_of_description()
        assert account_page.check_displaying_of_description() is True

    @allure.title('Переход в раздел «История заказов»')
    def test_navigate_to_order_history_page(self, driver, get_token_in_browser, create_user_and_order_and_delete):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        order_history_page = OrderHistoryPage(driver)
        main_page.click_on_personal_account_in_header()
        account_page.wait_visibility_of_description()
        account_page.click_on_order_history_button()
        order_history_page.wait_visibility_of_order_card()
        assert 'бургер' in order_history_page.get_text_of_order_card_title()

    @allure.title('Логаут по кнопке "Выйти"')
    def test_logout_from_profile_page(self, driver, get_token_in_browser):
        main_page = MainPage(driver)
        account_page = AccountPage(driver)
        main_page.click_on_personal_account_in_header()
        account_page.wait_visibility_of_description()
        account_page.click_on_logout_button()
        account_page.wait_visibility_of_button_register()
        assert account_page.check_displaying_of_button_register()