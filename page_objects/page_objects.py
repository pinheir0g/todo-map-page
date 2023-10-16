from abc import ABC

"""
Padrão Page Object
Pode ser utilizado em qualquer outro projeto
"""


class SeleniumObject:
    def find_element(self, locator):
        return self.webdriver.find_element(*locator)

    def find_elements(self, locator):
        return self.webdriver.find_elements(*locator)


class Page(ABC, SeleniumObject):
    def __init__(self, webdriver, url=''):
        self.webdriver = webdriver
        self.url = url
        self._reflection()

    def open(self):
        self.webdriver.get(self.url)

    def _reflection(self):
        for attr in dir(self):
            attr_val = getattr(self, attr)
            if isinstance(attr_val, PageElement):
                attr_val.webdriver = self.webdriver


class PageElement(ABC, SeleniumObject):
    def __init__(self, webdriver=None):
        self.webdriver = webdriver
