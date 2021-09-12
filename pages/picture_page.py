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
        time.sleep(1)

    def open_first_picture(self):
        first_picture = self.browser.find_element(*PictureSearchPage.FIRST_PICTURE)
        src_pic_one = first_picture.get_attribute('src')
        first_picture.click()
        src_pic_one_check = first_picture.get_attribute('src')
        assert str(src_pic_one) == str(src_pic_one_check), 'Открылась другая картинка'

    def get_src(self):
        image = self.browser.find_element(*PictureSearchPage.PICTURE_LOCATOR)
        src = image.get_attribute('src')
        return str(src)

    def click_next_button(self):
        button = self.browser.find_element(*PictureSearchPage.NEXT_BUTTON)
        button.click()

    def another_picture(self, src_first_picture):
        second_image = self.browser.find_element(*PictureSearchPage.PICTURE_LOCATOR)
        second_image_src = second_image.get_attribute('src')
        assert src_first_picture != str(second_image_src), 'Открылось тоже самое изображение'

    def click_previous_button(self):
        button = self.browser.find_element(*PictureSearchPage.PREVIOUS_BUTTON)
        button.click()

    def same_image(self, src_first_picture):
        first_image_after_click = self.browser.find_element(*PictureSearchPage.PICTURE_LOCATOR)
        first_image_after_click_src = str(first_image_after_click.get_attribute('src'))
        assert src_first_picture == first_image_after_click_src, 'Это уже другое изображение'











