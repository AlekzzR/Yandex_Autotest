from selenium.webdriver.common.by import By


class MainPageLocate:
    SEACH_FIELD = (By.ID, 'text')
    SUGGEST_TABLE = (By.CSS_SELECTOR, '[role=listbox]')
    SERVICES = (By.CSS_SELECTOR, '.services-new__item-title')
    PICTIRE_LINK = (By.CSS_SELECTOR, '[data-statlog="services_new.item.images.2"]')
    WORD_TO_SEARCH = 'Тензор'

class ResultSearchPage:
    SEARCH_RESULT = (By.ID,'#search-result')

