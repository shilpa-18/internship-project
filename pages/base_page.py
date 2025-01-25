from selenium.webdriver.common.by import By
from support.logger import logger

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)
        logger.info(f'Opening URL: {url}')

    def find_element(self, *locator):
        logger.info(f'Searching for element by locator: {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Searching for elements by locator: {locator}')
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Clicking element by locator: {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f'Entering text by locator: {locator}')
        self.driver.find_element(*locator).send_keys(text)

    def click_cart(self, *locator):
        return self.driver.find_element(*locator).click_cart


    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
