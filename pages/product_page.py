from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def go_to_product_page(self):
        button_add_to_the_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        button_add_to_the_basket.click()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Button add to the basket is not presented"

    def should_be_message_about_product_name(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product name is not presented"
        product_name = self.text_element(*ProductPageLocators.PRODUCT_NAME)
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        product_price = self.text_element(*ProductPageLocators.PRODUCT_PRICE)
        return product_name, product_price

    def should_be_message_about_product_name_in_basket(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), "No product name in basket"
        product_name_in_basket = self.text_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET)
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET), "No product price in basket"
        product_price_in_basket = self.text_element(*ProductPageLocators.PRODUCT_PRICE_IN_BASKET)
        return product_name_in_basket, product_price_in_basket

    def element_comparison(self, product, product_in_basket):
        assert product[0] == product_in_basket[0], "Incorrect product added"
        assert product[1] == product_in_basket[1], "Wrong product price"