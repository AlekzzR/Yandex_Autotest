from pages.main_page import MainPage
import time

url = "https://yandex.ru/"

def test_search(browser):
    main_page = MainPage(browser, url)
    main_page.open_link()
    main_page.search_field()
    main_page.paste_word_to_search_field()
    main_page.suggest()

    time.sleep(3)                   #временное решение для проверки автотеста
