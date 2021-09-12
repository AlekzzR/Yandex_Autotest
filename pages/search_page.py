from pages.base_page import BasePage
from pages.locators import ResultSearchPage


class SearchPage(BasePage):

    def link_in_result(self, k):
        result_list = self.browser.find_elements(*ResultSearchPage.SEARCH_RESULT)
        list_of_links = [x.text for x in result_list]
        assert "tensor.ru" in list_of_links[0:k+1], 'В первых пяти результатах отсутствует ссылка на tensor.ru '



