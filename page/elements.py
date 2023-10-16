from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.page_objects import PageElement
from time import sleep


class Todo(PageElement):
    """Atributo = locator"""
    title = By.ID, 'title'
    description = By.ID, 'description'
    submit = By.CLASS_NAME, 'btn-primary'
    new = By.XPATH, '//*[@id="navbarNavAltMarkup"]/div/a[2]'
    edit = By.CSS_SELECTOR, 'a.btn-outline-secondary'
    accordion = By.CSS_SELECTOR, 'button.accordion-button'

    def create_task(self, title, description):
        self.find_element(self.new).click()
        self.find_element(self.title).send_keys(title)
        self.find_element(self.description).send_keys(description)
        self.find_element(self.submit).click()

    def edit_task(self, title, description):
        self.find_element(self.accordion).click()

        # Esperar até que o acordeão esteja visível.
        wait = WebDriverWait(self.webdriver, 10)
        wait.until(EC.visibility_of_element_located(self.edit))

        self.find_element(self.edit).click()
        self.find_element(self.title).clear()
        self.find_element(self.title).send_keys(title)
        self.find_element(self.description).clear()
        self.find_element(self.description).send_keys(description)
        self.find_element(self.submit).click()


class Tasks(PageElement):
    accordion = (By.CLASS_NAME, 'accordion-item')

    @property
    def task_list(self):
        accordions = self.find_elements(self.accordion)
        return [Accordion(accordion) for accordion in accordions]


class Accordion:
    def __init__(self, selenium_object):
        self.selenium_object = selenium_object
        self.title = By.CLASS_NAME, 'accordion-header'
        self.description = By.CSS_SELECTOR, 'div.accordion-body strong'
        self.click = By.CSS_SELECTOR, 'button.accordion-button'
        self._do = By.CSS_SELECTOR, 'a.btn-outline-success'
        self._delete = By.CSS_SELECTOR, 'a.btn-outline-danger'
        self._load()

    def do(self):
        self.selenium_object.find_element(*self.click).click()
        sleep(0.5)
        self.selenium_object.find_element(*self._do).click()

    def delete(self):
        self.selenium_object.find_element(*self.click).click()
        sleep(0.5)
        self.selenium_object.find_element(*self._delete).click()

    def _load(self):
        self.title = self.selenium_object.find_element(*self.title).text
        self.selenium_object.find_element(*self.click).click()
        sleep(0.5)
        self.description = self.selenium_object.find_element(*self.description).text
        self.done_text = self.selenium_object.find_element(*self._do).text
        self.selenium_object.find_element(*self.click).click()

    def __repr__(self):
        return f'Accordion(title="{self.title}", description="{self.description}", do="{self.done_text}")'
