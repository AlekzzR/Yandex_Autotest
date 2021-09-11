from selenium.common.exceptions import NoSuchElementException

link = "https://yandex.ru/"

class BasePage:


    def __init__(self, browser, url):
        self.browser = browser
        self.url = link
        self.browser.implicitly_wait(5)

    def open_url(self):
        self.browser.get(self.url)

    def finding_element(self, how, where):
        try:
            self.browser.find_element(how, where)
        except (NoSuchElementException):
            return False
        return True


