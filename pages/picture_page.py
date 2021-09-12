from pages.locators import PictureSearchPage
from pages.base_page import BasePage
import pytest_check as check
import time


class PicturePage(BasePage):

    def verify_url(self):
        check.equal(self.browser.current_url, "https://yandex.ru/images/",
        'Открылась ссылка ' + self.browser.current_url + ', а не https://yandex.ru/images/')

    def open_first_category(self):
        link = self.browser.find_element(*PictureSearchPage.CATEGORY)
        link.click()
        time.sleep(3)


