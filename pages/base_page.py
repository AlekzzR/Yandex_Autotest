from selenium.common.exceptions import NoSuchElementException


class BasePage:

    def __init__(self, browser, link):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(5)

    def open_link(self):
        self.browser.get(self.link)

    def finding_element(self, how, where):
        try:
            self.browser.find_element(how, where)
        except (NoSuchElementException):
            return False
        return True


