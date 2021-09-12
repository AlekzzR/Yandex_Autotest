from pages.base_page import BasePage
from pages.locators import MainPageLocate
from selenium.webdriver.common.keys import Keys

class MainPage(BasePage):

    def search_field(self):
        assert self.finding_element(*MainPageLocate.SEACH_FIELD), 'Поле поиска не найдено'

    def paste_word_to_search_field(self):
        field = self.browser.find_element(*MainPageLocate.SEACH_FIELD)
        field.send_keys(MainPageLocate.WORD_TO_SEARCH)

    def suggest(self):
        assert self.finding_element(*MainPageLocate.SUGGEST_TABLE), 'Таблица с подсказками не появляется'

    def press_enter(self):
        button = self.browser.find_element(*MainPageLocate.SEACH_FIELD)
        button.send_keys(Keys.ENTER)

    def services(self):
        services_bar = self.browser.find_elements(*MainPageLocate.SERVICES)
        link_picture = [serv.text for serv in services_bar]
        assert 'Картинки' in link_picture, 'Ссылка "Картинки" отсутствует на странице'

    def open_picture_link(self):
        picture_link = self.browser.find_element(*MainPageLocate.PICTIRE_LINK)
        picture_link.click()








