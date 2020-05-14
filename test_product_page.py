import pytest
from .pages.product_page import ProductPage
import time

#@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
  #                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
  #                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
 #                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
  #                                "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
   #                               "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    #                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
     #                             pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
      #                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
       #                           "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9" ])


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    main_page_element = product_page.should_be_message_about_product()
    product_page.should_be_add_button()
    product_page.go_to_product_page()
    product_page.solve_quiz_and_get_code()
    product_page_element = product_page.should_be_message_about_product_in_basket()
    product_page.element_comparison(main_page_element, product_page_element)

#Проверка отсутствия элемента (в данном случае он здесь есть)
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_button()
    product_page.go_to_product_page()
    product_page.solve_quiz_and_get_code()
    product_page.should_not_be_success_message()

#Проверка отсутствия элемента (в данном случае его здесь нет)
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()

#проверка исчезновение элемента (в данном случае он не здесь не исчезает)
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_be_add_button()
    product_page.go_to_product_page()
    product_page.solve_quiz_and_get_code()
    product_page.should_be_success_message()




