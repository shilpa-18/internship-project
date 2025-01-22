from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    EMAIL_FIELD = (By.CSS_SELECTOR, "[type='email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[data-name='Password']")
    CONTINUE_BUTTON = (By.CSS_SELECTOR, "[wized='loginButton']")
    SECONDARY_TAB = (By.ID,"w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b697-9b22b68b")
    SECONDARY_PAGE = (By.ID, "w-node-bf44e609-bef9-12ba-bb17-9e5d5d1e09d4-7f66df43")
    FILTER_BUTTON = (By.XPATH, "//div[wized='openFiltersWindow']")
    APPLY_FILTER_BUTTON = (By.XPATH, 'a//[wized="applyFilterButtonMLS"]')


    def open_main_page(self):
        self.open_url('https://soft.reelly.io')

    def login_credentials(self, username, password):
        self.input_text(username, *self.EMAIL_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)
        self.click(*self.CONTINUE_BUTTON)

    def left_side_menu(self):
        self.click(MainPage.SECONDARY_TAB)

    def correct_page(self):
        self.click(MainPage.SECONDARY_PAGE)

    def open_filter(self):
        self.click(MainPage.FILTER_BUTTON)
        self.click(MainPage.APPLY_FILTER_BUTTON)

    def verify_prices_in_range(self, lower_price, higher_price):
        PRICE_CARD = (By.CSS_SELECTOR, '[div[wized="unitPriceMLS"]')
        prices = self.driver.find_elements(*PRICE_CARD)

        for price_card in prices:
            price_text = price_card.text.replace(',', '').replace('$', '').strip()
            price = float(price_text)

            if not (lower_price <= price <= higher_price):
                raise AssertionError(f"Price {price} is not within the range {lower_price} - {higher_price}")

        print(f"All prices are within the range {lower_price} - {higher_price}")


