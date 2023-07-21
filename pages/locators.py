from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.ID, "login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "login_form")
    REGISTER_FORM = (By.ID, "register_form")
    EMAIL_FIELD = (By.XPATH, '//*[@id="id_registration-email"]')
    PASSWORD_FIELD = (By.NAME, 'registration-password1')
    PASSWORD_REPEAT_FIELD = (By.NAME, 'registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    ADD_BASKET_BUTTON_LINK = (By.CLASS_NAME, "btn-add-to-basket")
    VIEW_BASKET_BUTTON_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    PRODUCT_NAME_IN_PRODUCT_PAGE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/h1')
    PRODUCT_PRICE_IN_PRODUCT_PAGE = (By.XPATH, '//*[@id="content_inner"]/article/div[1]/div[2]/p[1]')
    PRODUCT_NAME_IN_BASKET_PAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div/strong')
    PRODUCT_PRICE_IN_BASKET_PAGE = (By.XPATH, '//*[@id="messages"]/div[3]/div/p[1]/strong')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="messages"]/div[1]/div')


class BasePageLocators:
    BASKET_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')  # (By.CLASS_NAME, 'btn-cart')
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class BasketPageLocators:
    BASKET_IS_EMPTY = (By.XPATH, '//*[@id="content_inner"]/p')
    BASKET_ITEM = (By.XPATH, '//*[@id="basket_formset"]/div')
