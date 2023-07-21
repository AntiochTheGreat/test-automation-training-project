from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.ADD_BASKET_BUTTON_LINK)
        basket_button.click()

    def view_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.VIEW_BASKET_BUTTON_LINK)
        basket_button.click()

    def should_be_correct_product_page(self):
        assert self.should_be_correct_product_name() and self.should_be_correct_product_price(), "Incorrect product " \
                                                                                                 "in the basket "

    def should_be_correct_product_name(self):
        product_name_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_PRODUCT_PAGE)
        value_product_name_product = product_name_product.text
        product_name_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET_PAGE)
        value_product_name_basket = product_name_basket.text
        return value_product_name_product == value_product_name_basket

    def should_be_correct_product_price(self):
        product_price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_PRODUCT_PAGE)
        value_product_price_product = product_price_product.text
        product_price_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET_PAGE)
        value_product_price_basket = product_price_basket.text
        return value_product_price_product == value_product_price_basket

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message not is disappeared, but should be"
