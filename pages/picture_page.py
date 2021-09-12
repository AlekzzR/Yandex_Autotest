from pages.locators import PictureSearchPage
from pages.base_page import BasePage
import pytest_check as check
import time


class PicturePage(BasePage):

    def verify_url(self):
        check.equal(self.browser.current_url, "https://yandex.ru/images/",
        'Открылась ссылка ' + self.browser.current_url + ', а не https://yandex.ru/images/')

    def open_first_category(self):
        text_search = self.browser.find_element(*PictureSearchPage.CATEGORY_NAME).text
        self.text_search = text_search
        link = self.browser.find_element(*PictureSearchPage.CATEGORY)
        assert link, 'Переход невозможен'
        link.click()
        time.sleep(1)
        input_field = self.browser.find_element(*PictureSearchPage.INPUT_FIELD)
        input_field.click()
        search = self.browser.find_element(*PictureSearchPage.TEXT_AFTER_SEARCH).text
        self.text_after_search = search
        self.browser.find_element(*PictureSearchPage.TEXT_AFTER_SEARCH).click()
        assert str(search).lower() == str(text_search).lower(), 'Текст категории не совпадает с текстом в окне поиска'



