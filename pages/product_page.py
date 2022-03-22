from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def ShouldAddToCart(self):
        button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART)
        button.click()
        self.solve_quiz_and_get_code(self.browser)
        product_title = (self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)).text
        confirmation_title = (self.browser.find_element(*ProductPageLocators.CONFIRMATION_TITLE)).text
        assert product_title == confirmation_title, 'Added title does not match requested title'

    def ShouldMatchPrices(self):
        product_price = (self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)).text
        cart_price = (self.browser.find_element(*ProductPageLocators.CART_PRICE)).text
        assert product_price == cart_price, 'Prices do not match'
