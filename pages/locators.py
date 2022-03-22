from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ProductPageLocators():
    ADD_TO_CART = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_TITLE = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    CONFIRMATION_TITLE = (By.CSS_SELECTOR, '.alertinner :first-child')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    CART_PRICE = (By.CSS_SELECTOR, '.alertinner p strong')