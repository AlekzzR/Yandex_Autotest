from pages.main_page import MainPage
from pages.search_page import SearchPage
import time

url = "https://yandex.ru/"

def test_search(browser):
    main_page = MainPage(browser, url)
    main_page.open_link()
    main_page.search_field()
    main_page.paste_word_to_search_field()
    main_page.suggest()
    main_page.press_enter()
    search_page = SearchPage(browser, browser.current_url)
    search_page.link_in_result(5)
