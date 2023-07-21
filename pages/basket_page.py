from pages.base_page import BasePage
from pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY), "Basket should been empty, but it isn't empty"

    def should_not_be_basket_item(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEM), "Item is presented, but should not be"
