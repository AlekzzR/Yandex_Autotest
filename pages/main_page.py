from pages.base_page import BasePage
from pages.locators import MainPageLocate

class MainPage(BasePage):

    def search_field(self):
        assert self.finding_element(*MainPageLocate.SEACH_FIELD)


