from .pages.base_page import BasePage
from .pages.product_page import ProductPage
from selenium.common.exceptions import NoAlertPresentException
import pytest

base_url = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'


@pytest.mark.parametrize('promo', ['0', '1', '2', '3', '4', '5', '6', pytest.param('7', marks=pytest.mark.xfail), '8', '9'])
def test_guest_can_add_product_to_cart(browser, promo):
    link = f'{base_url}?promo=offer{promo}'
    page = ProductPage(browser, link)
    page.open()
    page.ShouldAddToCart()
    page.ShouldMatchPrices()

    




