from pages.main_page import MainPage

url = "https://yandex.ru/"

def test_search(browser):
    main_page = MainPage(browser, url)
    main_page.open_link()
