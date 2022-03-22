from .pages.base_page import BasePage
from .pages.product_page import ProductPage

link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'

def test_guest_can_add_product_to_cart(browser):
    page = ProductPage(browser, link)
    page.open()
    page.ShouldAddToCart()
    page.ShouldMatchPrices()

    




