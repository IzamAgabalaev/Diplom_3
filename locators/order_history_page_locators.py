from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:

    ORDER_CARD = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]')

    ORDER_CARD_TITLE = (By.XPATH, '//*[contains(@class, "OrderHistory_listItem")]//h2')

    ORDER_CARD_ID = (By.XPATH, '(//div[contains(@class, "OrderHistory_textBox")]'
                               '/p[contains(@class, "text_type_digits-default")])[1]')