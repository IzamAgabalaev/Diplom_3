from selenium.webdriver.common.by import By


class FeedPageLocators:

    SECTION_ORDERS_LIST = (By.XPATH, '//ul[contains(@class, "OrderFeed_list")]')

    TITLE_OF_ORDERS_FEED = (By.XPATH, '//div[contains(@class, "OrderFeed_orderFeed")]/h1')

    ORDER_IN_FEED = (By.XPATH, '//li[contains(@class, "OrderHistory_listItem")][1]')

    MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains'
                             '(@class, "Modal_orderBox")]')

    TITLE_OF_MODAL_ORDER = (By.XPATH, '//section[contains(@class, "Modal_modal_opened")]//div[contains(@class, '
                                      '"Modal_orderBox")]//h2')

    QUANTITY_OF_ORDERS = (By.XPATH, '//p[text()="Выполнено за все время:"]/following-sibling::p')

    DAILY_QUANTITY_OF_ORDERS = (By.XPATH, '//p[text()="Выполнено за сегодня:"]/following-sibling::p')

    ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li')

    NUMBER_OF_ORDER_IN_PROGRESS = (By.XPATH, '//ul[contains(@class, "OrderFeed_orderListReady")]/li[contains(@class, "text_type_digits-default")]')

    ID_ORDER_CARD_IN_FEED_WITH_SUBSTITUTIONS = (By.XPATH, './/*[text()="{order_id}"]')