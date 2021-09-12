from pages.picture_page import PicturePage
from pages.main_page import MainPage

url = "https://yandex.ru/"

def test_picture(browser):
    main_page = MainPage(browser, url)
    main_page.open_link()
    main_page.services()
