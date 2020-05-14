from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_be_an_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "The basket is not empty"
        empty_basket = self.text_element(*BasketPageLocators.EMPTY_BASKET)
        assert "Your basket is empty." in empty_basket, "The basket is not empty"

    def should_not_be_product_information(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_INFO), "The basket has product"
