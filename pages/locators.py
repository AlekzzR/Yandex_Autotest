from selenium.webdriver.common.by import By


class MainPageLocate:
    SEACH_FIELD = (By.ID, 'text')
    SUGGEST_TABLE = (By.CSS_SELECTOR, '[role=listbox]')
    SERVICES = (By.CSS_SELECTOR, '.services-new__item-title')
    PICTIRE_LINK = (By.CSS_SELECTOR, '[data-statlog="services_new.item.images.2"]')
    WORD_TO_SEARCH = 'Тензор'

class ResultSearchPage:
    SEARCH_RESULT = (By.CSS_SELECTOR, '.organic__path .link b')

class PictureSearchPage:
    CATEGORY = (By.CSS_SELECTOR, ".PopularRequestList-Item_pos_0")
    CATEGORY_NAME = (By.CSS_SELECTOR, '.PopularRequestList-SearchText')
    INPUT_FIELD = (By.CSS_SELECTOR, '.input__control')
    TEXT_AFTER_SEARCH = (By.CSS_SELECTOR, '.suggest2-item__text')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.input__control')
    FIRST_PICTURE = (By.CSS_SELECTOR, '.serp-item__link')
    NEXT_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_next")
    PREVIOUS_BUTTON = (By.CSS_SELECTOR, ".CircleButton_type_prev")
    PICTURE_LOCATOR = (By.CSS_SELECTOR, ".MMImage-Origin")






