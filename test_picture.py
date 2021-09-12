from pages.picture_page import PicturePage
from pages.main_page import MainPage
import time

url = "https://yandex.ru/"

def test_picture(browser):
    main_page = MainPage(browser, url)
    main_page.open_link()
    main_page.services()
    main_page.open_picture_link()
    picture_page = PicturePage(browser, browser.current_url)
    #picture_page.verify_url()
    picture_page.open_first_category()







