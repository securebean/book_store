import time
import selenium


def test_should_be_add_to_cart_button(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    assert len(browser.find_elements_by_css_selector('#add_to_basket_form > button')) != 0, "There is no such button"

    